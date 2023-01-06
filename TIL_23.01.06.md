# 파일 입출력
## 파일 입력
- open(file, mode='r', encoding=None)
    - file: 파일명
    - mode: 텍스트 모드
    - encoding: 인코딩 방식(일반적으로 utf-8활용)

    | mode | meaning |
    | --- | --- |
    | 'r' | open for reading (default)|
    | 'w' | open for writing, truncating the file first |
    | 'x' | open for exclusive creation, falling if the file already exists |
    | 'a' | open for writing, appending to the end of file if it exists |
    | 'b' | binary mode |
    | 't' | text mode(default) |
    | '+' | open for updating (reading and writing) |
- 파일 객체 활용
    ```python
    f = open('workfile', 'r', encoding='UTF8')
    print(f.read())
    f.close()
    ```
- **with 키워드 활용**
    ```python
    with open('workfile') as f:
        read_data = f.read()
        # 자동 닫기
    ```
    - with 키워드를 사용하지 않으면, f.close()를 반드시 호출하여 종료시켜야 오류가 없다. 따라서 일반적으로 with 키워드를 활용.
## [JSON](https://docs.python.org/ko/3/library/json.html#module-json)
> 자바스크립트 객체 표기법
>
> 개발환경에서 많이 활용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용.
- 문자 기반(텍스트) 데이터 포멧으로 다수의 프로그래밍 환경에서 쉽게 활용 가능.
    - 텍스트를 언어별 데이터 타입으로 변환시키거나
    - 언어별 데이터 타입을 적절하게 텍스트로 변환
```python
import json
movie_json = open("json_file", encoding="UTF8")
movie = json.load(movi_json) # movie가 딕셔너리가 된다.
```

### [pprint](https://docs.python.org/ko/3/library/pprint.html)
```python
from pprint import pprint
pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)
# object 출력
# indent: 들여쓰기
# width: 한줄 당 최대 글자 수
# depth: 한줄 당 최대 항목 수
# sort_dicts: 알파벳 순 정렬
# stream: 실시간 로그 스트림 출력
```
