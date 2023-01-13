# 클래스 상속 & 추가문법
## 클래스
### 클래스 메서드
- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용해 정의
    - 데코레이터: 함수를 어떤 함수로 꾸며 새로운 기능 부여
- 호출시 첫 인자로 클래스(cls)가 전달됨
### 스태틱 메서드
- 인스턴스나 클래스를 사용하지 않는 메서드
- @staticmethod 데코레이터
- 호출시 어떠한 인자도 전달되지 않음(클래스/인스턴스 정보에 접근/수정 불가)
```python
class MyClass:
    def method(self):
        return 'instance method', self
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    @staticmethod
    def staticmethod():
        return 'static method'
```
### 이름 공간(namespace)
- 클래스가 정의될 때 클래스와 해당하는 이름 공간 생성
- 인스턴스가 만들어질 때 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면 인스턴스 - 클래스 순으로 탐색

## 상속
### 클래스 상속
- 상속: 두 클래스 사이 부모-자식 관계를 정립하는 것
    - ex. 모든 파이썬 클래스는 object를 상속받음
- 부모에 정의된 속성/메서드를 활용하거나 오버라이딩(재정의)하여 활용
    - 코드의 재사용성 ↑ 클래스 간 계층적 관계 활용
- 상속 관련 함수와 메서드
```python
class ParentClass:
    pass
class ChildClass(ParentClass):
    pass
p1 = ParentClass()
p2 = ChildClass()
# isinstance(object, classinfo)
print(isinstance(p2, ParentClass))      # True, classinfo의 instance거나 subclass인 경우 True
print(isinstance(p2, ChildClass))       # True

# issubclass(class, classinfo)
print(issubclass(ChildClass, ParentClass))                  # True, 클래스가 classinfo의 subclass면 True
print(issubclass(ChildClass, (ParentClass, OtherClass)))    # True, classinfo는 클래스 객체 튜플일 수 있음. 모든 항목을 검사

# super() / 부모 메서드 활용 / 오버라이딩
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, namme, age, department)
        super().__init__(name, age)
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)             # 자식클래스에서 부모클래스를 사용하고 싶은 경우 활용
        self.gpa = gpa

    # 오버라이딩
    def talk(self):
        super().talk()
        print(f'저는 학생입니다.')

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)
p1.talk()                                       # 반갑습니다. 박교수입니다.     부모 메서드 활용
s1.talk()                                       # 반갑습니다. 김학생입니다.     메서드 오버라이딩
                                                # 저는 학생입니다.
```
### 다중 상속
- 파이썬은 두개 이상의 클래스를 상속 받을 수 있음
- 상속 받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 **상속 순서**에 의해 결정

## 파이썬 추가문법
### 조건표현식(Conditinoal Expression)
> 일반적으로 조건에 따라 값을 할당 할 때 활용
```python
<true인 경우 값> if <expression> else <false인 경우 값>

value = num if num >= 0 else -num
result = '홀' if num % 2 else '짝'
```
### enumerate 순회
> 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
>
> (index, value) 형태의 tuple로 구성된 열거 객체를 반환
- enumerate(iterable, start=0)
```python
for i in range(len(members)):
    print(f'{i} {members[i]}')

for i, member in enumerate(members):
    print(i, member)
```
### List Comprehension
> 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성
```python
[<expression> for <변수> in <iterable>]

[<expression> for <변수> in <iterable> if <조건식>]

[number**3 for number in range(1,4)]
```
### Dictionary Comprehension
```python
{key: value for <변수> in <iterable>}

{key: value for <변수> in <iterable> if <조건식>}

{number: number**3 for number in range(1,4)}
```
### lambda [parameter] : 표현식
- 람다함수: 표현식을 계산한 결과값을 반환하는 함수. 이름이 없는 함수라 익명함수라고도 불림
- 특징
    - return문을 가질 수 없다
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
    - 함수를 정의해서 사용하는 것보다 간결
    - def를 사용할 수 없는 곳에서도 사용가능

### 파이썬 버전별 업데이트
#### Type annotation
- 파이썬은 동적타입이라 필요 없지만 각 변수/함수마다 Type에 대한 설명을 덧붙임
- 정적 타입이 되는것은 아니고 코드 작성하는데 힌트를 주기 위함
```python
hello: str = 'hello world!'
def add(x: int, y: int) -> int:
    return x + y
result: int = add(7, 4)
``` 
#### Positional-only parameters
> 함수를 정의할 때 어떻게 호출해야 하는지를 함께 지정
```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```
- a, b는 위치만
- c, d는 위치 및 키워드 모두
- e, f는 키워드만