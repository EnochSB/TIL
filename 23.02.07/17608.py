# 막대기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

sticks = deque()
sticks.append(0)
for _ in range(int(input())):
    tmp = int(input())
    while True:
        check = sticks.pop()
        if check > tmp:
            sticks.append(check)
            break
        elif not sticks:
            break
    sticks.append(tmp)

print(len(sticks))