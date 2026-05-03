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