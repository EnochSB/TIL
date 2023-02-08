# 숫자의 개수
num = 1
for index in range(3):
    num *= int(input())
num = str(num)
for index in range(10):
    print(num.count(str(index)))