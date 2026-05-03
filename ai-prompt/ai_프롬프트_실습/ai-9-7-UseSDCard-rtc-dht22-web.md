## AI 프롬프트 실습 9-7: 온습도 정보를 시간과 함께 SD 카드에 기록하기
## 프롬프트 
file: ai-9-7-UseSDCard-rtc-dht22.md
```
( 여기에 'ai-patterns.md'의 내용을 넣으세요. )

components:
- 센서읽기_앞부분

- DHT22:
    이름: dht
    pin_gpio: P.DHT

- i2c:
    scl_pin: P.SCL
    sda_pin: P.SDA

- spi:
    sck_pin: P.SCK
    mosi_pin: P.MOSI
    miso_pin : P.MISO

- sdcard_mount_make_next_file:
    cs_pin: P.CS
    file_prefix: temphum
    file_digits: 3
    file_ext: json

- rtc

- date_time_str_func

def read_sensor():

    data = dht.read()
    p = Parse(data)
    
    print(f"{p.name}> 온도: {p.value[1]}°{p.temp_unit}, 습도: {p.value[0]}%")
    
    data['Time'] = date_time_str_func()
    
    ok, msg = sd.append_json(data)
    if not ok:
        print(f"SD 카드 기록 실패: {msg}")
    else:
        print(f"데이터 기록 완료: {data}")

components:
- 타이머:
    이름: timer_sensor
    period: 5*1000
    callback: read_sensor

- 센서읽기_뒷부분
```
## AI가 만든 코드
프로그램: 9_8_usesdcard_rtc_dht22.py
```python
import json
from timerrun import TimerRun
from run import Run
from parse import Parse
import pinno as P
from machine import Pin, I2C, SPI
from dht22sensor import DHT22Sensor
from usesdcard import UseSDCard
from ds1307 import DS1307

# Run 객체 초기화
run = Run()

# DHT22 센서 초기화
dht = DHT22Sensor(pin_gpio=P.DHT)

# I2C 초기화
i2c = I2C(0, scl=Pin(P.SCL), sda=Pin(P.SDA))

# SPI 초기화
spi = SPI(1, sck=Pin(P.SCK), mosi=Pin(P.MOSI), miso=Pin(P.MISO))

# SD 카드 초기화 및 파일 생성
sd = UseSDCard(spi_bus=spi, cs_gpio=P.CS)
ok, msg = sd.mount_sdcard()
if not ok:
    print(f"SD 카드 마운트 실패: {msg}")
else:
    ok, msg = sd.make_next_file(prefix='temphum', digits=3, ext='json')
    if not ok:
        print(f"SD 카드 파일 생성 실패: {msg}")
    else:
        print(f"SD 카드 파일 생성 완료: {sd.get_file()}")

# RTC 초기화
rtc = DS1307(i2c=i2c) # 책에서 rtc = DS1307(i2c)는 오류임. 

# 날짜와 시간 문자열 생성 함수
def date_time_str_func():
    """
    RTC에서 현재 날짜와 시간 정보를 가져와 문자열로 반환
    """
    year, month, day, hour, minute, second, week_day, sub_second = rtc.datetime
    date_time_str = f'{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'
    return date_time_str

# 센서 데이터 읽기 및 기록 함수
def read_sensor():
    """
    DHT22 데이터를 읽고 SD 카드에 기록
    """
    try:
        # DHT22 데이터 읽기
        data = dht.read()
        p = Parse(data)

        # 출력 정보
        print(f"{p.name}> 온도: {p.values[1]}°{p.temp_unit}, 습도: {p.values[0]}%")

        # 시간 정보 추가
        data['Time'] = date_time_str_func()

        # JSON 형식으로 SD 카드에 기록
        ok, msg = sd.append_json(data)
        if not ok:
            print(f"SD 카드 기록 실패: {msg}")
        else:
            print(f"데이터 기록 완료: {data}")
    except Exception as e:
        print(f"센서 읽기 실패: {e}")

# 타이머 설정
timer_sensor = TimerRun(period=5 * 1000, callback=read_sensor)
run.add(timer_sensor.run)

# 메인 실행
def main():
    while True:
        run.run()

if __name__ == '__main__':
    main()
```