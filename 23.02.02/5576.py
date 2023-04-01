# 콘테스트
wuni = [int(input()) for _ in range(10)]
kuni = [int(input()) for _ in range(10)]

wtop = sorted(wuni, reverse=True)[:3]
ktop = sorted(kuni, reverse=True)[:3]

print(sum(wtop), sum(ktop))