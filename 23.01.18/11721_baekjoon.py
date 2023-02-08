# 열 개씩 끊어 출력하기
s = input()
for i in range(1, len(s)+1):
    if i % 10 == 0:
        print(''.join(s[i-10:i]))
    elif i == len(s):
        print(''.join(s[i-(i%10):i]))