# 회사에 있는 사람
n = int(input())
now = {}
for index in range(n):
    name, info = input().split()
    now[name] = info

for key in sorted(now, reverse=True):
    if now[key] == 'enter':
        print(key)