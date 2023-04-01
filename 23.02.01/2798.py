# 블랙잭
n, m = map(int, input().split())
cards = list(map(int, input().split()))
jack = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] <= m:
                jack.add(cards[i] + cards[j] + cards[k])
print(max(jack))