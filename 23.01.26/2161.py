# 카드1
cards = list(range(1, int(input()) + 1))
while len(cards)>1:
    print(cards.pop(0), end=' ')
    cards.append(cards.pop(0))
print(*cards)

# pop(0)은 비효율적이라 deque을 쓰는것이 좋다.