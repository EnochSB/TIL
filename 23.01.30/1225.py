# 이상한 곱셈

a, b = input().split()
a_list = list(map(int, a))
b_list = list(map(int, b))
print(sum(a_list) * sum(b_list))