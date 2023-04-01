# 누울 자리를 찾아라
n = int(input())
room = [input() + 'X' for _ in range(n)]
room.append('X' * (n+1))
hor = 0
ver = 0

for i in range(n+1):
    spc = 0
    for j in range(n+1):
        if room[i][j] == '.':
            spc += 1
        else:
            if spc >= 2:
                hor += 1
            spc = 0

for j in range(n+1):
    spc = 0
    for i in range(n+1):
        if room[i][j] == '.':
            spc += 1
        else:
            if spc >= 2:
                ver += 1
            spc = 0

print(hor, ver)