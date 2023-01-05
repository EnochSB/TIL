# 모듈 & 예외처리
## 컬렉션
### 딕셔너리(Dictionary)
> 키-값(key-value) 쌍으로 이뤄진 모음(collection)
- 키(key): 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능)
- 값(values): 어떠한 형태든 관계 없음
- 키와 값은 **:**로 구분. 개별 요소는 **,**로 구분.
- 변경 가능하며(mutable), 반복 가능(iterable)
    - 딕셔너리는 반복하면 키가 반환됨.
```python
# 생성, 접근
students = {'홍길동': 30, '김철수': 25} # list, dictionary는 key로 설정 불가
students['홍길동'] # 30

# 키-값 추가 및 변경
students['홍길동'] = 80
students['박영희'] = 95

# 키-값 삭제
students.pop['홍길동']

# 딕셔너리 순회
grades = {'john': 80, 'eric': 90}
for name in grades:
    print(name) # 키 순회
    print(grades[name]) # 값 순회

# 순회_추가 메소드
print(grades.keys()) # dict_keys(['john', 'eric'])
print(grades.values()) # dict_values([80, 90])
print(grades.items()) # dict_items([('john', 80), ('eric', 90)]) (key, value)의 튜플로 구성된 결과
``` 

## 모듈
### 모듈과 패키지
- 모듈: 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함
- 라이브러리
    - 다양한 패키지가 하나의 묶음으로 모여있는 집합
- pip: 모듈, 패키지, 라이브러리를 관리하는 관리자.
### [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)
- 파이썬에 기본적으로 설치된 모듈과 내장 함수
#### random
> 숫자/수학 모듈 중 의사 난수 생성(pseudo random number generator)
- random.randint(a, b)
    - a 이상 b 이하의 임의의 정수 N 리턴
- random.choice(seq)
    - 비어있지 않은 시퀀스에서 임의의 요소를 리턴
    - seq가 비어있으면 IndexError를 발생
- random.shuffle(seq)
    - seq를 제자리에서 섞기
- random.sample(population, k)
    - 무작위 비복원 추출한 결과인 k 길이의 리스트 리턴
#### datetime
> 날짜와 시간을 조작하는 객체 제공
- datetime.date(year, month, day)
    - 모든 인자 필수, 인자는 특정범위 내 정수
    - 범위를 벗어나면 ValueError
- datetime.date.today()
    - 현재 지역 날짜 리턴
- datetime.datetime.today()
    - 현재 지역 datetime을 리턴. now()를 활용해 탐존 설정 가능.
#### os
> os(운영체제)를 조작
- os.listdir(path='.')
    - pathe에 의해 주어진 디렉터리에 있는 항목들의 일므을 담고 있는 리스트를 리턴.
    - 리스트는 임의의 순서로 나열. 특수 항목은 포함X
- os.mkdir(path)
    - path라는 디렉터리를 만든다
- os.chdir(path)
    - paht를 변경
### 파이썬 패키지
> PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
- 패키지 관리는 추후 Django학습하며 보충

## 에러/예외 처리(Error/Exception Handling)
### 디버깅
> 제어가 되는시점. 조건/반복, 함수. '값이 변경되는 시점'
- 에러 메시지가 발생하는 경우
    - 해당하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
    - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
### 에러와 예외
#### 문법에러(Syntax Error)
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
#### 예외(Exception)
- 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- ZeroDivisionError
- NameError
- TypeError
- ValueError
- IndexError
- KeyError
- ModuleNotFoundError
- KeyboardInterrupt
### 예외 처리
- try 문 / except 절을 이용하여 예외 처리를 할 수 있음
- try문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, except 없이 실행 종료
- except문
    - 예외가 발생하면, except 절이 실행
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
```python
try:
    num = input('숫자입력 : ')
    print(int(num))
except:
    print('숫자가 아닙니다')
```
### 예외 발생시키기
