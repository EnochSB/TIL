# 더하기 싸이클
n = input()
cnt = 0
if len(n) == 1:
    n = '0' + n
cal = n
while True:
    cal = cal[1] + str(int(cal[0]) + int(cal[1]))[-1]
    cnt +=1
    if cal == n:
        break
print(cnt)