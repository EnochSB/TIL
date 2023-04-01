# 직사각형 네개의 합집합의 면적 구하기

matrix = [[0]*100 for _ in range(100)]
for _ in range(4):
    sqr = list(map(int, input().split()))
    for i in range(sqr[0]-1, sqr[2]-1):
        for j in range(sqr[1]-1, sqr[3]-1):
            matrix[i][j] = 1
print(sum(map(sum, matrix)))