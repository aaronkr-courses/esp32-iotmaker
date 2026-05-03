## AI 프롬프트 활용 9-6: 마이크로파이썬의 구문 'try: except KeyError:'에 대한 예제
## 프롬프트 
file: 활용-9-6-마이크로파이썬의 구문 try- except KeyError-에 대한 예제.md
```
마이크로파이썬의 구문 ‘try: except KeyError:’에 대한 예제를 만들고 설명해 줘.
```
## AI가 만든 결과
MicroPython에서 `try: except KeyError:` 구문은 **딕셔너리(Dictionary)**에서 존재하지 않는 키를 접근하려고 할 때 발생하는 `KeyError`를 처리하는 전형적인 패턴입니다. 예를 들어 다음과 같은 예제를 살펴볼 수 있습니다:

```python
# 딕셔너리 예시
person_info = {
    "name": "Alice",
    "age": 30
}

try:
    # 존재하지 않는 키인 'hobbies'를 접근
    print("Hobbies:", person_info["hobbies"])
except KeyError:
    # 만약 'hobbies' 키가 없으면 KeyError가 발생
    print("해당 키가 존재하지 않습니다.")
```

---

## 동작 방식 설명

1. **딕셔너리 접근**  
   - `person_info["hobbies"]` 같이 딕셔너리에서 존재하지 않는 키를 사용해 값을 가져오려고 하면, Python(또는 MicroPython)은 `KeyError` 예외를 발생시킵니다.

2. **`try:` 블록에서 예외 처리 감싸기**  
   - `person_info`에서 키를 조회하는 부분을 `try:`로 감싸, 예외가 발생해도 프로그램이 중단되지 않도록 합니다.

3. **`except KeyError:`**  
   - 딕셔너리에서 해당 키가 없는 경우에 발생하는 `KeyError`를 잡아 처리합니다.
   - 키가 존재하지 않을 때 실행될 로직(예: 키가 없다는 안내 메시지)을 작성해두면, 예외 상황에서도 프로그램이 정상적으로 진행될 수 있습니다.

이와 같이 `try: except KeyError:` 구문을 사용하면, **존재하지 않는 키를 조회했을 때** 프로그램이 중단되지 않도록 안전하게 예외를 처리할 수 있습니다. 임베디드 환경(MicroPython)에서도 일반 Python과 동일한 방식으로 예외 처리를 적용할 수 있습니다.