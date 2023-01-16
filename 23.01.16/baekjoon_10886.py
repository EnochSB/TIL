# 0 = not cute / 1 = cute
n = int(input())
cute = 0
n_cute = 0
for vote in range(n):
    if input() == '1':
        cute += 1
    else:
        n_cute += 1

if cute > n_cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')