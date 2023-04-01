# 박스
for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = [input().split() for _ in range(m)]
    move = 0
    for j in range(n):
        tmp = 0
        cnt = 0
        for i in range(m):
            if grid[i][j] == '1':
                tmp =  tmp + m - 1 - i - cnt
                cnt += 1
        move += tmp
    print(move)