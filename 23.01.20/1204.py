# 최빈수 구하기
from collections import Counter
T = int(input())
for index in range(T):
    t = input()
    most = []
    scores = Counter(list(map(int, input().split())))
    for score in scores:
        if scores[score] == max(scores.values()):
            most.append(score)

    print(f'#{t} {max(most)}')