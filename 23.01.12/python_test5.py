# 새로운 불면증 치료법
T = int(input())
for t in range(1, T+1):
    num_list = list(range(10))
    N = int(input())
    n = 1
    while num_list != []:
        result = N * n
        for elem in str(result):
            if int(elem) in num_list:
                num_list.remove(int(elem))
        n+=1
    print(f'#{t} {result}')