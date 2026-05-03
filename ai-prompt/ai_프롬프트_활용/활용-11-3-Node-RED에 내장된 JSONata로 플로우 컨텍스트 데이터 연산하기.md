## AI 프롬프트 활용 11-3: Node-RED에 내장된 JSONata로 플로우 컨텍스트 데이터 연산하기
## 프롬프트 
file: 활용-11-3-Node-RED에 내장된 JSONata로 플로우 컨텍스트 데이터 연산하기.md
```
Node-RED의 change 노드에서 JSONata를 사용할거야. flow.value를 숫자로 바꾸어서 1을 더하는 구문
을 만들어 줘.
```
## AI가 만든 결과
Node-RED의 Change 노드에서 JSONata 표현식을 통해 **flow.value**를 숫자로 변환한 뒤 1을 더하려면, 아래와 같은 식을 사용하면 됩니다.

```jsonata
$number($flowContext("value")) + 1
```

### 사용 예시

1. **Change 노드**를 추가하고, ‘Set’ 액션을 선택합니다.
2. **Property**를 `flow.value`로 지정하고, **To**를 `Expression`(JSONata)로 설정합니다.
3. 위의 JSONata 식을 입력합니다:
   ```jsonata
   $number($flowContext("value")) + 1
   ```
4. Change 노드가 실행될 때마다, 원래 `flow.value`가 문자열이든 숫자든 상관없이, 우선 숫자 변환 후(`$number(...)`)에 1을 더해 다시 `flow.value`에 저장하게 됩니다.

> **참고**  
> Node-RED에서 **flow/context** 변수는 JSONata에서 직접 참조할 수 없고, `$flowContext("...")`, `$globalContext("...")` 같은 함수를 통해 가져와야 합니다.  
> - `$number(...)`는 문자열이 숫자 형태를 띌 경우 이를 **숫자형**으로 변환해 줍니다. 만약 변환이 불가능한 문자열이라면 `null`이 반환될 수 있습니다.