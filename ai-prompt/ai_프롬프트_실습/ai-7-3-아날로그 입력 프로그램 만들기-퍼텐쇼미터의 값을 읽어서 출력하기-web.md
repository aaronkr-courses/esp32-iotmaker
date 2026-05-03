## AI 프롬프트 실습 7-3: 아날로그 입력 프로그램 만들기-페텐쇼미터의 값을 읽어서 출력하기
## 프롬프트 
```
마이크로파이썬 프로그램을 다음 조건에 따라 만들고, 코드를 설명해 줘. 
from machine import … 
import time 
time.sleep() 대신 time.sleep_ms()를 사용함.

모듈 pinno에는 핀 번호 상수 값이 저장되어 있음. 
import pinno 
POTENTIOMETER_PIN = pinno.L2_IN 
POTENTIOMETER의 전압은 3.3V까지 읽음.
프로그램 시작하면    
	print("퍼텐쇼미터의 노브를 돌려보세요.")  
first = True
다음은 연속 실행이야:    
	0.5초 단위로 퍼텐쇼미터의 값을 읽음.    
	first가 True 또는 prev_값과 current_값의 차이가 4095의 0.5% 이상이면        
		읽은 값과 4095에 대한 백분율을 프린터함.
```
## AI가 만든 코드
프로그램: 7_3_read_potentiometer.py
```python
from machine import ADC, Pin
import time
import pinno

# 핀 번호 상수 설정
POTENTIOMETER_PIN = pinno.L2_IN

# ADC 설정: 포텐셔미터 입력 핀을 ADC로 사용
potentiometer = ADC(Pin(POTENTIOMETER_PIN))

# ADC 분해능 설정 (기본 12비트, 최대 4095)
potentiometer.atten(ADC.ATTN_11DB)  # 최대 3.3V까지 측정 가능

# 퍼텐쇼미터 읽기 및 값 비교에 필요한 변수
prev_value = 0
first = True
THRESHOLD = 4095 * 0.005  # 0.5% 변화 임계값

# 프로그램 시작 메시지
print("퍼텐쇼미터의 노브를 돌려보세요.")

while True:
    # 퍼텐쇼미터 값 읽기
    current_value = potentiometer.read()
    
    # first가 True이거나, 값이 0.5% 이상 변했을 경우 출력
    if first or abs(current_value - prev_value) > THRESHOLD:
        # 4095에 대한 백분율 계산
        percentage = (current_value / 4095) * 100  
        print(f"퍼텐쇼미터 값: {current_value}, 백분율: {percentage:.2f}%")
        
        # 첫 번째 출력 후 first를 False로 설정
        first = False
        prev_value = current_value  # 이전 값 갱신

    # 1ms 대기
    time.sleep_ms(1)

    # 0.5초 간격으로 퍼텐쇼미터 값을 읽음
    time.sleep(0.5)

```
## AI가 만든 코드 설명
### 1. 퍼텐쇼미터 입력 설정
POTENTIOMETER_PIN 핀에서 퍼텐쇼미터 값을 읽기 위해 ADC를 사용합니다. ADC.ATTN_11DB 감쇠 설정으로 0V에서 3.3V까지의 전압을 읽을 수 있습니다. 

### 2. first 플래그 설정
프로그램이 처음 실행될 때 무조건 값을 출력하기 위해 first 변수를 True로 설정했습니다. 

### 3. 퍼텐쇼미터 값 읽기
0.5초마다 potentiometer.read( )로 퍼텐쇼미터 값을 읽습니다. 이 값은 0에서 4095 사이의 정수입니다. 

### 4. 값 차이 판단
prev_value와 current_value의 차이가 4095의 0.5% 이상일 때만 값을 출력합니다. 이 조건이 처음 실행 시에도 적용되도록 했습니다. 

### 5. 백분율 계산 및 출력
퍼텐쇼미터 값과 4095에 대한 백분율을 계산해 출력합니다. 

### 6. 0.5초 간격 실행
time.sleep_ms(500)을 사용해 매 0.5초마다 퍼텐쇼미터 값을 읽고 처리합니다.

이 프로그램은 퍼텐쇼미터 값이 처음 실행되거나, 이전 값과의 차이가 0.5% 이상일 때만 값을 출력하도록 구현되었습니다.
