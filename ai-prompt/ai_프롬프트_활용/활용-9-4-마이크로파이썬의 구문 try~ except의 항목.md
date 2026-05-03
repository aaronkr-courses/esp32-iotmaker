## AI 프롬프트 활용 9-4: 마이크로파이썬의 구문 try~ except 항목에서 발생할 수 있는 항목
## 프롬프트 
file: 활용-9-4-마이크로파이썬의 구문 try~ except의 항목.md
```
마이크로파이썬의 구문 'try: except 항목:'에서 발생할 수 있는 항목을 모두 나열해 줘.
```
## AI가 만든 결과
MicroPython은 기본적으로 “표준 Python”의 예외 클래스 중 상당수를 지원하며, 여기에 일부 예외는 빠져 있거나(임베디드 환경 때문에) 혹은 축소된 형태로 제공됩니다. 하지만 일반적으로 아래와 같은 **내장 예외(Built-in Exceptions)** 들을 `except` 뒤에 지정하여 처리할 수 있습니다. (MicroPython 버전이나 포트별로 지원 여부가 달라질 수 있으니, 실제 사용 환경의 문서를 확인하시는 것이 가장 정확합니다.)

아래는 MicroPython이 제공하는 대표적인 **예외 클래스**들을 정리한 목록입니다.

---

## 1. 최상위 예외 계층 구조

- **BaseException**  
  모든 예외의 최상위 클래스입니다. 일반적으로 직접 사용하기보다는, 하위 예외를 구체적으로 명시해서 사용합니다.

- **SystemExit**  
  스크립트나 프로그램의 종료를 나타내는 예외입니다.

- **KeyboardInterrupt**  
  사용자가 키보드에서 `Ctrl + C`를 눌렀을 때 발생합니다.  
  (단, 포트·환경에 따라 지원 여부가 달라질 수 있습니다.)

- **Exception**  
  BaseException에서 파생된 일반적인 예외의 최상위 클래스입니다.  
  보통 `except Exception:` 으로 묶으면 하위 모든 일반 예외를 처리할 수 있습니다.

---

## 2. 일반 예외 클래스

다음은 `Exception`을 상속받는 일반적인 예외들입니다.

1. **ArithmeticError**  
   - 산술 연산 관련 최상위 예외 클래스입니다.  
   - `OverflowError`, `ZeroDivisionError` 등을 포함합니다.

2. **FloatingPointError**  
   - 부동소수점 연산에서 에러가 발생했을 때(일반적인 Python에서는 잘 사용되지 않으며,  
     MicroPython에서도 실제로 거의 발생하지 않을 수 있습니다.)

3. **OverflowError**  
   - 수의 범위를 넘어서는 연산(예: 너무 큰 정수 연산) 등에서 발생할 수 있습니다.

4. **ZeroDivisionError**  
   - 0으로 나누려고 할 때 발생합니다.

5. **AssertionError**  
   - `assert` 문이 실패했을 때 발생합니다.

6. **AttributeError**  
   - 객체에 없는 속성(메서드나 변수)을 참조하려고 할 때 발생합니다.

7. **EOFError**  
   - 파일이나 입력 스트림에서 더 이상 읽을 데이터가 없을 때 발생합니다.

8. **ImportError**  
   - `import` 구문에서 모듈을 불러올 수 없을 때 발생합니다.

9. **LookupError**  
   - “탐색” 계열(시퀀스, 맵 등) 오류의 최상위 예외입니다.
     - `IndexError`, `KeyError` 등이 포함됩니다.

   - **IndexError**  
     리스트, 튜플 등 시퀀스에서 범위를 벗어난 인덱스를 참조할 때 발생합니다.  
   - **KeyError**  
     딕셔너리에서 존재하지 않는 키를 참조할 때 발생합니다.

10. **MemoryError**  
    - 메모리가 부족할 때 발생합니다(임베디드 환경에서 가끔 보게 됩니다).

11. **NameError**  
    - 존재하지 않는 변수나 함수를 참조할 때 발생합니다.
      - **UnboundLocalError**: 지역 변수 범위 문제로 인한 예외(내부적으로 `NameError`를 상속).

12. **OSError**  
    - OS 관련 에러(파일·디렉터리 접근, 소켓·네트워크 오류, 디바이스 I/O 등) 시 발생합니다.  
    - MicroPython에서 꽤 자주 보이는 예외로, 파일 시스템이나 네트워크 함수 등에서 많이 발생합니다.

13. **SyntaxError**  
    - 구문이 잘못되어 파이썬 코드로 해석할 수 없을 때 발생합니다.
      - **IndentationError**: 들여쓰기가 잘못되었을 때  
      - **TabError**: 공백과 탭을 혼합해서 들여쓰기할 때

14. **SystemError**  
    - 파이썬 인터프리터 내부에서 무엇인가 잘못된 경우 발생할 수 있습니다(자주 보진 않음).

15. **TypeError**  
    - 지원되지 않는 타입 연산(예: 정수와 문자열을 + 연산으로 더하려고 시도) 시 발생합니다.

16. **ValueError**  
    - 연산이나 함수에 전달된 값이 기대하는 범위·형식과 다를 때 발생합니다.

17. **StopIteration**  
    - 이터레이터(예: for 루프)에서 반복이 끝났음을 나타내기 위해 발생합니다.  
      (일반적으로 사용자 코드에서 직접 except로 잡는 일은 드뭅니다.)

18. **GeneratorExit**  
    - 제너레이터가 종료될 때 내부적으로 발생할 수 있습니다. (역시 직접 잡는 경우는 드물 수 있음)

19. **NotImplementedError**  
    - 아직 구현되지 않은 메서드를 호출했을 때 발생합니다.  
    - MicroPython에서도 일부 함수가 구현되지 않았을 경우 이 예외를 발생시킬 수 있습니다.

---

## 3. 사용자 정의 예외

- 물론 **사용자 정의 클래스**(예: `class MyError(Exception): ...`) 도 직접 만들어 `except MyError:` 식으로 처리할 수 있습니다.
- 임베디드 환경에서는 메모리 사용을 최소화하기 위해, 너무 많은 예외 클래스를 만들진 않는 편입니다.

---

## 4. 정리

정리하면, MicroPython의 `try:` `except 항목:` 구문에서 `항목`으로 지정할 수 있는 대표적인 **빌트인 예외 클래스**들은 다음과 같습니다(버전에 따라 일부가 제외되었거나 추가될 수 있음).

- **BaseException**
- **SystemExit**
- **KeyboardInterrupt**
- **Exception**
- **StopIteration**
- **GeneratorExit**
- **ArithmeticError**
  - FloatingPointError  
  - OverflowError  
  - ZeroDivisionError  
- **AssertionError**
- **AttributeError**
- **EOFError**
- **ImportError**
- **LookupError**
  - IndexError  
  - KeyError  
- **MemoryError**
- **NameError**
  - UnboundLocalError  
- **OSError**
- **SyntaxError**
  - IndentationError  
  - TabError  
- **SystemError**
- **TypeError**
- **ValueError**
- **NotImplementedError**

추가로:

- **사용자 정의 예외 클래스**(예: `class MyError(Exception)`)  
  → `except MyError:` 로 처리

위 예외 유형들은 표준 Python 3와 매우 유사하지만, **MicroPython 포트별로 차이가 있을 수 있으니**(어떤 예외가 빠져 있거나, 추가된 전용 예외가 있을 수도 있음) 실제 동작 환경(펌웨어 버전, 포트)에서 지원되는 예외 목록을 확인하는 것이 좋습니다.