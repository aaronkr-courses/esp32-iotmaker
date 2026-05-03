## AI 프롬프트 실습 8-1: 하드웨어 인터럽트 프로그램 만들기 - 버튼의 인터럽트로 LED 조작하기
## 프롬프트 
```
마이크로파이썬 프로그램을 다음 조건에 따라 만들고, 코드를 설명해 줘. 

from machine import … 
import time 
time.sleep_ms()를 사용함. 

2개의 LED와 2개의 버튼을 사용함.
모듈 pinno에는 핀 번호 상수 값이 저장되어 있음. 
import pinno 
BUTTON_1_PIN = pinno.L3_IN 
BUTTON_2_PIN = pinno.L4_IN 
LED_1_PIN = pinno.L5_IN 
LED_2_PIN = pinno.L6_IN 

LED_1:    
	핀 번호: LED_1_PIN    
	전류 소싱으로 연결함.    
	LED_1_ON_VALUE = 1    
	LED_1_OFF_VALUE = not LED_1_ON_VALUE

LED_2:핀 
	번호: LED_2_PIN
	전류 싱킹으로 연결함.    
	LED_2_ON_VALUE = 0    
	LED_2_OFF_VALUE = not LED_2_ON_VALUE 

led_1_toggle():    
	LED_1이 켜져 있으면 off    
	LED_1이 꺼져 있으면 on
	디바운스를 위해:       
		irq(handler=None)       
		300ms 중지
		다시 irq 실행

led_2_on_off():
	버튼_2의 값이 HIGH(눌렸으면) LED_2를 on
	버튼_2의 값이 LOW(해제되었으면) LED_2를 off
	
버튼_1:
	핀 번호: BUTTON_1_PIN    
	PULL_UP 해야 함.    
	irq 설정:        
		falling(HIGH에서 LOW)        
		handler: led_1_toggle()

버튼_2:
	핀 번호: BUTTON_2_PIN    
	PULL_DOWN 해야 함.    
	irq 설정:        
		rising과 falling 동시         
		handler: led_2_on_off()

프로그램 시작하면    
	Print("버튼_1을 누르면 LED_1 toggle(), 버튼_2를 누르면 LED_2 on() 떼면 off()")
	두 LED를 off   

다음은 연속 실행이야:
	모든 while loop에 대해:        
		1ms 중지
```
## AI가 만든 코드
프로그램: 8_1_interrupt_buttons_control_leds.py
```python
from machine import Pin
import time
import pinno

# 핀 번호 상수 설정
BUTTON_1_PIN = pinno.L3_IN
BUTTON_2_PIN = pinno.L4_IN
LED_1_PIN = pinno.L5_IN
LED_2_PIN = pinno.L6_IN

# LED 상태 값 설정
LED_1_ON_VALUE = 1
LED_1_OFF_VALUE = not LED_1_ON_VALUE
LED_2_ON_VALUE = 0
LED_2_OFF_VALUE = not LED_2_ON_VALUE

# LED 핀 설정
led_1 = Pin(LED_1_PIN, Pin.OUT)
led_2 = Pin(LED_2_PIN, Pin.OUT)

# 버튼 핀 설정
button_1 = Pin(BUTTON_1_PIN, Pin.IN, Pin.PULL_UP)
button_2 = Pin(BUTTON_2_PIN, Pin.IN, Pin.PULL_DOWN)

# LED_1 토글 함수 (디바운스 포함)
def led_1_toggle(pin):
    # LED_1 토글
    if led_1.value() == LED_1_ON_VALUE:
        led_1.value(LED_1_OFF_VALUE)
    else:
        led_1.value(LED_1_ON_VALUE)

    # IRQ 비활성화 (디바운스 처리)
    button_1.irq(handler=None)  # IRQ 비활성화
    time.sleep_ms(300)         # 300ms 대기
    button_1.irq(trigger=Pin.IRQ_FALLING, handler=led_1_toggle)  # IRQ 다시 활성화

# LED_2 on/off 함수
def led_2_on_off(pin):
    if button_2.value() == 1:  # 버튼_2가 눌렸을 때
        led_2.value(LED_2_ON_VALUE)
    else:  # 버튼_2가 해제되었을 때
        led_2.value(LED_2_OFF_VALUE)

# IRQ 설정: 버튼_1의 FALLING 엣지에서 led_1_toggle() 실행
button_1.irq(trigger=Pin.IRQ_FALLING, handler=led_1_toggle)

# IRQ 설정: 버튼_2의 RISING, FALLING에서 led_2_on_off() 실행
button_2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=led_2_on_off)

# 프로그램 시작 시 메시지 출력
print("버튼_1을 누르면 LED_1 toggle(), 버튼_2를 누르면 LED_2 on() 떼면 off()")

# LED 초기 상태 off
led_1.value(LED_1_OFF_VALUE)
led_2.value(LED_2_OFF_VALUE)

# 메인 루프
while True:
    time.sleep_ms(1)
```
## AI가 만든 코드 설명

### 1. 핀 설정 및 변수 정의
pinno 모듈에서 핀 번호 상수를 불러와 버튼과 LED 핀을 설정합니다. LED_1은 전류 소싱으로 연결되고, LED_2는 전류 싱킹으로 연결됩니다. LED_1_ON_VALUE = 1, LED_2_ON_VALUE = 0으로 설정됩니다. 

### 2. led_1_toggle 함수
LED_1을 토글하는 함수입니다. 디바운스 처리를 위해, LED_1을 토글한 후 버튼_1의 인터럽트를 해제(irq(handler=None))하고, 300ms 동안 대기 후 다시 인터럽트를 활성화합니다. 

### 3. led_2_on_off 함수
버튼_2가 눌리면 LED_2를 켜고, 해제되면 LED_2를 끄는 함수입니다.

### 4. IRQ 설정
-  버튼_1은 PULL_UP 저항을 사용하고, FALLING(HIGH에서 LOW) 시 led_1_toggle( ) 함수가 호출됩니다.
-  버튼_2는 PULL_DOWN 저항을 사용하고, RISING과 FALLING 모두에서 led_2_on_off( ) 함수가 호출됩니다. 

### 5. 프로그램 시작 시 메시지 출력
한국어로 프로그램 동작에 대한 설명을 출력하며, LED_1과 LED_2를 초기 상태로 꺼 둡니다. 

### 6. 메인 루프
time.sleep_ms(1)으로 1ms 동안 대기하면서 프로그램을 계속 실행합니다.