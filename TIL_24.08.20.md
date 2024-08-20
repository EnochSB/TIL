#  자바 입문
## 3. 제어문
### if문
- 조건식이 true일 경우에만 실행문이 실행
- if(조건문) 이후 {}(블럭)을 생략할 수 있다. 이 경우 실행문은 조건문 이후 한 줄만 적용.
```java
if(조건식){
    실행문;
    실행문;
}else if(조건식){
    실행문;
}else{
    실행문;
}
```

### 논리연산자
|<center>A</center>|<center>B</center>|<center>A && B</center>|<center>A \|\| B|<center>! A</center>|<center>A ^ B</center>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**TRUE**|**TRUE**|**TRUE**|**TRUE**|*FALSE*|*FALSE*|
|**TRUE**|*FALSE*|*FALSE*|**TRUE**|*FALSE*|**TRUE**|
|*FALSE*|**TRUE**|*FALSE*|**TRUE**|**TRUE**|**TRUE**|
|*FALSE*|*FALSE*|*FALSE*|*FALSE*|**TRUE**|*FALSE*|

### 삼항연산자
- 조건식 ? 피연산자1 : 피연산자2
- int a = (5>4) ? 50 : 40;
- 피연산자에는 주로 값이 오지만 연산식도 들어갈 수 있다.

### switch문
- 어떤 변수의 값에 따라 실행할 수 있도록 하는 제어문.
- break가 없다면 만족하는 case의 실행문을 실행하고 그 이후의 실행문을 전부 실행.
- 변수에는 정수 혹은 문자열.
```java
int value = 1;
switch(변수){
    case 값1 : 
        실행문; 
        break;
    case 값2 : 
        실행문; 
        break;
    // 다음과 같이 case문을 한번에 사용하면 더 짧게 코드를 짤 수 있다.
    case 값3:
    case 값4:
    case 값5:
        실행문;
        break;
    default;
        실행문;
}
```

### while문
```java
while(조건문){
    실행문;
}

int i = 0;  //while에서 사용할 변수를 선언

while(i < 10){
    System.out.println(i);
    i++; //조건문을 원하는 만큼만 반복하고 빠져나가기 위한 부분 
}
```
### do while문
-  while문은 조건을 만족하지 않으며 한 번도 실행을 안하지만, do while문은 무조건 한 번은 실행하는 반복문.
```java
do{
    실행문;
}while(조건문);

int value = 0;

// Scanner는 java.util 패키지에 있는 클래스로써 키보드로 부터 값을 입력받는 등 유용하게 사용할 수 있는 클래스
Scanner scan = new Scanner(System.in);
//위 처럼 작성하시면 키보드로부터 값을 입력받을 수 있는 Scanner객체가 생성 

do{
    value = scan.nextInt(); // Scanner클래스를 이용하여 키보드로부터 숫자값을 입력
    System.out.println("입력받은 수 : " + value);  
}while(value != 10);  // 입력받은 값이 10이 아닐 경우에는 계속 반복

System.out.println("반복문 종료");
```
### for문
- for문은 변수초기화, 조건식, 증감식이 한줄에 모두 있다.
  1. 초기화는 최초 한 번만 실행.
  2. 조건식을 실행해 결과가 false면 for문을 탈출.
  3. 결과가 true면 실행문을 실행.
  4. 증감식을 실행.
  5. 2~4를 반복.
```java
for(초기화식; 조건식; 증감식){
    실행문;
    실행문;
}

int total = 0; //1부터 100까지 합한 결과값을 담기위한 변수 선언 

for(int i = 1; i <= 100; i++){ //1부터 100까지 반복하기 위한 for 반복문 

    total += i; // 1부터 100까지 반복해서 total 변수에 값을 누적  
}
System.out.println(total);  //결과값 출력 
```