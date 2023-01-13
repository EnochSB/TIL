# 홀수만 더하기
T = int(input())
result = 0
for t in range(1, T+1):
    for i in map(int, input().split()):
        if i % 2:
            result += i 
    print(f'#{t} {result}')
    result = 0