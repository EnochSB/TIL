# 점수 집계
import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    sco = list(map(int, input().split()))
    sco.remove(max(sco))
    sco.remove(min(sco))
    if max(sco) - min(sco) >= 4:
        print('KIN')
    else:
        print(sum(sco))