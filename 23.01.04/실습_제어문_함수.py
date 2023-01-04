# 1번
n = int(input('정수를 입력하세요 > '))
if n >= 0:
    print(n)
else:
    print(-n)

# 2번
number_list = [1, 2, 3, 4, 5]
cnt = 0
for i in number_list:
    cnt += 1
print(cnt)

# 3번
number_list = [-1, -2, -3, -4, -5]
total = 0
for i in number_list:
    total += i
print(total)

# 4번
number_list = [2, 3, 5, 7]
total = 0
cnt = 0
for i in number_list:
    total += i
for i in number_list:
    cnt += 1
print(total / cnt)

# 5번
number_list = [1, 2, 3, 4, 5]
mul = 1
for i in number_list:
    mul *= i
print(mul)

# 6번
number_list = [1, 2, 3, 4, 5]
max_num = 0
for i in number_list:
    if i > max_num:
        max_num = i
print(max_num)

# 7번
number_list = [5, 5, 5, 2]
min_num = number_list[0]
for i in number_list:
    if i < min_num:
        min_num = i
print(min_num)

# 6번-음수포함
number_list = [-11, -1, -3, -4, -5]
max_num = number_list[0]
for i in number_list[1:]:
    if i > max_num:
        max_num = i
print(max_num)