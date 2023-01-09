# 문제 1
str_in = input('문자열을 입력하세요 > ')
for i in range(len(str_in)):
    if str_in[i] == 'e':
        print(i)
        break
    elif 'e' not in str_in:
        print(-1)
        break

# 문제 2
str_list = list(input('문자열을 입력하세요 > ').split())
str_dict = {}
for elem in str_list:
    str_dict[elem] = str_dict.get(elem, 0) + 1
for key in str_dict:
    print(key, str_dict[key])

# 문제 3
str_in = input('문자열을 입력하세요 > ')
new_str = ''
for elem in str_in:
    if elem != 'e':
        new_str += elem
    else:
        continue
print(new_str)

# 문제 4
str_in, alph_in = input('문자열을 입력하세요 > ').split()
cnt = 0
for elem in str_in:
    if elem == alph_in:
        cnt += 1
print(cnt)

# 문제 5
a, b, c = input('양의 정수를 입력하세요 > ').split()
print(a, b, c, sep="-")

# 문제 6
num = int(input('양의 정수를 입력하세요 > '))
num_di = []
sum_num = 0
if num >= 0:
    while num != 0:
        num_di.append(num % 10)
        num //= 10
    for i in num_di:
        sum_num += i
    print(sum_num)
else:
    print(-1)