# 점수계산
# n = int(input())
# ox = list(map(int, input().split()))
# scs = {}
# j = 1
# for i in ox:
#     if i == 1:
#         if j not in scs:
#             scs[j] = [i]
#         else:
#             scs[j].append(i)
#     else:
#         j += 1
# result = 0
# for sc in scs.values():
#     result += sum(range(1, len(sc)+1))
# print(result)

n = int(input())
ox = list(map(int, input().split()))
sc = 0
cnt = 0
for i in range(n):
    if ox[i] == 1:
        sc += ox[i] + cnt
        cnt += 1
    else:
        cnt = 0

print(sc)