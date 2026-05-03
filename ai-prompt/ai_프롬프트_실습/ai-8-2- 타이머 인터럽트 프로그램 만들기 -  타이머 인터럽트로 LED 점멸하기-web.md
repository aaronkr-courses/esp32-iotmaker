## AI 프롬프트 실습 8-2: 타이머 인터럽트 프로그램 만들기 - 타이머 인터럽트로 LED 점멸하기
## 프롬프트 
```
마이크로파이썬 프로그램을 다음 조건에 따라 만들고, 코드를 설명해 줘. 
from machine import … 
import time time.sleep_ms()를 사용함. 
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

LED_2:
	핀 번호: LED_2_PIN
	전류 싱킹으로 연결함.    
	LED_2_ON_VALUE = 0    
	LED_2_OFF_VALUE = not LED_2_ON_VALUE
	
버튼_1:
	핀 번호: BUTTON_1_PIN    
	PULL_UP 해야 함.    
	irq 설정:        
		falling(HIGH에서 LOW)        
		handler: button_1_mode_change()

버튼_2:
	핀 번호: BUTTON_2_PIN    
	PULL_DOWN 해야 함.    
	irq 설정:        
		rising과 falling 동시
		handler: button_2_blink_or_not() 

led_1_blink():    
	LED_1을 토글함. 

led_2_blink():    
	LED_2를 토글함. 

button_1_mode_change():    
	LED_1_blink_active = not LED_1_blink_active
	만약 LED_1_blink_active == True:        
		LED_1 on        
		Timer(0) 활성화:            
			0.5초 간격으로 주기적임.            
			Handler: led_1_blink()
	아니면:          
		Timer(0) 해제          
		LED_1 off

	디바운스를 위해:          
		IRQ 해제          
		300ms 중지
		다시 IRG 시작

button_2_blink_or_not():	
	만약 버튼_2가 눌린 상태면:        
		LED_2 on        
		Timer(0) 할성화:            
			0.25초 간격으로 주기적임.             
			Handler: led_2_blink()
	아니면:        
		Timer(0) 해제        
		LED_1 off

프로그램 시작하면    
	Print("버튼_1과 버튼_2를 각각 눌러서 두 LED의 점멸을 확인하세요.")
	두 LED를 off   

while True:    
	pass
```
## AI가 만든 코드
프로그램: 8_2_interrupt_buttons_control_led_blinks.py
```python
from machine import Pin, Timer
import time
import pinno

# 핀 설정
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

# 변수 설정
LED_1_blink_active = False
LED_1_timer = Timer(0)
LED_2_timer = Timer(1)

# LED_1 토글 함수 (0.5초 간격)
def led_1_blink(timer):
    led_1.value(not led_1.value())

# LED_2 토글 함수 (0.25초 간격)
def led_2_blink(timer):
    led_2.value(not led_2.value())

# 버튼_1 눌렀을 때 모드 변경
def button_1_mode_change(pin):
    global LED_1_blink_active
    LED_1_blink_active = not LED_1_blink_active

    if LED_1_blink_active:
        led_1.value(LED_1_ON_VALUE)  # LED_1 켜기
        # 0.5초 간격으로 LED_1 점멸
        LED_1_timer.init(period=500, mode=Timer.PERIODIC, callback=led_1_blink)
    else:
        # LED_1 타이머 해제 및 LED_1 끔
        LED_1_timer.deinit()
        led_1.value(LED_1_OFF_VALUE)

    # 디바운스 처리 (IRQ 해제 후 300ms 대기)
    button_1.irq(handler=None)  # IRQ 해제
    time.sleep_ms(300)         # 300ms 대기
    button_1.irq(trigger=Pin.IRQ_FALLING, handler=button_1_mode_change)  # IRQ 다시 설정

# 버튼_2 눌렀을 때 LED_2 점멸 제어
def button_2_blink_or_not(pin):
    if button_2.value() == 1:  # 버튼_2가 눌린 상태
        led_2.value(LED_2_ON_VALUE)  # LED_2 켜기
        LED_2_timer.init(period=250, mode=Timer.PERIODIC, callback=led_2_blink)  # 0.25초 간격 LED_2 점멸
    else:  # 버튼_2가 해제된 상태
        LED_2_timer.deinit()
        led_2.value(LED_2_OFF_VALUE)  # LED_2 끔

# IRQ 설정
button_1.irq(trigger=Pin.IRQ_FALLING, handler=button_1_mode_change)
button_2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_2_blink_or_not)

# 프로그램 시작 메시지 출력 및 LED 초기화
print("버튼_1과 버튼_2를 각각 눌러서 두 LED의 점멸을 확인하셔요")
led_1.value(LED_1_OFF_VALUE)
led_2.value(LED_2_OFF_VALUE)

# 메인 루프
while True:
    pass

# 버튼_1은 LED_1의 점멸을 토글함.버튼_2를 누르는 동안 LED_2 점멸함.
```
## AI가 만든 코드 설명

### 1. 핀 설정
-  Pin.OUT : LED를 제어하기 위해 GPIO 핀을 출력 모드로 설정합니다.
-  Pin.IN :  버튼 입력을 받기 위해 GPIO 핀을 입력 모드로 설정합니다.
-  PULL_UP, PULL_DOWN : 각각의 버튼의 초기 상태를 설정합니다. 

### 2. 타이머 설정
-  Timer(0) :  LED_1의 점멸을 제어하며, 0.5초 간격으로 LED_1을 토글합니다.
-  Timer(1) : LED_2의 점멸을 제어하며, 0.25초 간격으로 LED_2를 토글합니다. 

### 3. 핸들러 함수
-  button_1_mode_change : 버튼_1을 누르면 LED_1의 점멸 활성화 여부가 토글됩니다. 활성화되면 0.5초 간격으로 LED_1이 점멸하고, 비활성화되면 타이머를 해제하고 LED_1을 끕니다.
-   button_2_blink_or_not : 버튼_2를 누르면 0.25초 간격으로 LED_2가 점멸하고, 버튼을 떼면 LED_2가 꺼집니다. 

### 4. 디바운스 처리
버튼_1의 디바운스를 위해 IRQ를 일시적으로 해제하고, 300ms 동안 대기한 후 다시 활성화해 잘못된 입력을 방지합니다. 

### 5. 프로그램 시작
프로그램이 시작되면 한국어로 안내 메시지를 출력하고 두 LED를 초기 상태로 꺼 둡니다.