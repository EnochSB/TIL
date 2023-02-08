# 더하기
T = int(input())
for t in range(T):
    n = int(input())
    nums = [num for num in map(int, input().split())]
    print(sum(nums))