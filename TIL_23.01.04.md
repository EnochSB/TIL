# 반복문2 & 함수
## 반복문
### while문
- while문은 조건식이 참인 경우 반복적으로 코드 실행.
- 코드블럭 실행 이후 조건식을 다시 검사하고 코드 실행.
- while문은 무한 루프를 하지 않게 **종료조건**이 반드시 필요.
```python
while <expression>:
    # Code Block
```

## 함수
> Abstraction: 복잡한 내용은 숨기고, 기능에 집중해 사용.(추상화)

### 함수 기초
- 함수: 특정한 기능을 하는 코드의 조각(묶음)
- 함수도 function이란 타입을 갖고 있다.
- 함수 기본 구조
    - 선언 호출(define & call)
    - 입력(Input)
    - 범위(Scope)
    - 결과값(Output)
    ![function](/23.01.04/function_diagram.png)

### [내장 함수](https://docs.python.org/ko/3/library/functions.html)
#### 자주 사용하는 함수
- len(s)
    - 객체의 길이를 반환. 인자: 시퀀스/컬렉션
- sum(iterable, start=0)
    - start 및 iterable의 항목들을 왼쪽에서 오른쪽으로 합하고 합계를 반환.
    - iterable의 항목은 일반적으로 숫자. 시작값은 문자열이 될 수 없다.
- max(iterable)
    - iterable에서 가장 큰 항목이나 두 개 이상의 인자 중 가장 큰 것을 반환.
    - 여러 항목이 해당되면 처음 만난 항목을 반환
- min(iterable)
    - iterable에서 가장 작은 항목이나 두 개 이상의 인자 중 가장 작은 것을 반환.
    - 여러 항목이 해당되면 처음 만난 항목을 반환
#### 계산 관련 함수
- abs(x)
    - 숫자의 절댓값을 반환. 인자: 정수, 실수 또는 __abs__()를 구현하는 객체.
    - 인자가 복소수라면 그 크기를 반환.
- divmod(a, b)
    - 두 수를 받아 몫과 나머지를 반환.
- pow(base, exp, mod=None)
    - base의 exp 거듭제곱을 반환.
    - mod가 있는 경우, base의 exp 거듭제곱의 모듈로 mod를 반환.
- round(number, ndigit=None)
    - number를 소수점 다음에 ndigits 정밀도로 반올림한 값을 반환.
    - ndigits가 생략되거나 None이면, 입력에 가장 가까운 정수를 반환.
#### 논리 관련 함수
- all(iterable)
    - iterable의 모든 요소가 참이면(또는 iterable이 비어있으면) True를 반환.
- any(iterable)
    - iterable의 요소 중 어느 하나라도 참이면 True를 반환.
    - iterable이 비어있으면 False.
#### 기타
- bin(x)
    - 정수를 "0b'접두사가 붙은 이진 문자열로 반환.
- hex(x)
    - 정수를 "0x"접두사가 붙은 16진수 문자열로 반환.
- oct(x)
    - 정수를 "0o"접두사가 붙은 8진수 문자열로 반환.
- ord(c)
    - 유니코드 문자 c에 대응되는 유니코드 숫자를 반환.
- chr(i)
    - 정수 i에 대응되는 유니코드 문자를 반환.
#### map
- map(function, iterable)
    - iterable의 모든 요소에 function을 적용하고, 그 결과를 map object로 반환.
    ```python
    numbers = [1, 2, 3]
    result = map(str, numbers)
    print(result, type(result))
    # <map object at 0x10e2ca100> <class 'map'>
    ```
    - 알고리즘 문제 풀이 시 input 값들을 숫자로 바로 활용하고 싶을 때
    ```python
    n, m = map(int, input().split()) # 3 5
    print(n, m)
    print(type(n), type(m))
    # 3 5
    # <class 'int'> <class 'int'>
    ```
