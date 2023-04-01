# 가장 큰 금민수
n = int(input())

for num in reversed(range(n + 1)):
    minsu = True
    for dig in str(num):
        if dig in '47':
            continue
        else:
            minsu = False
            break
    if minsu:
        print(num)
        break