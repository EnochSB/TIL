# 대표값
nums = [int(input()) for _ in range(10)]
num_d = {}
for num in nums:
    num_d[num] = num_d.get(num, 0) + 1
print(sum(nums) // 10)
print(sorted(num_d, key= lambda x: num_d[x], reverse=True)[0])