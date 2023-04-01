# 지능형 기차
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

cnt = 0
max_cnt = 0
for _ in range(4):
    off, on = map(int, input().split())
    cnt = cnt - off + on
    if cnt > 10000:
        cnt = 10000
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)