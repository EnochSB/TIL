# 1번
num = int(input('정수를 입력하세요 > '))
if num > 0:
    print('True')
else:
    print('False')

# 2번
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
if num1 == num2:
    print('False')
elif num1 > num2:
    print(num1)
else:
    print(num2)

# 3번
num = int(input('정수를 입력하세요 > '))
if num >= 10:
    print('False')
elif num > 1:
    print('True')
else:
    print('False')

# 4번
num = int(input('정수를 입력하세요 > '))
if num % 2:
    print('False')
else:
    print('True')

# 5번
num = int(input('정수를 입력하세요 > '))
if num > 100:
    print('에러')
elif num >= 60:
    print('합격')
elif num >= 0:
    print('불합격')
else:
    print('에러')

# 6번
str = input('문자열을 입력하세요 > ')
for i in range(-1, -len(str)-1, -1):
    print(str[i])

# 7번
n1 = int(input('첫 번째 정수를 입력하세요 > '))
n2 = int(input('두 번째 정수를 입력하세요 > '))
if n1-1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
elif n1+1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
elif n1 < n2:
    for i in range(n1+1, n2):
        print(i)
elif n1 > n2:
    for i in range(n2+1, n1):
        print(i)
else:
    print('False')

# 7번-1
n1 = int(input('첫 번째 정수를 입력하세요 > '))
n2 = int(input('두 번째 정수를 입력하세요 > '))
if n1 == n2:
    print("False")
elif n1 + 1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
elif n1 - 1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
else:
    for i in range(min(n1, n2) + 1, max(n1, n2)):
        print(i)

# 8번
n1 = int(input('첫 번째 정수를 입력하세요 > '))
n2 = int(input('두 번째 정수를 입력하세요 > '))

if n1-1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
elif n1+1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
elif n1 < n2:
    for i in range(-1, n1-n2, -1):
        tmp = range(n1+1, n2)
        print(tmp[i], end=" ")
elif n1 > n2:
    for i in range(-1, n2-n1, -1):
        tmp = range(n2+1, n1)
        print(tmp[i], end=" ")
else:
    print('False')

# 8번-1
n1 = int(input('첫 번째 정수를 입력하세요 > '))
n2 = int(input('두 번째 정수를 입력하세요 > '))

if n1-1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
elif n1+1 == n2:
    print('두 수 사이에는 정수가 존재하지 않습니다.')
elif n1 < n2:
    for i in range(n2-1, n1, -1):
        print(i, end=" ")
elif n1 > n2:
    for i in range(n1-1, n2, -1):
        print(i, end=" ")
else:
    print('False')

# 9번
n = int(input('정수를 입력하세요 > '))
if n > 0:
    for i in range(1, n):
        if i % 2 == 0:
            continue
        print(i)
else:
    print('False')

# 10번
for m in range(2, 10):
    for n in range(2, 10):
        print(f"{m} X {n} = {m * n}")