## AI 프롬프트 실습 7-1: 디지털 입력 프로그램 만들기 - 버튼 눌림 값 찾기
## 프롬프트 
```
마이크로파이썬 프로그램을 다음 조건에 따라 만들고, 코드를 설명해 줘.
from machine import …
import time

2개의 버튼을 사용함.
모듈 pinno에는 핀 번호 상수 값이 저장되어 있음.
import pinno
BUTTON_1_PIN = pinno.L3_IN
BUTTON_2_PIN = pinno.L4_IN
첫 번째 버튼은 PULL_UP해야 하고 두 번째 버튼은 PULL_DOWN해야 함.
프로그램 시작하면
    Print("버튼_1과 버튼_2를 눌러보세요.")
다음은 계속 실행해야 해.
각각의 버튼 값을 읽어서 값이 달라지면
    Print("버튼_x의 값이 바뀜",버튼_x의 값)
    20ms의 디바운스 여유를 둠.
```
## AI가 만든 코드
프로그램: 7_1_read_two_buttons.py
```python
from machine import Pin
import time
import pinno as pinno

# 핀 번호 상수 설정
BUTTON_1_PIN = pinno.L3_IN  # 첫 번째 버튼(PULL_UP)
BUTTON_2_PIN = pinno.L4_IN  # 두 번째 버튼(PULL_DOWN)

# 버튼 설정
button_1 = Pin(BUTTON_1_PIN, Pin.IN, Pin.PULL_UP)   # PULL_UP 방식
button_2 = Pin(BUTTON_2_PIN, Pin.IN, Pin.PULL_DOWN) # PULL_DOWN 방식

# 시작 메시지 출력
print("버튼_1과 버튼_2를 눌러 보셔요")

# 각 버튼의 이전 상태 저장
prev_button_1_state = button_1.value()
prev_button_2_state = button_2.value()

# 메인 루프
while True:
    # 버튼_1 상태 확인
    current_button_1_state = button_1.value()
    if current_button_1_state != prev_button_1_state: 
        print("버튼_1의 값이 바뀜", current_button_1_state)
        prev_button_1_state = current_button_1_state  # 상태 업데이트
        time.sleep(0.02)  # 디바운스 (20ms)

    # 버튼_2 상태 확인
    current_button_2_state = button_2.value()
    if current_button_2_state != prev_button_2_state:
        print("버튼_2의 값이 바뀜", current_button_2_state)
        prev_button_2_state = current_button_2_state  # 상태 업데이트
        time.sleep(0.02)  # 디바운스 (20ms)
```
## AI가 만든 코드 설명
### 1. 핀 번호 설정
BUTTON_1_PIN과 BUTTON_2_PIN은 pinno.L3_IN과 pinno.L4_IN으로 설정되어 있습니다. 이
핀들은 각각 풀업(PULL_UP)과 풀다운(PULL_DOWN)으로 설정됩니다.

### 2. 버튼 설정
- button_1은 풀업 방식(Pin.PULL_UP)으로 설정되어 버튼을 누르지 않으면 기본적으로 HIGH(1),
누르면 LOW(0)를 반환합니다.
- button_2는 풀다운 방식(Pin.PULL_DOWN)으로 설정되어 버튼을 누르지 않으면 LOW(0), 누르
면 HIGH(1)을 반환합니다.

### 3. 메인 루프
- 프로그램은 계속 실행되면서 각 버튼의 상태를 읽습니다.
- 이전 상태(prev_button_1_state, prev_button_2_state)와 비교해 버튼 상태가 변하면 메시지를
출력합니다.
- 상태가 변경될 때마다 20ms의 대기 시간(디바운스)을 둬서 떨림 현상을 방지합니다.
이 코드는 두 버튼의 상태 변화를 실시간으로 감지하고, 상태가 변경될 때만 출력하며, 디바운스 처리를
통해 노이즈를 제거합니다.

이 코드는 두 버튼의 상태 변화를 실시간으로 감지하고, 상태가 변경될 때만 출력하며, 디바운스 처리를
통해 노이즈를 제거합니다.