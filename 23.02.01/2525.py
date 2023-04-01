# 오븐 시계
a, b = map(int, input().split())
c = int(input())
h, m = divmod(c, 60)
if b + m >= 60:
    if a + h >= 23:
        a = a + h - 23
        b = b + m - 60
    else:
        a = a + h + 1
        b = b + m - 60
else:
    if a + h >= 24:
        a = a + h -24
        b = b + m
    else:
        a = a + h
        b = b + m

print(a, b)