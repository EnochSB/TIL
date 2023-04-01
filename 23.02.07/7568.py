# 덩치
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

group = []
for _ in range(int(input())):
    w, h = map(int, input().split())
    group.append((w, h))

for i, j in group:
    cnt = 0
    for x, y in group:
        if x > i and y > j:
            cnt += 1
    print(cnt + 1, end=' ')