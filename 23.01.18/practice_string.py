# 2789. 유학금지
string = input()
new_s = ''
for elem in string:
    if elem not in 'CAMBRIDGE':
        new_s += elem
print(new_s)

# 2675. 문자열 반복
T = int(input())
for t in range(T):
    new_s = ''
    r, s = input().split()
    for elem in s:
        new_s += elem * int(r)
    print(new_s)

# 109878. 팰린드롬인지 확인하기
string = input()
if string == string[::-1]:
    print(1)
else:
    print(0)

# 17249. 태보태보 총난타(1)
tb = input()
cnt = 0 
aft = []
for elem in tb:
    if elem == '@':
        cnt += 1
    elif elem == '(':
        aft.append(cnt)
        cnt = 0
aft.append(cnt)
print(*aft)

# 17249. 태보태보 총난타(2)
TB = input().split('(')
for elem in TB:
    print(elem.count('@'), end='')

# 2941. 크로아티아 알파벳
cro = input()
cro_l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for cro_a in cro_l:
    cro = cro.replace(cro_a, '!')
print(len(cro))

# 10809. 알파벳 찾기
s = input()
alph = 'abcdefghijklmnopqrstuvwxyz'
s_l = []
for al in alph:
    if al in s:
        s_l.append(s.index(al))
    else:
        s_l.append(-1)
print(*s_l)