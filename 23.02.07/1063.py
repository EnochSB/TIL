# 킹
import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

def coor(start):
    x = 8 - int(start[1])
    y = ord(start[0]) - 65
    return (x, y)

def loca(x, y):
    finish = chr(65+y) + str(8-x)
    return finish

move = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1),
}

k, s, n = input().split()
kx, ky = coor(k)
sx, sy = coor(s)

for _ in range(int(n)):
    i, j = move[input()]
    if 0 <= kx + i < 8 and 0 <= ky + j < 8:
        kx, ky = kx + i, ky + j

        if kx == sx and ky == sy:
            if 0 <= sx + i < 8 and 0 <= sy + j < 8:
                sx, sy = sx + i, sy + j
            else:
                kx, ky = kx - i, ky - j

print(loca(kx, ky))
print(loca(sx, sy))