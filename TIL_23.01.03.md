# String Formating
- 문자열에 변수를 활용해 작성.
    - %-formatting
        ```python
        name = 'Kim'
        score = 4.5
        print('Hello, %s' % name)
        print('내 성적은 %d' % score)
        print('내 성적은 %f' % score)

        # Hello, Kim
        # 내 성적은 4
        # 내 성적은 4.500000
        ```
    - f-string
        ```python
        name = 'Kim'
        score = 4.5
        print(f'Hello, {name}! 성적은 {score}')
        # Hello, Kim! 성적은 4.5

        pi = 3.141592
        print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}')
        # 원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368
        ```
# 형 변환(Typecasting)
## 암시적 형 변환
- 사용자가 의도하지 않고 파이썬 내부적으로 자료형을 변환
    - bool
    - Numeric type (int, float, complex)
```python
True + 3 # 4
3 + 5.0 # 8.0
3 + 4j + 5 # (8+4j)
```
## 명시적 형 변환
- 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환
    - int: str, float => int
    - float: str, int => float
    - str: int, float, list, tuple, dict => str
```python
int('3') + 4 # 7
float('3.5') + 5 # 8.5
```
# 제어문(Contrl Statement)
## 조건문(Conditional Statement)
### 조건문 기본
- 조건문은 True/False를 판단할 수 있는 조건식과 함께 사용(expression)
    - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭 실행
    - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭 실행
    - else는 선택적으로 활용
```python
if < expression >:
    # Run this Code bolck
else:
    # Run this Code block
 ```

### 복수 조건문
```python
if < expression >:
    # Code bolck
elif < expression >:
    # Code bolck
else:
    # Code block
```

### 중첩 조건문
```python
if < expression >:
    # Code bolck
    if < expression >:
        # Code bolck
else:
    # Code block
```

## 반복문
### 레인지(Range)
> range(n, m, s)
> 
> 숫자의 시퀀스를 나타내기 위해 사용
- 기본형: range(n)
    - 0 ~ n-1까지 숫자 시퀀스
- 범위 지정: range(n, m)
    - n ~ m-1까지 숫자 시퀀스
- 범위 및 스탭 지정: range(n, m, s)
    - n ~ m-1까지 s 스탭 숫자 시퀀스
- 변경불가(immutable), 반복 가능(iterable)
- 예시
```python
list(range(3)) # [0, 1, 2]
list(range(1, 5)) # [1, 2, 3, 4]
list(range(1, 5, 2)) # [1, 3]
# 역순
list(range(6, 1, -1)) # [6, 5, 4, 3, 2]
# []
list(range(6, 1, 1))
```
### for문
> 반복가능한 객체를 모두 순회하면 종료 (별도의 종료조건 X)
- 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)(set, dictionary 등)의 요소를 모두 순회.
```python
for <변수명> in <iterable>:
    # Code block
```

### 반복문 제어
- break: 반복문 종료
- continue: continue 이후 코드블록 수행X, 다음 요소 수행.
- for-else: 끝까지 반복문을 실행한 이후 else문 실행
    - break를 통해 중간에 종료된다면 else 실행X
