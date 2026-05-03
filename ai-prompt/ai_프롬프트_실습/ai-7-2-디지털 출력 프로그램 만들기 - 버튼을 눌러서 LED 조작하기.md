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
