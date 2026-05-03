## AI 프롬프트 활용 9-7: 마이크로파이썬의 구문 'try: except IndexError:'에 대한 예제
## 프롬프트 
file: 활용-9-7-마이크로파이썬의 구문 try- except IndexError-에 대한 예제.md
```
마이크로파이썬의 구문 ‘try: except IndexError:’에 대한 예제를 만들고 설명해 줘.
```
## AI가 만든 결과
MicroPython에서 `try: except IndexError:` 구문은 **리스트(List)나 튜플(Tuple)**에서 유효하지 않은 인덱스를 사용해 접근하려고 할 때 발생하는 `IndexError`를 처리하는 데 사용됩니다. 아래 예시 코드를 살펴봅시다:

```python
numbers = [10, 20, 30]

try:
    # 유효 범위(0~2)를 벗어난 인덱스 5를 접근
    value = numbers[5]
    print("인덱스 5의 값:", value)
except IndexError:
    # numbers[5]가 유효하지 않으면 IndexError 발생
    print("인덱스 범위를 벗어났습니다.")
```

---

## 동작 방식 설명

1. **리스트 인덱스 접근**  
   - `numbers[5]` 처럼 실제로 존재하지 않는 인덱스를 접근하면, Python(또는 MicroPython)에서 `IndexError` 예외가 발생합니다.

2. **`try:` 블록**  
   - 문제가 발생할 가능성이 있는 리스트 접근 코드를 `try:` 블록으로 감싸, 예외가 발생해도 프로그램이 중단되지 않도록 합니다.

3. **`except IndexError:`**  
   - 리스트(또는 튜플)에서 인덱스 범위를 벗어났을 때 발생하는 `IndexError` 예외를 잡아 처리합니다.
   - 예외 발생 시 안내 메시지를 출력하거나, 다른 로직을 수행하여 프로그램이 정상적으로 진행되도록 만들 수 있습니다.

이처럼 `try: except IndexError:` 구문을 통해 **잘못된 인덱스 접근**으로 인해 프로그램이 강제로 중단되지 않도록 예외를 처리할 수 있습니다. 이는 임베디드 환경(MicroPython)에서도 일반 Python과 동일하게 동작합니다.
