# 문제 1: 몫과 나머지
T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{test_case} {a // b} {a % b}')

# 문제 2: 평균값
T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    result = sum(num_list) / 10
    print(f'#{test_case} {result:.0f}')
    
# 문제 3: 아주 간단한 계산기
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)

# 문제 4: 스탬프
sharp = int(input())
for i in range(sharp):
    print('#', end='')

# 문제 5: 최대수
T = int(input())
for test_case in range(1, T+1):
    num_list = list(map(int, input().split()))
    max_num = max(num_list)
    print(f'#{test_case} {max_num}')
