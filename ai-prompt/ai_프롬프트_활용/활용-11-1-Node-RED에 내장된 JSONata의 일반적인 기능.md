## AI 프롬프트 활용 11-1: Node-RED에 내장된 JSONata의 일반적인 기능
## 프롬프트 
file: 활용-11-1-Node-RED에 내장된 JSONata의 일반적인 기능.md
```
Node-RED에 내장된 JSONata의 일반적인 기능에 대해 알려줘.
```
## AI가 만든 결과
**JSONata**는 Node-RED의 *Change 노드* 등에서 JSON 데이터를 쉽고 유연하게 조작하기 위해 사용하는 **쿼리 및 변환 언어**입니다. Node-RED에 내장되어 있으며, JSON 구조의 데이터를 대상으로 **필터링, 변환, 매핑, 계산** 등의 작업을 간편하게 수행할 수 있습니다. 아래는 JSONata의 주요 기능과 특징에 대한 간략한 설명입니다.

---

## 1. 경로 표현(Path Expressions)
JSONata의 가장 기본적인 기능은 **경로(Path)**를 통해 JSON 데이터 내부의 특정 필드나 값을 **선택**하는 것입니다.

```json
{
  "person": {
    "name": "Alice",
    "age": 30,
    "skills": ["JS", "Node-RED", "JSONata"]
  }
}
```
예를 들어, 위 JSON에서 `person.name`을 가져오려면 JSONata 식으로 simply `person.name`이라고 쓰면 됩니다.  
- `person.skills[1]` → `"Node-RED"`  
- `person.skills[0..1]` → `["JS", "Node-RED"]`  

---

## 2. 필터(조건) 연산
배열이나 객체를 대상으로 조건을 지정하여 특정 요소만 골라낼 수 있습니다. 예를 들어, 배열의 각 요소에 대해 조건을 주고, 통과하는 요소만 뽑아낼 수 있습니다.

```json
{
  "users": [
    { "name": "Alice", "age": 30 },
    { "name": "Bob",   "age": 25 },
    { "name": "Carol", "age": 35 }
  ]
}
```

- `users[age >= 30]` → `[ { "name": "Alice", "age": 30 }, { "name": "Carol", "age": 35 } ]`  

이처럼 **중괄호 안에 조건식을** 넣으면, 해당 배열 요소들 중 조건에 부합하는 값들만 필터링됩니다.

---

## 3. 맵/리듀스 등 고차 함수(Higher-Order Functions)
JSONata는 배열에 대한 **함수형 연산**을 지원합니다.  
- **`$.map(...)`**, **`$.filter(...)`**, **`$.reduce(...)`**와 같은 함수를 제공하며, 각각 ECMAScript의 map, filter, reduce와 유사하게 작동합니다.
  
예를 들어, 나이(age)의 평균값을 구한다면:

```jsonata
$reduce(users, function($acc, $current) {
    $acc + $current.age
}, 0) / count(users)
```

- `users` 배열의 모든 `age` 값을 누적(`$acc`)하여 더하고(`$current.age`), 마지막에 총 사용자 수로 나누어 평균을 구하는 예시입니다.

---

## 4. 연산자와 함수
문자열, 숫자, 논리 연산 등을 위해 다양한 **연산자**와 **내장 함수**들을 지원합니다.

1. **산술 연산자**: `+`, `-`, `*`, `/`, `%`
2. **비교 연산자**: `=`, `!=`, `<`, `<=`, `>`, `>=`
3. **논리 연산자**: `and`, `or`, `not`
4. **문자열 함수**: `$substring()`, `$length()`, `$contains()`, `$replace()`, `$lowercase()`, `$uppercase()` 등
5. **날짜/시간 함수**: `$now()`, `$millis()`, `$fromMillis()`, `$toMillis()`, `$moment()`, (Node-RED 특정 환경에서 사용 가능)  
6. **배열/객체 관련 함수**: `$each()`, `$map()`, `$filter()`, `$reduce()`, `$keys()`, `$lookup()`, 등

이를 조합하면 복잡한 데이터 변환 로직도 간결한 스크립트로 표현할 수 있습니다.

---

## 5. 조건문(Conditional)과 삼항 연산
JSONata에서는 `if ... then ... else` 문법이나, **삼항(ternary) 연산자** 스타일의 표현식을 통해 조건 로직을 구성할 수 있습니다.

```jsonata
(
  if (person.age >= 30) then
    "장년"
  else
    "청년"
)
```
또는
```jsonata
person.age >= 30 ? "장년" : "청년"
```
처럼 작성할 수도 있습니다.

---

## 6. 사용자 정의 함수
복잡한 로직을 반복해서 사용할 때는, JSONata 식 내부에서 **사용자 정의 함수**를 정의할 수 있습니다.

```jsonata
(
  $isSenior := function($age) {
      $age >= 65
  };
  users[$isSenior(age)]
)
```
- `$isSenior`라는 함수를 정의하고, `users` 배열 중 `age >= 65` 조건을 만족하는 사용자들만 필터링합니다.

---

## 7. 정규식(Regular Expression)
문자열 검색, 치환 등을 위해 **정규 표현식(Regex)**도 사용할 수 있습니다( `$replace()` 함수와 함께). 예:

```jsonata
$replace("Hello 123 World", /\d+/, "Numbers")
```
- `\d+` (숫자 연속)을 `"Numbers"`로 치환 → `"Hello Numbers World"`

---

## 8. Node-RED에서의 활용
Node-RED에서는 주로 **Change 노드**의 'Set' 액션에서 'Use JSONata expression'을 선택하여 아래와 같이 스크립트를 작성합니다.

1. **메시지(payload) 변환**  
   - `msg.payload` 속의 특정 값을 추출/가공하여 다시 `msg.payload`에 저장
2. **메시지 분기**  
   - `Switch 노드`에서 JSONata 식을 사용해 조건 분류
3. **함수 노드 대체**  
   - 간단한 가공 로직이라면 함수 노드 대신 Change 노드 + JSONata로 처리하면 더 간결할 수 있음

JSONata 식을 사용하면, 복잡한 JavaScript 코드를 작성하지 않고도 직관적으로 JSON 데이터 처리를 할 수 있습니다.

---

## 정리
- **JSONata**는 Node-RED에 **내장된 JSON 변환 및 쿼리 언어**로, 경로 표현, 필터, 함수형 연산, 내장 함수, 사용자 정의 함수 등을 지원합니다.  
- **Node-RED의 Change 노드** 등에서 `Use JSONata expression` 모드를 통해 복잡한 JSON 변환 작업을 **짧고 간결하게** 구현할 수 있습니다.  
- **배열**과 **객체**를 다루는 고급 기능(맵, 필터, 리듀스, 조건문, 함수 정의 등)이 풍부하여, 다양한 변환 로직을 손쉽게 작성할 수 있습니다.

이런 JSONata의 특징을 숙지하면, Node-RED에서 메시지(payload) 처리를 훨씬 유연하게 다룰 수 있게 됩니다.