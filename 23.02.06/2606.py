# 바이러스
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
infect = [None] + [False]*n

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def virus(start):
    stack = [start]
    infect[start] = True

    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not infect[adj]:
                infect[adj] = True
                stack.append(adj)
    return print(infect.count(True)-1)

virus(1)