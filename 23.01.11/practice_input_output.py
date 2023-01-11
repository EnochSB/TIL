import sys
# 문제 1
sys.stdin = open('input1.txt', 'r')

num_list = map(int, input().split())
print(*num_list)

# 문제 2
sys.stdin = open('input2.txt', 'r')
str_list = input().split()
print(*str_list)

# 문제 3
sys.stdin = open('input3.txt', 'r')
t = int(input())
print(t)
for test_case in range(1, t+1):
    n = int(input())
    print(n)
    for input_line in range(1, n+1):
        print(int(input()))

# 문제 4
sys.stdin = open('input4.txt', 'r')
t = int(input())
print(t)
for test_case in range(1, t+1):
    n = int(input())
    print(n)
    for input_line in range(1, n+1):
        a, b = map(int, input().split())
        print(a, b)

# 문제 5
sys.stdin = open('input5.txt', 'r')
t = int(input())
print(t)
for test_case in range(1, t+1):
    n = int(input())
    print(n)
    for input_line in range(1, n+1):
        str_list = input().split()
        print(*str_list)

# 문제 6
sys.stdin = open('input6.txt', 'r')
t = int(input())
print(t)
for test_case in range(1, t+1):
    n = int(input())
    print(n)
    for input_line in range(1, n+1):
        num_list = map(int, input().split())
        print(*num_list)

# 문제 7
sys.stdin = open('input7.txt', 'r')
t, n = map(int, input().split())
print(t, n)
for test_case in range(1, t+1):
    for input_line in range(1, n+1):
        print(int(input()))

# 문제 8
sys.stdin = open('input8.txt', 'r')
t, n = map(int, input().split())
print(t, n)
for t_case in range(1, t+1):
    for in_line in range(1, n+1):
        a, b = map(int, input().split())
        print(a, b)

# 문제 9
sys.stdin = open('input9.txt', 'r')
t, n = map(int, input().split())
print(t, n)
for t_case in range(1, t+1):
    for in_line in range(1, n+1):
        num_list = map(int, input().split())
        print(*num_list)