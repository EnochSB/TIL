# 소득불균형
T = int(input())
for t in range(1, T+1):
    n = int(input())
    incoms = list(map(int, input().split()))
    avg = sum(incoms) / n
    down = []
    for incom in incoms:
        if incom <= avg:
            down.append(incom)
    print(f'#{t} {len(down)}')