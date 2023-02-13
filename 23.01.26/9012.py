# 괄호
for t in range(int(input())):
    pars = input()
    check = []
    if pars.count('(') != pars.count(')'):
        print('NO')
    else:
        for par in pars:
            if par == '(':
                check.append(par)
            else:
                if '(' in check:
                    check.pop()
        if len(check) == 0:
            print('YES')
        else:
            print('NO')