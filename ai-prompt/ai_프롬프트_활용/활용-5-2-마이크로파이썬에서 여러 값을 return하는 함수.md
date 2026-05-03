## AI 프롬프트 활용 5-2: 마이크로파이썬에서 여러 값을 return하는 함수
## 프롬프트 
```
마이크로파이썬에서 여러 값을 return하는 함수를 만들고, 코드를 단계별로 설명해 줘.
```
## AI가 만든 결과
아래 예시는 **마이크로파이썬(MicroPython)** 환경에서 함수를 정의할 때, 여러 값을 **한 번에 return**하고 이를 호출부에서 받아오는 간단한 예시입니다.

---

## 예제 코드

```python
# 1. 여러 값을 반환하는 함수를 정의한다.
def arithmetic_operations(x, y):
    add_result = x + y         # 더하기
    sub_result = x - y         # 빼기
    mul_result = x * y         # 곱하기
    div_result = x / y         # 나누기 (나눗셈 예시: 실제로는 y가 0이 아닐 때만 가능)

    # 여러 값을 튜플 형태로 반환
    return add_result, sub_result, mul_result, div_result

# 2. 함수를 호출하고, 반환값을 여러 변수에 각각 받는다.
result_add, result_sub, result_mul, result_div = arithmetic_operations(10, 3)

# 3. 결과를 출력한다.
print("더하기 결과:", result_add)
print("빼기 결과:", result_sub)
print("곱하기 결과:", result_mul)
print("나누기 결과:", result_div)
```

---

## 단계별 설명

1. **함수 정의: `arithmetic_operations(x, y)`**  
   ```python
   def arithmetic_operations(x, y):
       add_result = x + y
       sub_result = x - y
       mul_result = x * y
       div_result = x / y
       return add_result, sub_result, mul_result, div_result
   ```  
   - 파라미터(매개변수)로 `x`, `y` 두 개의 숫자를 받고, 네 가지 연산 결과를 구합니다.  
   - `return` 문에서 반환값을 쉼표로 구분하면, **튜플(tuple)** 형태로 여러 값을 한 번에 반환합니다.  
   - 반환 결과는 `(add_result, sub_result, mul_result, div_result)`가 됩니다.

2. **함수를 호출하고, 반환값을 여러 변수에 각각 받기**  
   ```python
   result_add, result_sub, result_mul, result_div = arithmetic_operations(10, 3)
   ```  
   - 함수를 호출하면 `(더하기 결과, 빼기 결과, 곱하기 결과, 나누기 결과)`를 튜플로 돌려받습니다.  
   - `result_add`, `result_sub`, `result_mul`, `result_div` 변수에 **언패킹(unpacking)**으로 각각의 값이 들어갑니다.

3. **결과 출력**  
   ```python
   print("더하기 결과:", result_add)
   print("빼기 결과:", result_sub)
   print("곱하기 결과:", result_mul)
   print("나누기 결과:", result_div)
   ```  
   - 분리된 각 결과 변수를 `print()`로 출력합니다.  
   - 예: `더하기 결과: 13`, `빼기 결과: 7`, `곱하기 결과: 30`, `나누기 결과: 3.3333...`

---

### 요약

- 마이크로파이썬에서 **여러 값을 반환**하려면, `return` 문에 여러 값을 쉼표로 구분해 적습니다. 사실상 **튜플** 형태로 묶여 반환됩니다.  
- 함수 호출 시에는 “언패킹” 기법을 사용해 각각의 반환값을 **여러 변수**에 쉽게 할당할 수 있습니다.  
- 이 기법은 일반 파이썬(CPython)과 동일하게 동작하며, 임베디드 환경에서도 편리하게 사용할 수 있습니다.