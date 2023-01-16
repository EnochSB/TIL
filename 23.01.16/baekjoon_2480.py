# 주사위 세개
dices = list(map(int, input().split()))
for dice in dices:
    if dices.count(dice) == 3:
        print(10000 + 1000 * dice)
        break
    elif dices.count(dice) == 2:
        print(1000 + 100 * dice)
        break
    else:
        if dice == dices[-1]:
            print(max(dices) * 100)