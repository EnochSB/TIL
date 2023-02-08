# 직사각형의 길이 찾기
T = int(input())
for t in range(1, T+1):
    rec = list(map(int, input().split()))
    for l in rec:
        if rec.count(l) == 3:
            print(f"#{t} {l}")
            break
        elif rec.count(l) == 1:
            print(f"#{t} {l}")
            break