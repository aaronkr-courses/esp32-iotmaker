## AI 프롬프트 활용 3-9: 
#### 마이크로파이썬에서 int 자료형으로 변환하는 프로그램
```
마이크로파이썬에서 다른 자료형을 int 자료형으로 변환하는 프로그램을 만들고, 코드를 단계별로 설명해 줘.
```
## AI가 만든 결과
아래 예시는 마이크로파이썬(MicroPython) 환경에서 문자열, 실수(float), 불리언(boolean) 등의 다른 자료형을 int 자료형으로 변환하는 간단한 예제 코드입니다. 각 단계별로 코드를 해석해 보겠습니다.

---

## 전체 코드

```python
# 자료형 변환 예제 (MicroPython)

# 1. 문자열(String)을 int로 변환
value_str = "123"
int_from_str = int(value_str)

# 2. 실수(Float)를 int로 변환
value_float = 3.14
int_from_float = int(value_float)

# 3. 불리언(Boolean)을 int로 변환
value_bool = True
int_from_bool = int(value_bool)

# 4. 변환 결과 출력
print("int_from_str:", int_from_str)
print("int_from_float:", int_from_float)
print("int_from_bool:", int_from_bool)
```

---

## 코드 단계별 설명

1. **주석 달기(`#`)**  
   \- 코드의 각 부분이 어떤 일을 하는지 보기 좋게 설명을 달아줍니다.  
   \- 마이크로파이썬에서는 일반 파이썬과 동일하게 `#` 뒤로 적는 내용이 주석이 됩니다.

2. **문자열(String)을 int로 변환하기**  
   ```python
   value_str = "123"
   int_from_str = int(value_str)
   ```
   \- `value_str` 변수에 문자열 `"123"`을 저장합니다.  
   \- `int(value_str)` 함수는 문자열 형태의 숫자를 정수(int)로 변환합니다.  
   \- `"123"`은 숫자로 바꾸기 적합한 형태이므로 정상적으로 `123`(정수)으로 변환됩니다.

3. **실수(Float)를 int로 변환하기**  
   ```python
   value_float = 3.14
   int_from_float = int(value_float)
   ```
   \- `value_float` 변수에 `3.14` 값을 저장합니다.  
   \- `int(value_float)` 함수는 소수점 이하를 잘라내어 정수 부분만 가져옵니다.  
   \- `3.14` → `3`으로 변환됩니다(소수점 이하 버림).

4. **불리언(Boolean)을 int로 변환하기**  
   ```python
   value_bool = True
   int_from_bool = int(value_bool)
   ```
   \- `value_bool` 변수에 `True` 값을 저장합니다.  
   \- 파이썬에서 `True`는 1로, `False`는 0으로 매핑됩니다.  
   \- 따라서 `True`를 정수로 변환하면 `1`이 됩니다.

5. **변환 결과 출력하기**  
   ```python
   print("int_from_str:", int_from_str)
   print("int_from_float:", int_from_float)
   print("int_from_bool:", int_from_bool)
   ```
   \- 각 변수에 담긴 변환 결과를 출력합니다.  
   \- 변환된 값들을 한눈에 확인할 수 있습니다.  

6. **에러 처리(참고)**  
   \- 만약 `"abc"`처럼 숫자가 아닌 문자열을 `int()` 함수로 변환하려고 하면 `ValueError`가 발생합니다.  
   \- 필요하다면 `try` / `except` 구문을 사용하여 예외를 처리할 수 있습니다.
   ```python
   try:
       invalid_str = "abc"
       int_from_invalid = int(invalid_str)
   except ValueError:
       print("문자열을 정수로 변환할 수 없습니다.")
   ```

---

## 요약

- **`int()` 함수**를 사용해 문자열, 실수, 불리언 등 다른 자료형을 정수형으로 변환할 수 있습니다.  
- 문자열을 변환할 때는 숫자로 이루어진 문자열이어야 합니다.  
- 실수를 변환할 때는 소수점 이하가 버려집니다(내림).  
- 불리언을 변환할 때는 `True` → 1, `False` → 0 이 됩니다.  
- 변환이 불가능한 문자열인 경우에는 예외(`ValueError`)가 발생하니 주의해야 합니다.

이 과정을 통해 마이크로파이썬에서도 일반 파이썬과 동일하게 `int()` 함수를 사용하여 다른 자료형을 정수로 변환할 수 있습니다.