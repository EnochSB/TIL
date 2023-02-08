# 나무 조각
wood = list(map(int, input().split()))

while True:
    for i in range(4):
        if wood[i] > wood[i+1]:
            tmp = wood[i]
            wood[i] = wood[i+1]
            wood[i+1] = tmp
            print(*wood)
    if wood == [1, 2, 3, 4, 5]:
        break