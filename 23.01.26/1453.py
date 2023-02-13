# 피시방 알바
n = input()
cus = list(map(int, input().split()))
seat = set(cus)
print(len(cus) - len(seat))