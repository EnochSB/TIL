# 나는 요리사다
chif = []
for i in range(1, 6):
    chif.append((i, sum(map(int, input().split()))))

print(*sorted(chif, key=lambda x: x[1], reverse=True)[0])