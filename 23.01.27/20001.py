# 고무오리 디버깅
duck = input()
stack = []
while not duck.endswith('끝'):
    duck = input()
    if duck == '문제':
        stack.append(duck)
    elif duck == '고무오리':
        if stack:
            stack.pop()
        else:
            stack.append('문제')
            stack.append('문제')
if stack:
    print('힝구')
else:
    print('고무오리야 사랑해')