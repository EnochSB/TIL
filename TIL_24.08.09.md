#  defaultdict()
## 사용법
```python
from collections import defaultdict

int_dict = defaultdict(int)
list_dict = defaultdict(list)
set_dict = defaultdict(set)
new_dect = defaultdict(lambda: [0,0])
```

## 설명
- 딕셔너리를 만드는 dict클래스의 서브 클래스
- 인자로 주어진 객체(default-factory)의 기본값을 딕셔너리 값의 초기값으로 지정할 수 있다.


## 예시
### defaultdict(int)
- 문자열의 알파벳 갯수 세기
```python
letters = 'dongdongfather'
letters_dict = defaultdict(int)
for i in letters:
  letters_dict[i] += 1

# defaultdict(<class 'int>, {'d': 2, 'o':2, 'n': 2, 'g': 2, 'f': 1, 'a': 1, 'h': 1, 'e': 1, 'r': 1})
```

### defaultdict(list)
- 각 성이 갖는 이름 취합
```python
names = [('kim', 'sungsu'), ('kang', 'hodong'), ('park', 'jisung'), ('kim', 'yuna'), ('park', 'chanho')]
name_dict = defaultdict(list)
for i, j in names:
  name_dict[i].append(j)

# defaultdict(<class 'list'>, {'kim': ['sungsu', 'yuna'], 'kang': ['hodong', 'hodong'], 'park': ['jisung', 'chanho']})
```

### defaultdict(set)
- 각 성이 갖는 이름 취합
```python
names = [('kim', 'sungsu'), ('kang', 'hodong'), ('park', 'jisung'), ('kim', 'yuna'), ('park', 'chanho')]
name_dict = defaultdict(set)
for i, j in names:
  name_dict[i].add(j)

# defaultdict(<class 'set'>, {'kim': {'sungsu', 'yuna'}, 'kang': {'hodong'}, 'park': {'jisung', 'chanho'}})
```

### defaultdict(lambda: [0, 0])
- 그래프의 각 점에서 나가고 들어오는 간선 갯수 취합
```python
edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
graphDict = defaultdict(list)
outIn = defaultdict(lambda: [0, 0])

for edge in edges:
    dot1, dot2 = edge
    graphDict[dot1].append(dot2)

for dot, dots in graphDict.items():
    for i in dots:
        outIn[dot][0] += 1
        outIn[i][1] += 1
# outIn(<class 'list'>, {2: [1, 0], 3: [0, 2], 1: [1, 1], 4: [1, 0]})
```