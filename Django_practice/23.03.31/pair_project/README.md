# 가계부 서비스 만들기
## 후기
- CRUD를 구현하고 COPY까지 구현하는게 본 과제였고 여기까지는 쉬웠다.
- TRY에 분류 입력시 select 태그 활용, 분류별 다른 디자인, 분류별 조회, 특정 기준 정렬 조회를 구현했다.
- select, 분류별 디자인(script)은 간단했지만 조회는 애를 먹었다.

- index에 select 태그로 분류를 고르면 바로 해당 분류의 리스트를 조회하는 로직을 짰다.
- select를 입력 받을 때, form에 method를 POST로 두고 view함수에서 POST로 입력 받았을 경우에 category를 get하고 get이 존재할 경우 filter를 통해 해당 리스트를 뽑았다.
- POST입력이 없는 경우에는 전체를 조회.(처음 index함수 호출 될때는 POST가 없기 때문)

- 특정 기준 정렬 조회는 사용 날짜와 사용 금액을 위한 버튼만 만들었다.
- a 태그를 사용해 sort값과 order값을 GET.
  - \<a href="?sort=date&order={{ order }}">사용날짜 {{ order }}\</a>
  - 날짜를 누르면 date, 금액을 누르면 amount가 sort에 들어감.
- order GET할 때 존재하지 않으면 넣을 defult_value도 추가.(GET.get(order, 오름차순))
- 각 sort값에 따라, order에 따라 order_by. order의 값을 반대로 바꿈.

- 첫번째로 까다로웠던 것은 위에서 만든 분류를 선택하고 정렬하면 분류를 선택한 것이 취소되고 전체에서 정렬하게 되었던 일.
- 선택된 분류를 그대로 유지하기 위해 POST입력이 없는 경우에도 GET 을 통해 분류값을 받아내고 이를 통해 filter로 조회.
- 받은 분류값을 다시 context에 담아 html호출에 같이 보냈다.
- 보내진 분류값은 a 태그의 링크에 담았다.
  - {% if category_target %}&category_target={{ category_target }}{% endif %}
  - category_target이 존재하면 쿼리스트링에 &category_target을 추가

- 두 번째로 까다로웠던 것은 버튼 2개가 오름차순과 내림차순으로 함께 변한다는 것.
- 두 버튼이 따로 동작하게 만들기 위해 order를 date_order와 amount_order로 나눴다.
- 그리고 sort가 date일 때는 date_order에 따라 작동하고 amount일 때는 amount_order에 따라서만 작동하게 if문을 작성했다.

- 아쉬웠던 점은 시간이 부족해 프론트앤드에는 크게 신경을 못쓴점.
- 값을 넣지 않고 create나 edit하려고 할때를 처리하지 못한점.
- 쿼리 스트링을 쓰지 않고 값을 전달하는 방법을 찾지 못한점. 등이 있다.