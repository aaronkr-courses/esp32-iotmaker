## AI 프롬프트 실습 7-4: 아날로그 출력 프로그램 만들기 - 퍼텐쇼미터로 LED 밝기 조절하기
## 프롬프트 
```
마이크로파이썬 프로그램을 만들고, 코드를 설명해 줘. 

from machine import… 
import time 
time.sleep_ms()를 사용함. 

2개의 LED와 2개의 버튼을 사용함.
모듈 pinno에는 핀 번호 상수 값이 저장되어 있음. 
import pinno 
POTENTIOMETER_PIN = pinno.L2_IN 
BUTTON_1_PIN = pinno.L3_IN 
BUTTON_2_PIN = pinno.L4_IN 
LED_1_PIN = pinno.L5_IN 
LED_2_PIN = pinno.L6_IN 

POTENTIOMETER에 대해:
	메소드 atten(): 3.3V까지 읽도록 지정
	메소드 width(): 해상도 12비트
potentiometer_percent = (POTENTIOMETER 읽은 값 / 4095 * 100)의 정수 

첫 번째 버튼은 PULL_UP해야 하고 두 번째 버튼은 PULL_DOWN해야 함. 
BUTTON_1_PRESSED_VALUE = 0 
BUTTON_2_PRESSED_VALUE = 1

첫 번째 LED는 전류 소싱 방식으로 연결되어 있고,
두 번째 LED는 전류 싱킹 방식으로 연결되어 있음. 
led_1_on_percent =  potentiometer_percent %
led_1_off_percent =  0 % 
led_2_on_percent =  (100 - potentiometer_percent) % 
led_2_off_percent =  100 % 

LED를 on할 때는 PWM을 led_x_on_percent에 따름.
LED를 off할 때는 PWM을 led_x_off_percent에 따름. 
PWM에 대해:    
	메소드 duty()를 사용함.    
	메소드 freq(): 1000 

led_on_off_state = False 
prev_potentiometer = 0

프로그램 시작하면:    
	Print("버튼_1을 누르면 on(), 버튼_2를 누르면 off()")    
	Print("불이 켜지면 너브를 돌려서 밝기를 조절하세요")    
	두 LED를 off

다음은 연속 실행이야:    
	current_potentiometer와 prev_potentiometer의 차이가 2% 이상이면:        
		prev_potentiometer = current_potentiometer                    
		led_on_off_state = True이면:             
			두 LED를 켬(PWM: led_x_on_percent)            
			print("밝기 조절: {led_1_on_percent}%")    
	current_버튼_상태 != prev_버튼_상태:           
		디바운스 20ms        
		버튼_1이 PRESSED이면:             
			두 LED를 on             
			print("on(): {led_1_on_percent}%")         
		버튼_2가 PRESSED이면::             
			두 LED를 off             
			print("off()")     
	모든 while loop에 대해:        
		prev_버튼_상태 = current_버튼_상태        
		1ms 중지
```
## AI가 만든 코드
프로그램: 7_4_control_leds_with_potentiometer.py
```python
from machine import Pin, ADC, PWM
import time
import pinno

# 핀 번호 상수 설정
POTENTIOMETER_PIN = pinno.L2_IN
BUTTON_1_PIN = pinno.L3_IN
BUTTON_2_PIN = pinno.L4_IN
LED_1_PIN = pinno.L5_IN
LED_2_PIN = pinno.L6_IN

# 상수 설정
BUTTON_1_PRESSED_VALUE = 0
BUTTON_2_PRESSED_VALUE = 1
PWM_FREQ = 1000

# 핀 객체 설정
potentiometer = ADC(Pin(POTENTIOMETER_PIN))
potentiometer.atten(ADC.ATTN_11DB)  # 3.3V까지 읽을 수 있도록 설정
potentiometer.width(ADC.WIDTH_12BIT)  # 12비트 해상도 설정

BUTTON_1 = Pin(BUTTON_1_PIN, Pin.IN, Pin.PULL_UP)
BUTTON_2 = Pin(BUTTON_2_PIN, Pin.IN, Pin.PULL_DOWN)

led_1 = PWM(Pin(LED_1_PIN))
led_2 = PWM(Pin(LED_2_PIN))

# 초기 설정
led_1.freq(PWM_FREQ)
led_2.freq(PWM_FREQ)
led_on_off_state = False
prev_potentiometer = 0
prev_BUTTON_1_state = BUTTON_1.value()
prev_BUTTON_2_state = BUTTON_2.value()

# 초기 메시지 출력
print("버튼_1을 누르면 on(), 버튼_2를 누르면 off()")
print("불이 켜지면 너브를 돌려서 밝기를 조절하셔요")

# 두 LED를 끔
led_1.duty(0)
led_2.duty(1023)

while True:
    # 현재 포텐셔미터 값을 읽음
    current_potentiometer = potentiometer.read()
    potentiometer_percent = int(current_potentiometer / 4095 * 100)

    # 포텐셔미터 값이 2% 이상 변했는지 확인
    if abs(current_potentiometer - prev_potentiometer) > (4095 * 0.02):
        prev_potentiometer = current_potentiometer

        # LED가 켜져 있을 때 밝기 조절
        if led_on_off_state:
            led_1_on_percent = potentiometer_percent
            led_2_on_percent = 100 - potentiometer_percent

            led_1.duty(int(led_1_on_percent / 100 * 1023))
            led_2.duty(int(led_2_on_percent / 100 * 1023))

            print(f"밝기 조절: {led_1_on_percent}%")

    # 버튼 상태 확인
    current_BUTTON_1_state = BUTTON_1.value()
    current_BUTTON_2_state = BUTTON_2.value()

    # 버튼 상태가 변경되었는지 확인 (디바운스 적용)
    if current_BUTTON_1_state != prev_BUTTON_1_state or current_BUTTON_2_state != prev_BUTTON_2_state:
        time.sleep_ms(20)  # 디바운스 시간

        # 버튼_1이 눌렸을 때
        if BUTTON_1.value() == BUTTON_1_PRESSED_VALUE:
            led_on_off_state = True
            led_1.duty(int(potentiometer_percent / 100 * 1023))
            led_2.duty(int((100 - potentiometer_percent) / 100 * 1023))
            print(f"on(): {potentiometer_percent}%")

        # 버튼_2가 눌렸을 때
        if BUTTON_2.value() == BUTTON_2_PRESSED_VALUE:
            led_on_off_state = False
            led_1.duty(0)
            led_2.duty(1023)
            print("off()")

    # 이전 버튼 상태 업데이트
    prev_BUTTON_1_state = current_BUTTON_1_state
    prev_BUTTON_2_state = current_BUTTON_2_state

    # 1ms 중지
    time.sleep_ms(1)
```
## AI가 만든 코드 설명
### 1. ADC와 PWM으로 핀 정의하기
퍼텐쇼미터는 ADC를 사용하고, LED는 PWM으로 제어됩니다. 

### 2. 퍼텐쇼미터 입력 설정
atten( )은 3.3V까지 읽기 위해 설정되었고, width( )는 12비트 해상도로 값을 읽기 위해 설정되었습니다. 

### 3. 버튼_1과 버튼_2 설정
버튼_1은 PULL_UP, 버튼_2는 PULL_DOWN으로 설정되어 버튼을 누른 상태를 감지합니다. 

### 4. 초기 설정
프로그램은 초기 메시지를 출력하고, 두 LED를 끈 상태에서 시작합니다. 

### 5. 반복 실행 
while 루프에서는
	-  퍼텐쇼미터의 값이 2% 이상 변동할 때만 LED의 밝기가 조절됩니다.
	-  버튼이 눌리면, LED가 켜지거나 꺼지며, 그 상태에 따라 밝기를 조절하거나 LED를 끕니다.
	-  버튼 상태 변화 시 20ms의 디바운스를 적용합니다.
	
### 6. LED 밝기 제어
PWM 제어는 duty( )를 통해 이루어지며, potentiometer_percent에 따라 LED 밝기를 조절합니다.

이 프로그램은 두 버튼과 퍼텐쇼미터를 활용해 LED의 상태와 밝기를 조절하는 시스템입니다. 
