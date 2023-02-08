# 문자열의 거울상
T = int(input())
bdpq = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
for t in range(1, T+1):
    mirror = ''
    string = input()
    for char in string[::-1]:
        mirror += bdpq[char]
    print(f'#{t} {mirror}')