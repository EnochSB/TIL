# 홀수
nums = []
for index in range(7):
    num = int(input())
    if num % 2 == 1:
        nums.append(num)
if len(nums) != 0:
    print(sum(nums), min(nums), sep='\n')
else:
    print(-1)