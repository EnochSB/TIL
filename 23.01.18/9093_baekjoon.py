# 단어 뒤집기
T = int(input())
for t in range(T):
    sen = input().split()
    n_sen = [word[::-1] for word in sen]
    print(*n_sen)