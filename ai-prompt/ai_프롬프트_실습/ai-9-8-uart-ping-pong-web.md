## AI 프롬프트 실습 9-8: UART1과 UART2가 정보를 주고받기
## 프롬프트 
file: ai-9-8-uart-ping-pong.md
```
다음의 조건에 따라 마이크로파이썬 프로그램을 만들고 설명해 줘.
- 동일한 개발 보드에 있는 UART1과 UART2를 서로 연결할거야. 
  import pinno as P 
  uart1 = UART(1, baudrate=9600, tx=P.TX, rx=P.RX, timeout=10)
  uart2 = UART(2, baudrate=9600, tx=P.R5, rx=P.R6, timeout=10)
- UART1에서 UART2로 {'ser':1}을 데이터로 보내면,
  UART2에서는 5초를 기다렸다가 ser에 1을 더하여 {'ser':2}를 UART1으로 돌려 보내게 돼.
- UART1에도 5초를 기다렸다가 받은 데이터 ser에 1을 더하여 {'ser':3}를 UART2으로 보내는 행위를 무한 반복하는 거야.
- 각 단계에서 UART의 이름과 받은 ser을 출력하고, 보낼 때도 이름과 ser을 출력하면 돼.
```
## AI가 만든 코드
프로그램: 9_10_uart_ping_pong.py
```python
from machine import UART
import pinno as P
import time
import json

# UART 초기화
uart1 = UART(1, baudrate=9600, tx=P.TX, rx=P.RX, timeout=10)
uart2 = UART(2, baudrate=9600, tx=P.R5, rx=P.R6, timeout=10)

def main():
    # 초기 데이터 전송
    data = {'ser': 1}
    uart1.write(json.dumps(data) + '\n')  # 데이터를 JSON 문자열로 전송
    print(f"UART1 sent: {data}")

    while True:
        # UART2에서 데이터 수신 및 처리
        if uart2.any():  # UART2에 수신된 데이터가 있으면
            received = uart2.readline()  # 데이터를 줄 단위로 읽기
            try:
                received_data = json.loads(received.decode().strip())  # JSON 디코드
                print(f"UART2 received: {received_data}")

                # ser 값 증가 및 출력
                received_data['ser'] += 1
                print(f"UART2 sending: {received_data}")

                # 5초 대기 후 UART1로 전송
                time.sleep(5)
                uart2.write(json.dumps(received_data) + '\n')
            except Exception as e:
                print(f"Error processing UART2 data: {e}")

        # UART1에서 데이터 수신 및 처리
        if uart1.any():  # UART1에 수신된 데이터가 있으면
            received = uart1.readline()  # 데이터를 줄 단위로 읽기
            try:
                received_data = json.loads(received.decode().strip())  # JSON 디코드
                print(f"UART1 received: {received_data}")

                # ser 값 증가 및 출력
                received_data['ser'] += 1
                print(f"UART1 sending: {received_data}")

                # 5초 대기 후 UART2로 전송
                time.sleep(5)
                uart1.write(json.dumps(received_data) + '\n')
            except Exception as e:
                print(f"Error processing UART1 data: {e}")

if __name__ == "__main__":
    main()
```