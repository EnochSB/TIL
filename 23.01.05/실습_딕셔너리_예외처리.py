# 문제 1
str = input('문자열을 입력하세요 > ')
e_cnt = 0
for element in str:
    if element == 'e':
        e_cnt += 1
print(e_cnt)

# 문제 2
str = input('문자열을 입력하세요 > ')
vowel_count = 0
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for element in str:
    if element in vowel:
        vowel_count += 1
print(vowel_count)

# 문제 3
dict_variable = {
    "이름": "정우영",
    "생년": "20000101",
    "회사": "하이퍼그로스",
}
import datetime
born_year = int(dict_variable["생년"][0:4])
this_year = int(datetime.date.today().year)
dict_variable['나이'] = f'{this_year - born_year + 1}세'
print(f'나이 : {dict_variable["나이"]}')

# 문제 4
dict_variable = {}
dict_variable['이름'] = input('이름을 입력하세요 > ')
dict_variable['전화번호'] = input('전화번호를 입력하세요 > ')
dict_variable['거주지'] = input('거주지를 입력하세요 > ')

print(dict_variable)
for i in dict_variable:
    print(i, ":", dict_variable[i])

# 문제 5
dict_variable = {}
dict_inner = {}
dict_variable[input('이름을 입력하세요 > ')] = dict_inner
dict_inner['전화번호'] = input('전화번호를 입력하세요 > ')
dict_inner['이메일'] = input('이메일을 입력하세요 > ')
dict_inner['거주지'] = input('거주지를 입력하세요 > ')
print(dict_variable)

# 문제 6
str = input('문자열을 입력하세요 > ')
dict_variable = {}
for element in str:
    dict_variable[element] = 0
for element in str:
    dict_variable[element] += 1
for key in dict_variable:
    print(key, dict_variable[key])