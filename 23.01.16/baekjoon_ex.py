# 1번
A, B = map(int, input().split())
print(A + B)

# 2번
a = int(input())
b = int(input())
print(a + b)

# 3번
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a + b)

# 4번
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split(','))
    print(a + b)

# 5번
import sys
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {a + b}")

# 6번
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a + b}')