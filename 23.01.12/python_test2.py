# 연월일 달력
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
list_31 = [1, 3, 5, 7, 8, 10, 12]
list_30 = [4, 6, 9, 11]
new_date = ''
for t in range(1, T+1):
    date = input()
    if int(date[4:6]) in list_31:
        if int(date[6:8]) <= 31:
            new_date += date[0:4] + '/' + date[4:6] + '/' + date[6:8]
            print(f'#{t} {new_date}')
            new_date = ''
        else:
            print(f'#{t} {-1}')
    elif int(date[4:6]) in list_30:
        if int(date[6:8]) <= 30:
            new_date += date[0:4] + '/' + date[4:6] + '/' + date[6:8]
            print(f'#{t} {new_date}')
            new_date = ''
        else:
            print(f'#{t} {-1}')
    elif int(date[4:6]) == 2:
        if int(date[6:8]) <= 28:
            new_date += date[0:4] + '/' + date[4:6] + '/' + date[6:8]
            print(f'#{t} {new_date}')
            new_date = ''
        else:
            print(f'#{t} {-1}')
    else:
        print(f'#{t} {-1}')