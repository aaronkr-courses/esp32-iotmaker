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