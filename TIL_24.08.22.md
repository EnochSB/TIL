# 자바 입문
## 5. 클래스와 객체
### 클래스 선언
- 클래스는 객체를 만들기 위한 틀. 객체를 만들기 전 클래스를 만들어야 한다.
```java
// Car.java
public class Car{

}
```
- Car.java 파일을 생성 후 저장하면 컴파일되어 디스크에 Car라는 클래스가 생성됨.
- 클래스가 생성되었다고 해서 객체가 생성된 것이 아님.

### 객체 생성
```java
public class CarExam{
    public static void main(String args[]){
        Car c1 = new Car(); // 연산자 new는 뒤에 나오는 생성자를 이용해 메모리에 객체를 생성하라는 명령.
        Car c2 = new Car(); // 생성된 객체를 참조하는 변수 c1, c2가 선언되었다.
    }
}
```

### 참조 타입
- 참조형 타입: 기본형 타입을 제외한 모든 타입. 배열과 클래스도 참조 타입이다.
- 참조형 변수
  - String str1 = new String("hello");
  - new는 객체를 메모리에 올려준다. 이렇게 올라간 객체를 인스턴스라고 한다.
  - str1이 올라간 인스턴스를 참조한다. 변수가 인스턴스의 값을 갖고 있는 것이 아닌 값이 저장된 장소(메모리의 위치)를 가리키고 있는 것.
  - 위치 값이 저장된다고 하더라도 어떤 메모리에 저장되었는지를 알 수는 없다.
  - 앞으로 배울 클래스들은 모두 참조형.

### String 클래스
- 문자열을 표현하는 자바에서 가장 많이 사용하는 클래스
- new를 사용하지 않고 인스턴스 생성 가능.
- String 인스턴스 생성 방법
  1. new를 사용하지 않는 방법
    ```java
    String str1 = "hello";
    String str2 = "hello";
    ```
    - "hello"라는 문자열이 메모리 중에서 상수가 저장되는 영역에 저장된다.(상수는 변하지 않는 값을 의미)
    - str2가 선언될 때 hello 라는 문자열 상수는 이미 만들어져 있으므로 str1이 참조하는 인스턴스를 str2도 참조.
  2. new를 사용하는 방법
    ```java
    String str3 = new String("hello");
    String str4 = new String("hello");
    ```
    - new를 이용하면 무조건 새로운 인스턴스를 생성.
    - str3과 str4는 서로 다를 인스턴스를 참조.
- 메모리를 아끼려면 String은 new를 사용하지 않고 사용하는 것이 좋다.
- String은 불변 클래스: String이 인스턴스가 될때 가지고 있던 값을 나중에 수정할 수 없다.
- 문자열과 관련된 다양한 메소드를 가지고 있다. 메소드를 호출한다 하더라도 String 내부의 값은 변하지 않는다.
- String이 가지고 있는 메소드중 String을 반환하는 메소드는 모두 새로운 String을 생성해서 반환한다.
  ```java
  String str5 = "hello world";
  String str6 = str5.substring(3);  // substring은 문자열을 자른 결과를 반환하는 메소드. 해당 코드가 실행되어도 str5는 변하지 않는다.
  // str6은 str5가 가지고 있는 문자열 중 3번째 위치부터 자른 결과 즉 새로운 String을 참조.
  ```

### 필드 선언
- 자동차는 이름, 번호를 가지고 있고, 달리고 멈추는 기능이 있다. 여기에서 클래스가 가지고 있는 것을 **속성**이라고 한다. 자바에서는 이러한 속성을 **필드**(Field)라는 용어로 사용한다.
```java
    public class Car{
        String name;    
        int number;
    }
```
- 클래스 인스턴스화
```java
    Car c1 = new Car();
    Car c2 = new Car();
    //Car라는 인스턴스가 메모리에 2개 만들어 진다. 객체별로 name과 number라는 속성을 가진다.

    //참조변수 다음의 점(dot)은 참조변수가 참조하는 객체가 가지고 있는 것을 사용할 때 사용
    //c1.name은 c1이 참조하는 객체의 name을 의미.

    c1.name = "소방차";
    c1.number = 1234;

    c2.name = "구급차"
    c2.number = 1004;

    System.out.println(c1.name);  // c1이 참조하는 객체의 name을 출력
    System.out.println(c1.number); // c1이 참조하는 객체의 number를 출력

    String name = c2.name;   // c2가 참조하는 객체의 name을 String 타입 변수 name도 참조
```