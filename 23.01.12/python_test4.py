# 간단한 N의 약수
N = int(input())
num_list = []
print(*[n for n in range(1, N+1) if N % n == 0])