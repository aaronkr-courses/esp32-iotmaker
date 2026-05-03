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