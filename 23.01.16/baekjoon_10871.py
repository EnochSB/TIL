# X보다 작은 수
n, x = map(int, input().split())
s_nums = []
nums = list(map(int, input().split()))
for num in nums:
    if num < x:
        s_nums.append(num)
print(*s_nums)