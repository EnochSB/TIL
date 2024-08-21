# 자바 입문
## 4. 배열
### 1차원 배열 생성
- 배열: 같은 데이터 타입을 가진 연속된 메모리 공간으로 이루어진 자료구조.
```java
int[] array = new int[4]; // 정수 4개를 저장 할 수 있는 배열

array[0] = 1;
array[3] = 2;

int value = array[0];

int[] array2 = new int[]{1, 2, 3, 4, 5}; // 선언과 동시에 초기화
```
### 배열과 for문
```java
int[] iarray = new int[100];
//배열에 값을 반복적으로 넣어야 하므로, for 반복문을 이용
for(int i = 0; i < iarray.length; i++){ 
//배열의 인덱스는 0부터 시작하므로, 0부터 배열의 길이보다 하나 작을때까지 반복하면 배열의 크기만큼 반복할 수 있다. 
        iarray[i] = i + 1;  
}
```
### 2차원 배열
```java
// 2차원 배열 생성
int[][] array4 = new int[3][4];
array4[0][0] = 10;

// 가변크기의 2차원 배열
int[][] array5 = new int[3][];
//위와 같이 선언하면 array5는 3개의 배열을 참조하겠다는 뜻. 그러나 아직은 참조하는 배열이 없다.

array5[0] = new int[1]; //정수를 하나 담을 수 있는 배열을 생성해서 array5 의 0 번째 인덱스가 참조
array5[1] = new int[2];
array5[2] = new int[3];

// 선언과 동시에 초기화
int[][] array6 = {{1}, {2,3}, {4,5,6}};
```
### for each
```java
// array.length를 사용하지 않고 바로 배열의 값에 접근
int[] iarr = {10, 20, 30, 40, 50};

for(int value:iarr){
    System.out.println(value);
}
```