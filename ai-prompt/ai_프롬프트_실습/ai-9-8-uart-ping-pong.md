다음의 조건에 따라 마이크로파이썬 프로그램을 만들고 설명해 줘.
- 동일한 개발 보드에 있는 UART1과 UART2를 서로 연결할거야. 
  import pinno as P 
  uart1 = UART(1, baudrate=9600, tx=P.TX, rx=P.RX, timeout=10)
  uart2 = UART(2, baudrate=9600, tx=P.R5, rx=P.R6, timeout=10)
- UART1에서 UART2로 {'ser':1}을 데이터로 보내면,
  UART2에서는 5초를 기다렸다가 ser에 1을 더하여 {'ser':2}를 UART1으로 돌려 보내게 돼.
- UART1에도 5초를 기다렸다가 받은 데이터 ser에 1을 더하여 {'ser':3}를 UART2으로 보내는 행위를 무한 반복하는 거야.
- 각 단계에서 UART의 이름과 받은 ser을 출력하고, 보낼 때도 이름과 ser을 출력하면 돼.