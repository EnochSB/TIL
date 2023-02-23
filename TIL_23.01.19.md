# 딕셔너리
## 1. 해시 테이블
### 1.1 해시란
- 해시 함수: 임으 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
- 해시: 해시 함수를 통해 얻어진 값

### 1.2 파이썬 딕셔너리
- 파이썬 딕셔너리는 해시 함수와 해시 테이블을 이용하기 때문에 삽입, 삭제, 수정 조회 연산의 속도가 리스트보다 빠르다.
  - Hash function을 이용한 산술 계산으로 값이 잇는 위치를 바로 알 수 있기 때문에

| 연산 종류 | 시간복잡도 |
| --- | --- |
| Get Item | O(1) |
| Insert Item | O(1) |
| Update Item | O(1) |
| Delete Item | O(1) |
| Search Item | O(1) |

- 딕셔너리를 사용하면 좋을 때
  - Key, Value구조로 관리를 해야하는 경우(순서나 인덱스가 아니라)
  - 데이터에 대한 빠른 접근 탐색이 필요한 경우

## 2. 딕셔너리 기본 문법
### 2.1 선언
```python
myDict = {
  'name': 'kyle',
  'gentdr': 'male',
  'address': 'Seoul'
}
```

### 2.2 삽입/수정
```python
myDict = {
  'name': 'kyle',
  'gentdr': 'male',
  'address': 'Seoul'
}
myDict['job'] = 'coach'
# {'name': 'kyle', 'gentdr': 'male', 'address': 'Seoul', 'job': 'coach'}
```
```python
myDict = {
  'name': 'kyle',
  'gentdr': 'male',
  'address': 'Seoul'
}
myDict['name'] = 'justin'
# {'name': 'justin', 'gentdr': 'male', 'address': 'Seoul'}
```

### 2.3 삭제
- 두번째 인자로 default(기본)값을 지정하여 KeyError 방지 가능
```python
myDict = {
  'name': 'kyle',
  'gentdr': 'male',
  'address': 'Seoul'
}
phone = a.pop('phone', '010-1234-5678')
# {'name': 'kyle', 'gentdr': 'male', 'address': 'Seoul'}
# 010-1234-5678
```

### 2.4 조회
- 기본적으로 딕셔너리[key]로 조회
- 딕셔너리.get(key, default)로 조회하면 key가 없어도 오류가 안뜬다.
```python
myDict = {
  'name': 'kyle',
  'gentdr': 'male',
  'address': 'Seoul'
}
print(myDict['phone'])
print(myDict.get('phone', '없음'))
# KeyError
# 없음
```

## 3. 딕셔너리 메서드
### 3.1 .keys()
- 딕셔너리 key 목록이 담긴 dict_keys 객체 반환
- dict_keys(['name', 'gentdr', 'address'])

### 3.2 .values()
- 딕셔너리 value 목록이 담긴 dict_values 객체 반환
- dict_values(['kyle', 'male', 'Seoul'])

### 3.3 .items()
- 딕셔너리의 (key, value) 쌍 목록이 담긴 dict_items 객체 반환
- dict_items([('name', 'kyle'), ('gentdr', 'male'), ('address', 'Seoul')])