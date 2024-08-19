# 자바 입문
## 2. 변수와 계산
### 변수
- 변수: 값(Data)을 저장할 수 있는 메모리의 공간.  값이 변할 수 있는 수.
- 변수의 선언
  - 타입 + 변수이름;
    - int count; (정수 값을 담는 count라는 이름의 변수 선언)
    - double average; (실수 값을 담는 average라는 변수 선언)
  - 식별자(identifier)는 클래스, 메소드, 변수 등 다양한 대상에 대해 이름이 붙여지는 경우. 그 이름을 뜻 함.
- java 식별자(변수 이름) 명명 규칙
  - 하나 이상의 글자.
  - 첫 글자는 문자 이거나 '$', '_'
  - 두 번째 이후는 숫자, 문자, '$', '_'
  - '$', '_'  이외 특수문자 사용 불가능
  -  길이 제한 없음
  - 키워드는 식별자로 사용불가
  - 상수 값을 표현하는 단어 true, false, null은 식별자로 사용불가
- 변수 명명 관례
  - 첫 문자가 소문자인 명사
  - 여러 단어로 구성될 경우 두 번째 단어부터는 첫 글자를 대문자로(helloWorld)
  - '_'를 쓰지 않음
  - 규칙은 반드시 지켜야함. 관례는 약속이기에 지켜주는 것이 좋다.
- 변수의 사용
  ```java
  public class VariableExam {

      public static void main(String[] args) {
          int totalCount;
          totalCount = 10;
          totalCount = 20;
          double average = 11.1;
          String name = "James";
      }
  }
  ```

### 상수
- 상수: 변하지 않는 값. 변경 불가.
- 상수 선언
  - final 상수타입 상수명;
  - 한 번만 값을 담을 수 있다.
- 상수 명명
  - 대문자로만 구성된 명사
  - 여러 단어일 경우 단어 사이에 '_'을 써서 구분.
- 값이 변하면 위험할 경우 사용.
- 값만 봤을 때 무엇을 의미하는 지 쉽게 파악할 수 없어도 값 자체를 사용하기 보다는 상수를 사용.
  ```java
  public class ConstantExam {

      public static void main(String[] args) {
          final int J;
          J = 10;
          // J = 5; 재할당 불가

          double circleArea;
          final double PI= 3.14159;
          circleArea = 3 * 3 * PI;

          final int OIL_PRICE = 1450;
          int totalPrice = 50 * OIL_PRICE;
      }
  }
  ```

  ### 기본형 타입
  - 가장 기본이 되는 데이터 타입. 정수형, 실수형, 문자형, 불린형.
  - 논리형(불린형)
    - 1byte. true / false (0과 1로 저장하는 것이 아님.)
  - 문자형(char)
    - 2byte. 작은 따옴표로 한 글자를 표현.
  - 정수형(int, long, byte, short, char)
    - int: 4byte.
    - long: 8byte. int 보다 더 큰 범위의 정수.
  - 실수형(float, double)
    - float: 4byte
    - double: 8byte. float보다 더 큰 범위 실수.
  - 리터럴
    - 소스 코드의 고정된 값을 대표하는 용어.
    - 일종의 값. true, false, 10, 11.1, a 등 데이터 값 다체를 리터럴이라고 칭한다.
  ```java
  public class PrimitiveDataTypeExam {

      public static void main(String[] args) {
          boolean  isTrue = False;
          char c = 'nice';
          int x = 33;
          long y = 34522442824724l; // l 혹은 L을 뒤에 붙여야 한다.
          float f = 33.4f;  // f 혹은 F를 뒤에 붙여야 한다.
          double d = 394842782442.42245;
      }
  }
  ```

### 기본형의 타입(형) 변환
- 형변환: 변수 또는 리터럴의 타입을 다른 타입으로 변환.
- byte < short, char < int < long < float < double
- 묵시적 형변환(암묵적 형변환)
  - 크기가 작은 타입을 더 큰 타입으로 바꿀때 묵시적으로 형을 바꾼다.
  - int x = 50000; => long y = x;
- 명시적 형변환(강제 형변환)
  - 크기가 더 큰 타입을 작은 타입으로 바꿀 때 명시적으로 변환.
  - long x = 50000; => ing y = (int) x;
  - 반드시 (타입)으로 명시적으로 형을 바꾸어 주어야 한다.
  ```java
  public class TypeCastingExam {

      public static void main(String[] args) {
        int x = 50000;
        long y = x;

        long a = 8;
        int b = (int) a;
      }
  }

### 산술연산자
- 연산: 데이터를 처리하여 결과를 산출하는 것.
- 부호 연산자(+ , -): 부호를 결정
- 산술 연산자(+, -, *, /, %)
- 증감 연산자(++, --)
- 피연산자: 연산 당하는 대상
- 단항 연산자: 피 연산자가 1개인 연산자(부호, 증감)
  ```java
  public class OperatorExam {

      public static void main(String[] args) {
          int i1 = -5;  // -5
          int i2 = +i1; // -5 부호연산자 +는 부호를 그대로 유지한다는 의미.
          int i3 = -i1; // 5

          int i4 = ++i3;  // i4 = i3 = i3 + 1 대입 전에 i3 + 1
          int i5 = i3++;  // i5 = i3, i3 + 1 대입 후에 i3 + 1

          int i =  5;
          int j = 2;

          System.out.println(i + j);  // 7
          System.out.println(i - j);  // 3
          System.out.println(i * j);  // 10
          System.out.println(i / j);  // 2, i와 j가 int타입 이기 때문에 그 연산 결과도 int
          System.out.println(i / (double)j);  // 2.5, j가 double타입으로 형변환 되어 그 연산 결과도 double. 둘 중 하나만 해도 됨.
          System.out.println(i % j);  // 1, 나머지 연산
      }
  }

### 비교연산자
- ==, !=, <, >, <=, >=
- 비교 연산자의 결과는 boolean

### 대입 연산자
- 단순 대입 연산자
  - i = 10;
- 복합 대입 연산자
  - i += 10;

### 연산자 우선순위
|||
|---|---|
| 최우선 연산자 |. [] ()|
|단항 연산자|++ -- ! ~ +/- : (부정, bit변환) > (부호) > (증감)|
|산술 연산자|( * / % ) > ( + - ) > shift/시프트 연산자(>> << >>>)|
|비교 연산자|> < <= >= == !=|
|비트 연산자|AND(&) OR(\|) XOR(^, 배타적 논리합, 하나만 true일경우 true) NOT(~)|
|논리 연산자|AND(&&) > OR(\|\|) NOT(!)|
|삼항 연산자|조건식?: int d = (a > b) ? a-b : b-a;|
|대입 연산자|= *= /= %= += -=|
|증감 후위 연산자|i++ i--|
