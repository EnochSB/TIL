# 신용카드 만들기1
T = int(input())
for t in range(1, T+1):
    card = list(map(int, input().split()))
    sixteen = 0
    for index in range(15):
        if index % 2 == 0:
            sixteen += 2 * card[index]
        else:
            sixteen += card[index]
    sixteen = (10 - sixteen % 10) % 10
    print(f'#{t} {sixteen}')