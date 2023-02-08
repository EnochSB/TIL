# 신용카드 만들기 2
T = int(input())
for t in range(1, T+1):
    card = input().replace('-', '')
    can = 0
    if card[0] in '34569':
        can = 1
    if len(card) != 16:
        can = 0
    print(f'#{t} {can}')