# 자바 입문
## 1. 자바
### 자바의 특징
- 배우기 쉽다!(C, C++에 비해)
- 플랫폼에 독립적(JVM만 있다면 윈도우, 리눅스, 맥 등 상관없이 실행)
  - JVM(Java Virtual Machine): OS에 종속받지 않고 CPU가 JAVA를 인식, 실행할 수 있게 하는 가상 컴퓨터
  - 컴파일러가 코드를 바로 기계어로 변환 시키지 않고 **java bytecode(*.class)** 로 변환 후 **JVM**이 기계어로 변환
- 객체지향 프로그래밍
- Garbage Collector로 사용되지 않는 메모리를 자동적으로 정리

### 자바 개발환경 구축
- JDK(Java Development Kit) 다운로드/설치 [링크](https://www.oracle.com/java/technologies/downloads/)
- 환경변수 설정
  - JAVA_HOME: jdk 설치 경로(C:\\Program Files\\Java\\jdk)
  - Path: **%JAVA_HOME%\\bin;** C:\\ProgamData ...
  - CLASSPATH: class를 찾는 위치(%JAVA_HOME\lib)

### 자바 개발 순서
- 소스 작성 => 컴파일 => JVM으로 실행
- cmd
  - 소스 작성
  - javac 파일이름.java로 컴파일
  - java 파일이름 으로 실행
- VSCode
  - ctrl + shift + p: Create Java Project
  - Project 타입 선택(Maven, Spring Boot 등, 없으면 No build tools)
  - 경로 지정 / 프로젝트 이름 지정
  - src에 java 파일 생성 및 소스 작성
  - bin에는 자동으로 컴파일 된 class파일 생성됨
  - 자바 파일 우클릭 Run Java
  ```java
  public class App {
      // 메인은 프로그램의 시작점
      public static void main(String[] args) throws Exception {
          System.out.println("Hello, World!");
      }
  }
  ```