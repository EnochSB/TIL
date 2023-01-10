# 문제 1
num = int(input('정수를 입력하세요 > '))
print(num)

# 문제 2
words = input('문자열을 입력하세요 > ').split()
print(*words)

# 문제 3
t_case = int(input('테스트 케이스 수를 입력하세요 > '))
case_list = []
for i in range(t_case):
    case_list.append(int(input(f'테스트 케이스 {i +1} 입력 > ')))
print(*case_list, sep='\n')

# 문제 4
num_list = list(map(int, input('여러 정수를 입력하세요 > ').split()))
print(*num_list)

# 문제 5
num1, num2 = map(int, input('두 개의 정수를 입력하세요 > ').split())
print(num1, num2)

# 문제 6
string = input('문장을 입력하세요 > ').split()
print(*string)

# 문제 7
t_case = int(input('테스트 케이스 수를 입력하세요 > '))
num_dict = {}
for i in range(t_case):
    num_dict[i] = list(map(int, input(f'정수 3개를 입력하세요({i+1}/{t_case})> ').split()))
for key in num_dict:
    print(*num_dict[key])

# 문제 8
t_case = int(input('테스트 케이스 수를 입력하세요 > '))
num_dict = {}
for i in range(t_case):
    num_dict[i] = list(map(int, input(f'정수 여러 개를 입력하세요({i+1}/{t_case})> ').split()))
for key in num_dict:
    print(*num_dict[key])
