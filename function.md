# [내장함수 정리](https://docs.python.org/ko/3/library/functions.html)
## 자주 사용하는 함수
- len(s)
    - 객체의 길이를 반환. 인자: 시퀀스/컬렉션
- sum(iterable, start=0)
    - start 및 iterable의 항목들을 왼쪽에서 오른쪽으로 합하고 합계를 반환.
    - iterable의 항목은 일반적으로 숫자. 시작값은 문자열이 될 수 없다.
- max(iterable)
    - iterable에서 가장 큰 항목이나 두 개 이상의 인자 중 가장 큰 것을 반환.
    - 여러 항목이 해당되면 처음 만난 항목을 반환
- min(iterable)
    - iterable에서 가장 작은 항목이나 두 개 이상의 인자 중 가장 작은 것을 반환.
    - 여러 항목이 해당되면 처음 만난 항목을 반환
## 계산 관련 함수
- abs(x)
    - 숫자의 절댓값을 반환. 인자: 정수, 실수 또는 __abs__()를 구현하는 객체.
    - 인자가 복소수라면 그 크기를 반환.
- divmod(a, b)
    - 두 수를 받아 몫과 나머지를 반환.
- pow(base, exp, mod=None)
    - base의 exp 거듭제곱을 반환.
    - mod가 있는 경우, base의 exp 거듭제곱의 모듈로 mod를 반환.
- round(number, ndigit=None)
    - number를 소수점 다음에 ndigits 정밀도로 반올림한 값을 반환.
    - ndigits가 생략되거나 None이면, 입력에 가장 가까운 정수를 반환.
## 논리 관련 함수
- all(iterable)
    - iterable의 모든 요소가 참이면(또는 iterable이 비어있으면) True를 반환.
- any(iterable)
    - iterable의 요소 중 어느 하나라도 참이면 True를 반환.
    - iterable이 비어있으면 False.
## 리스트 함수
- sorted(iterable, /, *, key=None, reverse=False)
- enumerate(iterable, start=0)
- filter(function, iterable)
## 기타
- bin(x)
    - 정수를 "0b'접두사가 붙은 이진 문자열로 반환.
- hex(x)
    - 정수를 "0x"접두사가 붙은 16진수 문자열로 반환.
- oct(x)
    - 정수를 "0o"접두사가 붙은 8진수 문자열로 반환.
- ord(c)
    - 유니코드 문자 c에 대응되는 유니코드 숫자를 반환.
- chr(i)
    - 정수 i에 대응되는 유니코드 문자를 반환.

- dir(object)