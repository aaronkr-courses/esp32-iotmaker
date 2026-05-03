## AI 프롬프트 실습 8-3:  하드웨어 인터럽트 프로그램 만들기 - 클래스를 학습시켜 새로운 프로그램 만들기
## 프롬프트 
```
마이크로파이썬 프로그램을 만들고, 코드를 설명해 줘. 

from machine import … 
import time 
time.sleep_ms()를 사용함. 

# 사용자 준비 라이브러리 
from timerrun import TimerRun 
from button   import Button 
from blink    import Blink 

# 모듈 pinno에는 핀 번호 상수 값이 저장되어 있음. 
import pinno 

# 2개의 LED와 2개의 버튼을 사용함. 
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

버튼_2:
	핀 번호: BUTTON_2_PIN    
	PULL_DOWN 해야 함.
	
# run 오브젝트: Timer(0)에 의해 10ms 간격으로 호출하도록 지정함. 
run = TimerRun(Timer(0),period=10) 
run.start() # 호출 시작
run.stop() # 호출 중지

# 지정된 함수는 호출에 등록함. 
run.add(함수 이름) 
# 지정된 함수는 호출에서 제외함. 
run.remove(함수 이름) 

button_1 = Button(Pin(BUTTON_1_PIN,Pin.IN,Pin.PULL_UP),inverted=True) 
button_2 = Button(Pin(BUTTON_2_PIN,Pin.IN,Pin.PULL_DOWN),inverted=False) 

def 호출_함수(response):    
	response의 구조       
		{'event': ...,       
			'event_name': ...,       
			'number': ...,       
			'clicks': 여기에 버튼을 누른 횟수가 옴.      
		 }    
	response['clicks']는 event=MULTIPLE일 때 사용함.   

# event는 PRESSED, RELEASED, LONG, SINGLE, DOUBLE, COUNT, MULTIPLE 

# PRESSED: 
button_1.add(event=Button.PRESSED,callback=호출_함수) 
# MULTIPLE: 버튼을 누른 횟수를 돌려줌. button_1.add(event=Button.MULTIPLE,callback=호출_함수) 
# COUNT: 누른 횟수가 지정한 number와 같을 때 response['clicks']로 돌려줌. 
button_1.add(event=Button.COUNT,callback=호출_함수,number=3) 

# 버튼 상태 주기적 확인하기 위해 TimerRun에 등록
run.add(button_1.run) # 버튼 주기적 확인
run.add(button_2.run) # 버튼 주기적 확인

led_1 = Blink(Pin(LED_1_PIN,Pin.OUT),inverted=Fasle) 
led_2 = Blink(Pin(LED_2_PIN,Pin.OUT),inverted=True) 

# LED 상태를 주기적으로 확인하기 위해 TimerRun에 등록
run.add(led_1.run) 
run.add(led_2.run) 

# on/off를 5회, count=0이면 무한 반복
led_1.begin_blink(on=500,off=300,count=5)

# blink 끝내기
led_1.end_blink() 

#on,off,toggle 
led_1.on() 
led_1.off() 
led_1.toggle()

다음과 같이 프로그램을 만들어 줘. 

1. 프로그램 시작하면:   
	print("버튼_1을 누른 횟수만큼 LED_1이 점멸합니다.")   
	print("버튼_2를 누르고 있으면 LED_2가 빠르게 점멸하고, 떼면 꺼집니다.") 
2. 버튼_1을 누른 횟수만큼(Button.MULTIPLE 사용)    
	LED_1을 점멸하기(on=500, off=300,count=누른 수) 
3. 버튼_2를 누르고 있으면(Button.PRESSED 사용)    
	LED를 점멸하고(on=250, off=250),   
	떼면(Button.RELEASED 사용) off() 
4. while True:       
	time.sleep_ms(1)	
```
## AI가 만든 코드
프로그램: 8_3_timerrun_button_blink.py
```python
from machine import Pin, Timer
import time
from timerrun import TimerRun
from button import Button
from blink import Blink
import pinno

# 핀 번호 상수 설정
BUTTON_1_PIN = pinno.L3_IN
BUTTON_2_PIN = pinno.L4_IN
LED_1_PIN = pinno.L5_IN
LED_2_PIN = pinno.L6_IN

# LED 설정
led_1 = Blink(Pin(LED_1_PIN,Pin.OUT), inverted=False)  # 전류 소싱
led_2 = Blink(Pin(LED_2_PIN,Pin.OUT), inverted=True)   # 전류 싱킹

# 버튼 설정
button_1 = Button(Pin(BUTTON_1_PIN,Pin.IN,Pin.PULL_UP), inverted=True)   # PULL_UP
button_2 = Button(Pin(BUTTON_2_PIN,Pin.IN,Pin.PULL_DOWN), inverted=False) # PULL_DOWN

# TimerRun 오브젝트 생성
run = TimerRun(Timer(0), period=10)

# 버튼_1의 눌린 수만큼 LED_1 점멸
def handle_button_1(response):
    if response['event'] == Button.MULTIPLE:
        clicks = response['clicks']
        print(f"버튼_1을 {clicks}번 눌렀습니다. LED_1이 {clicks}번 점멸합니다.")
        led_1.begin_blink(on=500, off=300, count=clicks)

# 버튼_2를 누르고 있을 때 LED_2 점멸, 떼면 꺼짐
def handle_button_2(response):
    if response['event'] == Button.PRESSED:
        print("버튼_2를 누르고 있습니다. LED_2가 빠르게 점멸합니다.")
        led_2.begin_blink(on=250, off=250, count=0)  # 무한 반복
    elif response['event'] == Button.RELEASED:
        print("버튼_2에서 손을 뗐습니다. LED_2가 꺼집니다.")
        led_2.off()

# 버튼 이벤트 등록
button_1.add(event=Button.MULTIPLE, callback=handle_button_1)  # 누른 횟수에 따라 LED_1 점멸
button_2.add(event=Button.PRESSED, callback=handle_button_2)   # 버튼_2를 누르면 LED_2 점멸
button_2.add(event=Button.RELEASED, callback=handle_button_2)  # 버튼_2에서 손을 떼면 LED_2 꺼짐

# TimerRun에 버튼과 LED 상태 주기적 확인 등록
run.add(button_1.run)
run.add(button_2.run)
run.add(led_1.run)
run.add(led_2.run)

# 프로그램 시작 메시지 출력
print("버튼_1을 누른 횟수만큼 LED_1이 점멸합니다")
print("버튼_2를 누르고 있으면 LED_2가 빠르게 점멸하고, 떼면 꺼집니다")

# TimerRun 시작
run.start()

# 메인 루프: 1ms 간격으로 주기적으로 상태 확인
while True:
    time.sleep_ms(1)
```
## AI가 만든 코드 설명

### 1. LED와 버튼 설정
-   led_1은 전류 소싱 방식으로 제어되며, led_2는 전류 싱킹 방식으로 제어됩니다.
-   button_1은 PULL_UP 방식으로, button_2는 PULL_DOWN 방식으로 설정되었습니다. 

### 2. 버튼_1의 눌린 횟수에 따라 LED_1 점멸
-   Button.MULTIPLE 이벤트는 버튼_1을 누른 횟수를 추적합니다.
-   handle_button_1( ) 함수는 눌린 횟수를 출력하고, LED_1을 해당 횟수만큼 점멸시킵니다.
-   on=500, off=300으로 LED_1의 점멸 속도를 설정했습니다. 

### 3. 버튼_2를 누르고 있으면 LED_2 점멸, 떼면 LED_2 꺼짐
-  Button.PRESSED 이벤트는 버튼_2가 눌렸을 때 발생하며, handle_button_2( ) 함수는 LED_2를 빠르게 깜빡이게 합니다.
-  Button.RELEASED 이벤트는 버튼_2에서 손을 떼면 발생하며, handle_button_2( ) 함수는 LED_2를 끄는 동작을 처리합니다.
-  LED_2는 on=250, off=250으로 빠르게 깜빡이도록 설정되어 있으며, 손을 뗄 때는 LED_2가 완전히 꺼집니다.

### 4. TimerRun을 통한 주기적 상태 확인
-  TimerRun 오브젝트는 10ms 간격으로 버튼과 LED의 상태를 주기적으로 확인해 이벤트를 처리합니다.
-  run.add(button_1.run) 및 run.add(button_2.run)으로 버튼 상태를 주기적으로 확인하고, run. add(led_1.run) 및 run.add(led_2.run)으로 LED 상태를 확인합니다. 

### 5. 메인 루프
while True 루프 내에서 time.sleep_ms(1)을 호출해 1ms마다 반복 실행됩니다. 이 루프는 프로그램이 종료되지 않도록 유지하면서 TimerRun과 LED 상태를 지속적으로 확인합니다.