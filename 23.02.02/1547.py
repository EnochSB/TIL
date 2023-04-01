# 공
cups = [0, 1, 0, 0]
for _ in range(int(input())):
    x, y = map(int, input().split())
    if cups[x] or cups[y] == 1:
        cups[x], cups[y] = cups[y], cups[x]

print(cups.index(1))