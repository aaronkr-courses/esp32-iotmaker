## AI 프롬프트 실습 7-2: 디지털 출력 프로그램 만들기 - 버튼을 눌러서 LED 조작하기
## 프롬프트 
```
마이크로파이썬 프로그램을 다음 조건에 따라 만들고, 코드를 설명해 줘.

from machine import …
import time
time.sleep_ms()를 사용함.

2개의 LED와 버튼을 사용함.
모듈 pinno에는 핀 번호 상수 값이 저장되어 있음.
import pinno
BUTTON_1_PIN = pinno.L3_IN
BUTTON_2_PIN = pinno.L4_IN
LED_1_PIN = pinno.L5_IN
LED_2_PIN = pinno.L6_IN

첫 번째 버튼은 PULL_UP해야 하고 두 번째 버튼은 PULL_DOWN해야 함.
BUTTON_1_PRESSED_VALUE = 0
BUTTON_2_PRESSED_VALUE = 1

첫 번째 LED는 전류 소싱 방식으로 연결되어 있고,
두 번째 LED는 전류 싱킹 방식으로 연결되어 있음.
LED_1_ON_VALUE = 1
LED_1_OFF_VALUE = not LED_1_ON_VALUE
LED_2_ON_VALUE = 0
LED_2_OFF_VALUE = not LED_2_ON_VALUE

프로그램 시작하면
    Print("버튼_1을 누르면 on(), 버튼_2를 누르면 off()")
    두 LED_x.value(LED_x_OFF_VALUE) 지정

다음은 연속 실행이야:
    각각의 버튼이 눌리면:
        버튼_1이면 두 LED에 대해 LED_x.value(LED_x.ON_VALUE)
        버튼_2이면 두 LED에 대해 LED_x.value(LED_x.OFF_VALUE)
        버튼_x가 눌린 사실과 on 또는 off하는지를 print함.
        20ms의 디바운스 여유를 둠.
    모드 while loop에 대해:
        prev_버튼_상태 = current_버튼_상태
        1ms 중지
```
## AI가 만든 코드
프로그램: 7_2_read_two_buttons_on_off_leds.py
```python
from machine import Pin
import time
import pinno

# 핀 번호 상수 설정
BUTTON_1_PIN = pinno.L3_IN
BUTTON_2_PIN = pinno.L4_IN
LED_1_PIN = pinno.L5_IN
LED_2_PIN = pinno.L6_IN

# 버튼이 눌린 값 설정
BUTTON_1_PRESSED_VALUE = 0  # 버튼_1 눌림
BUTTON_2_PRESSED_VALUE = 1  # 버튼_2 눌림

# LED의 ON/OFF 값 설정
LED_1_ON_VALUE = 1   # 전류 소싱 방식으로 연결된 LED_1 ON
LED_1_OFF_VALUE = not LED_1_ON_VALUE
LED_2_ON_VALUE = 0   # 전류 싱킹 방식으로 연결된 LED_2 ON
LED_2_OFF_VALUE = not LED_2_ON_VALUE

# 핀 설정: LED는 출력, 버튼은 입력(PULL_UP, PULL_DOWN)
led_1 = Pin(LED_1_PIN, Pin.OUT)
led_2 = Pin(LED_2_PIN, Pin.OUT)
button_1 = Pin(BUTTON_1_PIN, Pin.IN, Pin.PULL_UP)
button_2 = Pin(BUTTON_2_PIN, Pin.IN, Pin.PULL_DOWN)

# 초기 LED 상태 설정: OFF
led_1.value(LED_1_OFF_VALUE)
led_2.value(LED_2_OFF_VALUE)

# 시작 메시지 출력
print("버튼_1을 누르면 on(), 버튼_2를 누르면 off()")

# 버튼 상태 추적
prev_BUTTON_1_state = button_1.value()
prev_BUTTON_2_state = button_2.value()

while True:
    # 현재 버튼 상태 읽기
    current_BUTTON_1_state = button_1.value()
    current_BUTTON_2_state = button_2.value()

    # 버튼_1이 눌렸는지 확인
    if current_BUTTON_1_state == BUTTON_1_PRESSED_VALUE and prev_BUTTON_1_state != current_BUTTON_1_state:
        # LED1, LED2 켜기
        led_1.value(LED_1_ON_VALUE)
        led_2.value(LED_2_ON_VALUE)
        print("버튼_1 누름, 두 LED on")
        time.sleep_ms(20)  # 디바운스 시간

    # 버튼_2가 눌렸는지 확인
    if current_BUTTON_2_state == BUTTON_2_PRESSED_VALUE and prev_BUTTON_2_state != current_BUTTON_2_state:
        # LED1, LED2 끄기
        led_1.value(LED_1_OFF_VALUE)
        led_2.value(LED_2_OFF_VALUE)
        print("버튼_2 누름, 두 LED off")
        time.sleep_ms(20)  # 디바운스 시간

    # 상태 갱신
    prev_BUTTON_1_state = current_BUTTON_1_state
    prev_BUTTON_2_state = current_BUTTON_2_state

    # CPU 사용량 줄이기 위해 1ms 중지
    time.sleep_ms(1)
```
## AI가 만든 코드 설명

### 1. 핀 설정 및 초기화
- 버튼_1은 PULL_UP 설정, 버튼_2는 PULL_DOWN 설정으로 초기화합니다.
- led_1은 전류 소싱 방식이므로 ON일 때 1, led_2는 전류 싱킹 방식이므로 ON일 때 0이 됩니다.

### 2. LED 초기화
프로그램 시작 시 LED는 OFF 상태 (led_1.value(LED_1_OFF_VALUE), led_2.value(LED_2_
OFF_VALUE))로 설정됩니다.

### 3. 버튼 눌림 확인
버튼이 눌렸을 때만 LED 상태를 변경합니다. 버튼_1이 눌리면 두 LED를 켜고, 버튼_2가 눌리면 두
LED를 끕니다.

### 4. 디바운스 처리
20ms 동안의 지연(time.sleep_ms(20))을 통해 버튼 떨림을 방지합니다.

### 5. CPU 사용량 감소
매 루프에서 1ms 지연(time.sleep_ms(1))을 두어 CPU 사용량을 줄입니다.

이 코드는 버튼_1을 누르면 두 LED가 켜지고, 버튼_2를 누르면 두 LED가 꺼지도록 동작합니다.

