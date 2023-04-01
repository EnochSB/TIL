# 행복한지 슬픈지
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

string = input()

hcnt = string.count(':-)')
scnt = string.count(':-(')

if hcnt == scnt:
    if hcnt == 0:
        print('none')
    else:
        print('unsure')
elif hcnt > scnt:
    print('happy')
else:
    print('sad')