## AI 프롬프트 활용 9-8: 마이크로파이썬의 구문 'try: except KeyBoardInterrupt:'에 대한 예제
## 프롬프트 
file: 활용-9-8-마이크로파이썬의 구문 try- except KeyBoardInterrupt-에 대한 예제.md
```
마이크로파이썬의 구문 ‘try: except KeyBoardInterrupt:’에 대한 예제를 만들고 설명해 줘.
```
## AI가 만든 결과
MicroPython에서 `try: except KeyboardInterrupt:` 구문은 사용자가 **Ctrl + C**를 눌렀을 때 발생하는 `KeyboardInterrupt` 예외를 처리하는 데 쓰입니다. 다만 모든 MicroPython 포트(플랫폼)에서 동일하게 작동하는 것은 아니고, 실행 환경에 따라 차이가 있을 수 있습니다. 일반적으로 PC 시리얼 REPL이나 일부 개발 보드에서는 아래 예시처럼 동작합니다.

다음 예시는 무한 루프를 돌다가 사용자가 **Ctrl + C**를 눌러 인터럽트(중단)할 때, `KeyboardInterrupt` 예외를 잡아서 처리하는 코드입니다.

```python
try:
    print("무한 루프를 시작합니다. Ctrl + C를 눌러 중단해 보세요.")
    while True:
        pass  # 여기서는 단순히 시간을 소비하는 용도로 pass
except KeyboardInterrupt:
    print("Ctrl + C를 통해 무한 루프가 중단되었습니다.")
```

---

## 동작 방식 설명

1. **무한 루프(`while True:`)**  
   - `while True:` 구문은 조건 없이 계속 반복하므로, 사용자가 멈추지 않는 이상 무한정 실행됩니다.

2. **Ctrl + C 입력**  
   - 터미널이나 시리얼 REPL 상에서 실행 중이라면, 사용자가 **Ctrl + C**를 누르면 `KeyboardInterrupt` 예외가 발생합니다.

3. **`try:` 블록**  
   - 무한 루프 전체를 `try:` 블록으로 감싸 놓으면, `KeyboardInterrupt`가 발생했을 때 프로그램이 바로 종료되지 않고 `except KeyboardInterrupt:` 블록으로 제어가 넘어갑니다.

4. **`except KeyboardInterrupt:`**  
   - 예외가 발생하면 이 블록이 실행되고, 사용자에게 루프가 중단되었음을 알리는 메시지를 출력합니다.  
   - 이후 프로그램은 정상적으로 종료되거나, 다음 로직을 계속 진행할 수 있습니다.

이렇게 `try: except KeyboardInterrupt:` 패턴을 사용하면, **사용자가 의도적으로 Ctrl + C를 눌러 작업을 중단했을 때** 프로그램이 갑작스럽게 멈추는 대신, 원하는 종료 루틴(자원 정리, 상태 저장 등)을 안전하게 수행할 수 있습니다.