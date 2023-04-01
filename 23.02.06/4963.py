# 섬의 개수
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def search(w, h):
    cnt = 0
    for x in range(h):
            for y in range(w):
                if not check[x][y]:
                    cnt += dfs(x, y)

    return print(cnt)

def dfs(x, y):
    if sea_map[x][y] == 0:
        return 0
    if check[x][y]:
        return 0

    check[x][y] = True

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i] 
        if h > nx >=0 and w > ny >=0:
            if sea_map[nx][ny] == 1:
                dfs(nx, ny)

    return 1

while True:
    try:
        w, h = map(int, input().split())
        if w == h == 0:
            break

        check = [[False]*(w) for _ in range(h)]
        sea_map = [list(map(int, input().split())) for _ in range(h)]

        search(w, h)
    
    except:
        break