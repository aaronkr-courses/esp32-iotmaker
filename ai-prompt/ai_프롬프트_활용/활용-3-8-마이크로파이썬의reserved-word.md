## AI 프롬프트 활용 3-8: 
#### 마이크로파이썬의 reserved word
```
마이크로파이썬의 reserved word를 알려줘.
```
## AI가 만든 결과
MicroPython은 **표준 파이썬(Python 3 계열)** 문법을 상당 부분 공유하기 때문에, 예약어(reserved word)도 대부분 일반 파이썬과 동일합니다. 다만, MicroPython은 Python 버전 3.4~3.5 기반에서 시작되었고 이후 일부 기능(예: `async`, `await`)을 순차적으로 지원해 왔기 때문에, “match”, “case”(Python 3.10의 패턴 매칭) 같은 최신 키워드는 포함되지 않습니다.

아래는 **MicroPython에서 예약어로 취급되는 키워드** 목록입니다. (일반적으로 Python 3.5~3.7 수준과 유사)

---

1. **제어문/흐름 제어 관련**
   - `if`
   - `elif`
   - `else`
   - `while`
   - `for`
   - `break`
   - `continue`
   - `try`
   - `except`
   - `finally`
   - `raise`

2. **함수, 클래스, 모듈 정의**
   - `def`
   - `class`
   - `from`
   - `import`
   - `as`

3. **논리 및 연산자**
   - `and`
   - `or`
   - `not`
   - `in`
   - `is`

4. **값 및 타입**
   - `True`
   - `False`
   - `None`

5. **기타**
   - `assert`
   - `del`
   - `global`
   - `lambda`
   - `nonlocal`
   - `pass`
   - `return`
   - `with`
   - `yield`

6. **비동기(Async I/O) 관련** (지원 버전에서만 사용 가능)
   - `async`
   - `await`

---

## 참고사항

1. **MicroPython 버전에 따라 차이**  
   - 초창기 버전(예: 1.0대)에서는 `async`, `await`가 완전히 예약어가 아니었으나, 최근(1.9 이상) 버전에서는 비동기 I/O를 지원하므로 예약어로 취급됩니다.
   - Python 3.10 이상에서 등장한 `match`, `case` 키워드는 현재 MicroPython에 공식적으로 포함되어 있지 않습니다.

2. **예약어는 식별자로 사용할 수 없음**  
   - 변수, 함수, 클래스 이름 등으로 위 단어들을 사용할 경우 문법 오류(SyntaxError)가 발생합니다.

3. **`keyword` 모듈로 확인 가능**  
   - 일부 MicroPython 펌웨어에는 표준 라이브러리의 `keyword` 모듈이 포함되어 있을 수 있습니다. 만약 `import keyword`가 가능하다면 `keyword.kwlist`로 실제 런타임 환경에서의 예약어 목록을 확인할 수 있습니다.

---

정리하자면, MicroPython의 예약어는 **일반 파이썬(3.4~3.7 기반)과 거의 동일**하며, Python 3.10에 추가된 `match`, `case` 같은 최신 키워드는 포함되지 않는다는 점이 가장 큰 차이입니다. 이 목록을 참고해 변수/함수/클래스 이름을 지을 때 예약어 충돌이 없도록 유의하시면 됩니다.