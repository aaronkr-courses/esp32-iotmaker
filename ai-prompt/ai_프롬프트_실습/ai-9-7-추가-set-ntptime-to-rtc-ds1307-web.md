## AI 프롬프트 실습 9-7-추가: NTP 서버를 읽어서 RTC 모듈 DS1307에 세팅하기
## 프롬프트 
file: ai-9-7-추가-set-ntptime-to-rtc-ds1307.md
```
마이크로파이썬 프로그램을 만들어 줘.

ESP32를 WiFi를 통해 인터넷의 타임 서버에 연결하고,
I2C로 연결된 RTC 모듈 DS1307에 현재 시간을 세팅하고,
5초를 기다렸다가 다시 DS1307을 읽어서 날짜,요일,시간을 출력할거야.

DS1307 라이브러리는 import 하지 말고 직접 코드로 작성해 줘.

-code: 
  import pinno as P
  WIFI_SSID: your_ssid
  WIFI_PASSWORD: your_password
  SDA_PIN: P.SDA
  SCL_PIN: P.SCL
  TIME_ZONE: +9

프로그램 단계별로 메시지를 출력해 줘.
- 와이파이 정보 (ipconfig())
- 타임 서버 이름
- 세팅된 날짜,요일,시간 정보
- 읽어온 날짜,요일,시간 정보
```
## AI가 만든 코드

아래는 ESP32에서 동작하는 마이크로파이썬 예시 코드이며,  
1) ESP32를 와이파이에 연결하고,  
2) NTP 서버로부터 시간을 받아 내장 RTC(UTC 시간)를 설정한 뒤,  
3) I2C를 통해 DS1307 외부 RTC에 현재 시간을 세팅하고,  
4) 5초 뒤 DS1307에서 다시 시간을 읽어 출력하는 흐름을 보여줍니다.  

또한 코드 내 `rtc1307` 라이브러리를 따로 import하지 않고, DS1307(0x68)에 직접 레지스터를 쓰고 읽는 방식을 사용했습니다.

---

## 1. 프로그램 설명

### (1) 와이파이 연결
- `connect_wifi()` 함수에서 `network.WLAN(network.STA_IF)` 객체를 통해 스테이션 모드로 동작하게 합니다.
- `active()`를 사용해 활성화되어 있지 않으면 활성화하고,  
  `isconnected()`를 통해 실제 연결 여부를 확인합니다.
- 연결이 완료되면 `ifconfig()` 결과(IP, 서브넷마스크, 게이트웨이, DNS)를 확인할 수 있습니다.

### (2) NTP 서버 동기화
- `ntptime` 모듈을 사용하여 설정된 NTP 서버(`pool.ntp.org`)로부터 시간을 받아옵니다.
- `ntptime.settime()`을 통해 내부 RTC(UTC 기준)를 동기화합니다.
- 동기화 후 `time.time()`을 호출하면 UTC 타임스탬프(1970년 1월 1일 00시0분0초부터 지난 초)가 반환됩니다.
- `TIME_ZONE`(예: +9)을 곱하여 로컬 시각(예: KST)을 계산한 뒤, `time.localtime()`으로 가공된 형식으로 얻어냅니다.

### (3) DS1307에 시간 세팅
- DS1307(0x68)은 7Byte 레지스터(0~6)에 각각 [초,분,시,요일,일,월,년도(2자리)]를 **BCD**(Binary Coded Decimal) 형식으로 저장합니다.
- 마이크로파이썬의 `time.localtime()`에서 반환되는 요일 값(`tm_wday`)은 월요일=0, 일요일=6 형태입니다.  
  DS1307은 월=1, 화=2, … 일=7 형태를 사용하므로 변환이 필요합니다.
- `dec2bcd()`, `bcd2dec()` 함수로 10진수 ↔ BCD 변환을 수행합니다.
- 세팅 시, 연도(예: 2025)는 내부적으로 2자리(25)만 저장합니다.

### (4) DS1307에서 시간 읽어 출력
- DS1307에서 7Byte 레지스터를 읽어 동일하게 BCD -> 10진 변환을 하여 (year, month, day, wday, hour, minute, second)를 반환받습니다.
- 5초 대기(`time.sleep(5)`) 후에 다시 DS1307을 읽어 실제로 저장된 시간이 올바른지 확인하고, 형식에 맞춰 출력합니다.

---

## 2. 전체 코드
프로그램: 9_8_x_set_ntptime_to_rtc_ds1307.py
```python
import network
import time
import ntptime
from machine import Pin, I2C
import pinno as P  # (문제에서 주어진 가상의 라이브러리: SDA_PIN, SCL_PIN 등이 있다고 가정)

# [사용자 설정값들]
WIFI_SSID = "your_ssid"
WIFI_PASSWORD = "your_password"
SDA_PIN = P.SDA       # 예: 21번 핀
SCL_PIN = P.SCL       # 예: 22번 핀
TIME_ZONE = +9        # 한국 KST는 UTC+9
NTP_SERVER = "pool.ntp.org"  # 사용할 NTP 서버 주소

# DS1307 기본 I2C 주소
DS1307_I2C_ADDR = 0x68

# BCD 변환 함수들
def bcd2dec(bcd):
    """
    BCD(Binary Coded Decimal)로 표현된 값을 10진수 정수로 변환.
    예: 0x12 -> 18
    """
    return ((bcd >> 4) * 10) + (bcd & 0x0F)

def dec2bcd(dec):
    """
    10진수 정수를 BCD(Binary Coded Decimal) 형태로 변환.
    예: 18 -> 0x12
    """
    return ((dec // 10) << 4) + (dec % 10)

class DS1307:
    """
    DS1307 외부 RTC를 I2C를 통해 직접 제어하기 위한 클래스.
    레지스터 0~6: 초,분,시,요일,일,월,년도(2자리)
    """
    def __init__(self, i2c, address=DS1307_I2C_ADDR):
        self.i2c = i2c
        self.address = address

    def set_datetime(self, year, month, day, weekday, hour, minute, second):
        """
        DS1307 레지스터에 날짜/시간을 써넣는다.
        - year: 4자리 연도 (예: 2025)
        - month: 1 ~ 12
        - day: 1 ~ 31
        - weekday: 1=월, 2=화, 3=수, 4=목, 5=금, 6=토, 7=일
        - hour, minute, second: 시/분/초 (24시간 형식)
        """
        # DS1307은 내부적으로 2자리 연도만 저장 (20xx)
        year_2digit = year % 100

        # 레지스터 순서대로 초, 분, 시, 요일, 일, 월, 연도
        data = bytearray(7)
        data[0] = dec2bcd(second) & 0x7F  # CH(bit7)는 0으로: DS1307 동작
        data[1] = dec2bcd(minute)
        data[2] = dec2bcd(hour)          # 24시간 모드
        data[3] = dec2bcd(weekday)       # 1=월 ~ 7=일
        data[4] = dec2bcd(day)
        data[5] = dec2bcd(month)
        data[6] = dec2bcd(year_2digit)

        # 0x00(첫 번째 레지스터)부터 7바이트 연속 써주기
        self.i2c.writeto_mem(self.address, 0x00, data)

    def get_datetime(self):
        """
        DS1307에서 현재 날짜/시간을 읽어 반환.
        반환값: (year, month, day, weekday, hour, minute, second)
        """
        data = self.i2c.readfrom_mem(self.address, 0x00, 7)
        second = bcd2dec(data[0] & 0x7F)  # bit7(CH)는 제외
        minute = bcd2dec(data[1])
        hour   = bcd2dec(data[2] & 0x3F) # 24시간 모드
        weekday= bcd2dec(data[3])        # 1=월 ~ 7=일
        day    = bcd2dec(data[4])
        month  = bcd2dec(data[5])
        year_2digit = bcd2dec(data[6])
        year   = 2000 + year_2digit      # DS1307은 20xx만 저장 가능
        return (year, month, day, weekday, hour, minute, second)

def connect_wifi(ssid, password):
    """
    주어진 SSID, PASSWORD로 와이파이에 연결.
    연결 완료되면 네트워크 정보(IP, 서브넷, 게이트웨이 등) 확인 가능.
    """
    print("[1/4] 와이파이 연결 중...")

    # 1) 스테이션 모드 활성화
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.active():
        sta_if.active(True)

    # 2) 연결 시도
    if not sta_if.isconnected():
        sta_if.connect(ssid, password)
        # 연결될 때까지 대기
        while not sta_if.isconnected():
            time.sleep(0.5)

    print("[1/4] 와이파이 연결 완료")
    return sta_if

def main():
    # 1) 와이파이 연결
    station = connect_wifi(WIFI_SSID, WIFI_PASSWORD)
    ip_info = station.ifconfig()
    print(f"[WiFi 정보] IP: {ip_info[0]}, Netmask: {ip_info[1]}, "
          f"Gateway: {ip_info[2]}, DNS: {ip_info[3]}\n")

    # 2) NTP 서버 동기화
    print("[2/4] NTP 서버 설정 및 동기화 진행...")
    print(f"NTP 서버: {NTP_SERVER}")
    ntptime.host = NTP_SERVER
    ntptime.settime()  # 내부 RTC를 UTC로 세팅

    # 내부 RTC는 현재 UTC이므로, 로컬 타임(예: KST +9)을 위해 보정
    now = time.time() + TIME_ZONE * 3600
    local_time = time.localtime(now)
    # local_time 구조: (year, month, mday, hour, minute, second, weekday, yearday)

    # 3) I2C 초기화 후 DS1307에 시간 세팅
    print("[3/4] DS1307(RTC) 시간 세팅 중...")
    i2c = I2C(1, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=100000)
    ds = DS1307(i2c)

    # MicroPython weekday(월=0, 화=1, 수=2, 목=3, 금=4, 토=5, 일=6) -> DS1307(1~7)
    ds1307_wday = local_time[6] + 1
    if ds1307_wday > 7:
        ds1307_wday = 7

    year, month, day = local_time[0], local_time[1], local_time[2]
    hour, minute, second = local_time[3], local_time[4], local_time[5]

    ds.set_datetime(year, month, day, ds1307_wday, hour, minute, second)

    # 설정된 시간 출력
    weekday_kor = ["월", "화", "수", "목", "금", "토", "일"]
    print("[세팅된 날짜/시간 정보]")
    print(f" {year}년 {month}월 {day}일 "
          f"({weekday_kor[ds1307_wday - 1]}) "
          f"{hour:02d}:{minute:02d}:{second:02d}\n")

    # 4) 5초 후 DS1307에서 시간 읽어오기
    print("[4/4] 5초 대기 후 DS1307 다시 읽어오기...")
    time.sleep(5)
    year_r, month_r, day_r, wday_r, hour_r, min_r, sec_r = ds.get_datetime()

    # 읽어온 시간 출력
    print("[읽어온 날짜/시간 정보]")
    print(f" {year_r}년 {month_r}월 {day_r}일 "
          f"({weekday_kor[wday_r - 1]}) "
          f"{hour_r:02d}:{min_r:02d}:{sec_r:02d}\n")

if __name__ == "__main__":
    main()
```

---

## 3. 프로그램 해설

1. **와이파이 연결**  
   - `connect_wifi()` 함수에서 `network.STA_IF`(스테이션 모드)로 동작하게 하고,  
     `active()`가 `False`라면 `active(True)`로 활성화합니다.  
   - `isconnected()`가 `False`면 `connect(ssid, password)`로 연결을 시도하고,  
     연결이 완료될 때까지 `while not sta_if.isconnected(): time.sleep(0.5)`로 대기합니다.  

2. **NTP 시간 동기화**  
   - `ntptime.host = NTP_SERVER`로 원하는 NTP 서버(`"pool.ntp.org"`)를 설정한 뒤,  
     `ntptime.settime()`을 실행하면 내장 RTC가 UTC 기준으로 재설정됩니다.  
   - 이후 `time.time()`은 UTC 기준 타임스탬프를 반환하므로, `TIME_ZONE`(+9)을 고려해서 로컬 시각으로 변환합니다.

3. **DS1307 시간 설정**  
   - `machine.I2C(1, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=100000)`로 I2C를 초기화하고, DS1307 객체를 생성합니다.  
   - DS1307는 레지스터 0x00 ~ 0x06에 `[초,분,시,요일,일,월,년도(2자리)]`를 **BCD** 형식으로 저장하기 때문에,  
     연도/월/일/요일/시/분/초를 `dec2bcd()`로 변환 후 `i2c.writeto_mem()`으로 레지스터에 쓰는 방식을 사용합니다.

4. **요일 변환**  
   - MicroPython의 `time.localtime()`에서 `tm_wday`는 월=0, 화=1, 수=2, … 일=6 을 사용합니다.  
   - DS1307는 1=월, 2=화, … 7=일 을 사용합니다. 따라서 `tm_wday + 1`을 하여 세팅해야 합니다.  
   - 일요일(`tm_wday = 6`)의 경우 `6 + 1 = 7` → DS1307의 일요일(7)로 저장 가능합니다.

5. **DS1307에서 시간 읽어 확인**  
   - 5초 대기(`time.sleep(5)`) 후 `ds.get_datetime()`으로 다시 레지스터(0x00~0x06)을 읽어,  
     BCD → 10진수로 복원합니다.  
   - 연도는 DS1307 내부에 2자리만 저장(예: 25)되므로, 2000 + (2자리 연도)로 계산하여 완전한 4자리 연도를 얻습니다.

6. **출력 형식**  
   - `[WiFi 정보]` -> IP, 서브넷, 게이트웨이, DNS  
   - `[세팅된 날짜/시간 정보]` -> DS1307에 쓰기 직전의 시간(연-월-일 (요일) 시:분:초)  
   - `[읽어온 날짜/시간 정보]` -> 실제 DS1307에서 읽은 날짜/요일/시간

---

위 코드와 해설을 참고하여 원하는 기능(네트워크 연결, 시간 동기화, RTC 세팅 및 확인)을 구현하실 수 있습니다.  
추가로 궁금하신 사항이 있으면 언제든 말씀해주세요!