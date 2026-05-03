## AI 프롬프트 활용 5-4: 마이크로파이썬에서 클래스의 이름을 만들 때 사용하는 Pascal Case
## 프롬프트 
```
마이크로파이썬에서 클래스의 이름(identifier, 식별자)을 만들 때 사용하는 Pascal Case를 설명해 줘.
```
## AI가 만든 결과
Pascal Case(파스칼 케이스)는 **클래스 이름 등 식별자를 작성할 때** 각 단어의 첫 글자를 **대문자로** 쓰고, 단어 사이에 구분 기호(언더스코어 등)를 사용하지 않는 명명 규칙(네이밍 컨벤션)입니다. 예를 들어, 다음과 같은 방식으로 클래스 이름을 지을 때 Pascal Case를 사용합니다.

- `MyClass`
- `TemperatureSensor`
- `MotorController`

즉, **각 단어의 첫 글자를 대문자로** 표기하고, 단어들을 **연결**하여 한 단어처럼 보이게 만드는 방식이며, 이를 “UpperCamelCase”라고 부르기도 합니다.

---

## Python(마이크로파이썬 포함)에서의 사용
일반적으로 Python의 [PEP 8 스타일 가이드](https://peps.python.org/pep-0008/)에서는 **클래스 이름**을 Pascal Case로 작성하도록 권장합니다. 마이크로파이썬(MicroPython)에서도 Python과 같은 코드 스타일을 사용할 수 있기 때문에, 클래스 명은 Pascal Case로 적는 것이 관례적이고 가독성 면에서도 좋습니다. 예:

```python
class TemperatureSensor:
    def __init__(self, pin):
        self.pin = pin

    def read_value(self):
        # 센서 값 읽는 로직
        return 42  # 예시
```

이처럼 **`TemperatureSensor`**라는 클래스명은 각 단어(Temperature, Sensor)의 첫 글자를 모두 대문자로 쓴 **Pascal Case** 형태입니다.

---

## Pascal Case의 특징
1. **각 단어의 첫 글자를 대문자로** 표기한다.
2. **단어들 사이에 밑줄(underscore)이나 공백 없이** 연결한다.
3. 보통 **클래스, 예외 클래스, 열거형** 등의 이름에 사용한다.

이 외에 함수나 변수 이름은 보통 소문자와 밑줄(`snake_case`)을 사용하는 것이 Python 스타일 가이드(PEP 8)의 권장 사항입니다. 

결론적으로, 마이크로파이썬에서도 **클래스 이름**을 정의할 때는 **Pascal Case**를 사용하여, “`MyClass`”, “`MyDeviceDriver`”, “`MotorController`”처럼 작성하는 것이 관례입니다.