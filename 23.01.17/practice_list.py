# 최소, 최대
n = int(input())
nums = [i for i in map(int, input().split())]
print(min(nums), max(nums))

# 숫자의 합
n = int(input())
total = 0
for num in input():
    total += int(num)
print(total)

# 수 정렬하기
n = int(input())
nums = [int(input()) for i in range(n)]
print(*sorted(nums), sep='\n')

# 최댓값
nums = [int(input()) for i in range(9)]
print(max(nums), nums.index(max(nums))+1, sep='\n')
