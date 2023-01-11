# 사용자 정의 클래스
## 객체 지향 프로그래밍
### 객체(object) 특징
- 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한지
- 속성(attribute): 어떤 상태(데이터)를 갖는지
- 조작법(method): 어떤 행위(함수)를 할 수 있는지
### 객체 지향 프로그래밍
- 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍
- 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 사용.
- 프로그래밍을 더 배우기 쉽게 하고 개발 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점이 있다.

## 클래스와 인스턴스
### 기본 문법
```python
class MyClass:
    pass
my_instance = MyClass() # 인스턴스 생성
my_instance.my_method() # 매서드 호출
my_instance.my_attribute    # 속성
```
### 클래스, 인스턴스
> 클래스는 타입을 새로 만드는 것. 인스턴스는 그 타입의 객체(실체/사례)
```python
class Person:
    pass

print(type(Person)) # type      -> 타입이라는 타입
p1 = Person() 
print(type(p1))     # __main__.Person   -> Person타입
isinstance(person1, Person) # True      -> Person의 인스턴스
```
### 속성
- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터
```python
class Person:
    def __init__(self, name):   # init은 객체가 생성될때 바로 작동하는 method
        self.name = name        # 인스턴스 변수 정의

personal = Person('지민')   # init이 있는 클래스에는 필요한 값을 넣으면서 생성
print(personal.name)        # 인스턴스 변수 접근, 지민
```

### 메서드
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
```python
class Person:
    def talk(self):
        print('안녕')
    
    def eat(self, food):
        print(f'{food}를 냠냠')

personal = Person()
print(personal.talk())      # 안녕
print(personal.eat('피자')) # 피자를 냠냠
print(personal.eat('치킨')) # 치킨을 냠냠
```

### 객체 배교
- ==
    - 동등한(eaual)
    - 변수가 참조하는 객체가 내용이 같은 경우 True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 참조하는지는 모른다.
- is
    - 동일한(identical)
    - 두 변수가 동일한 객체를 참조하면 True
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b)       # True False

b = a
print(a == b, a is b)       # True True
```

## 인스턴스
### 인스턴스 변수
> 인스턴스가 개별적으로 갖고있는 속성(attribute)
>
> 각 인스턴스들의 고유한 변수
- 생성자 메소스(init)에서 self.<변수>로 정의
- 인스턴스 생성 후 <instance>.<변수>로 접근/할당
```python
class Person:
    def __init__(self, name):   # init은 객체가 생성될때 바로 작동하는 생성자 method
        self.name = name        # 인스턴스 변수 정의
    
    def __del__(self):          # 소멸자 method
        print('인스턴스가 사라졌습니다.')

personal = Person('지민')   # init이 있는 클래스에는 필요한 값을 넣으면서 생성
print(personal.name)        # 인스턴스 변수 접근, 지민
del personal                # 인스턴스가 사라졌습니다.
```

### 인스턴스 메서드
- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
- 클래스 내부에 정의되는 메소드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자신(self)이 전달

### self
- 인스턴스 자기 자신
- 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    - 매개변수 이름으로 self를 첫번째 인자로 정의
    - self라고 안해도 되지만, 암묵적인 규칙

### 생성자(constructor) 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
- 인스턴스 변수들의 초기값을 설정
    - 인스턴스 생성
    - __init__메소드 자동 호출

### 소멸자(destructor) 메서드
- 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

### 매직 메서드
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드, 매직 메서드로 불림.
- 특정 상황에 자동으로 불리는 메서드
- ex)
    ```python
     #__str__(self), __len__(self), __repr__(self)
     # __lt__(self, other), __le__(self, other), __eq__(self, other)
     # __gt__(self, other), __ge__(self, other), __ne__(self, other)
     ```
     - str: 해당 객체의 출력 형태를 지정
        - 인스턴스를 그대로 프린트하게 될때 str의 return값 출력
    - gt: 부등호 연산자(>, greater than)
```python
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
    
    def __str__(self):
        return f'[원] radius: {self.r}'
    
    def __gt__(self, other):
        return self.r > other.r

c1 = Circle(10)
c2 = Circle(1)

print(c1)           # [원] radius: 10
print(c2)           # [원] radius: 1
print(c1 > c2)      # True
print(c1 < c2)      # False
```