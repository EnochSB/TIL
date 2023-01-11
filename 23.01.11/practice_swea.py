# 문제 1. 신문 헤드라인
string = input()
print(string.upper())

# 문제 2. N줄 덧셈
n = int(input())
print(sum(range(1, n+1)))

# 문제 3. 1대1 가위바위보
class player:
    def __init__(self, name, wep):
        self.name = name
        self.wep = wep
    def __gt__(self, other):
        if self.wep%3 == (other.wep+1)%3:
            return self
        else:
            return other
    def __str__(self):
        return self.name
a, b = map(int, input().split())
p1 = player('A', a)
p2 = player('B', b)
print(p1 > p2)

# 문제 4. 대각선 출력하기
sl = 5
string = list('+'*sl)
for i in range(sl):
    string[i] = '#'
    print(*string, sep='')
    string = list('+'*sl)

# 문제 5. 자릿수 더하기
num = input()
result = 0
for i in num:
    result += int(i)
print(result)

# 문제 6. 더블더블
num = int(input())
for i in range(num+1):
    print(2**i, end=' ')