# 02. Web - The box model
## 1. 개요
> CSS Box Model: 모든 HTML 요소를 박스로 표현한다.
## 2. 구성 요소
### Box의 구성
![box구성](23.02.23/box-model.png)
- Margin: 해당 박스와 다른 요소 사이의 공백, 가장 바깥 영역
- Border: 컨텐츠와 패딩을 감싸는 테두리
- Pading: 컨텐츠 주위에 위치하는 공백 영역
- Content: 컨텐츠가 표시되는 영역

### Box 구성의 방향 별 명칭
![방향별 명칭](23.02.23/Boxmodell-detail.png)

### box-sizing 속성
- 박스의 사이즈(width, hight)를 지정할 때 기본적으로 content의 사이즈를 대상으로 함.
- 그러나 우리는 border를 기준으로 사이즈를 정하고 싶다.
- 그럴때 쓰는 것이 box-sizing
```CSS
* {
  box-sizing: content-box;
}

* {
  box-sizing: border-box;
}
```

## 3. 박스 타입

### block 타입 특징
- 항상 새로운 행으로 나뉨
- width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
- 기본적으로 width속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지.(너비를 사용가능한 공간의 100%로 채우는 것)
- 부모 자식 관계이면 부모 요소의 너비 100% 차지, 자식 컨텐츠의 최대 높이를 취함.
- block 요소의 총 너비와 총 높이는 content + padding + border width/height
- block 요소는 서로 margins로 구분된다.
- 대표적인 block 타입의 태그
  - h1~6, p, div

### inline 타입 특징
- 새로운 행으로 나뉘지 않음
- width와 height 속성을 사용할 수 없음(img는 사용 가능)
- 크기를 제어하려면 block 요소로 변경하거나 inling-block 요소로 설정
- 수직 방향
  - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
- 수평 방향
  - padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inling 타입 태그
  - a, img, span

## 참고
### shorthand 속성
- border
  - border의 width, style, color를 한번에 설정
  ```CSS
  /* shorthand(축약어): 작성 순서 무관하게 스타일, 픽셀, 색상 작성 */
  .box {
    border: 1px solid black;
  }
  ```
- margin & padding
  - 4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성
  ```CSS
  /* 4개 - 상우하좌(시계방향) */
  .box {
    /* 4개 - 상우하좌(시계방향) */
    margin: 10px 20px 30px 40px;
    padding: 10px 20px 30px 40px;

    /* 3개 - 상/좌우/하 */
    margin: 10px 20px 30px;
    padding: 10px 20px 30px;

    /* 2개 - 상하/좌우 */
    margin: 10px 20px;
    padding: 10px 20px;

    /* 1개 - 공통 */
    margin: 10px;
    padding: 10px;
  }
  ```
### display: inline-block
- inline과 block 요소 사이의 중간 지점을 제공하는 display 값
- 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용
- block 요소의 특징을 가짐
  - 너비 및 높이 속성이 준수
  - 패딩, 여백 및 테두리로 인해 다른 요소가 상자에서 밀려난다.

### Margin collapsing(마진 상쇄)
- 두 block 타입 요소의 margin top과 bottom이 만나 큰 margin으로 결합되는 현상
- 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함
  - 각 요소에 대한 상/하 margin을 각각 설정하지 않고 한 요소에 대해서만 설정할 수 있음.