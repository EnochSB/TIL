# 다이얼
gmom = input()
time = 0
for char in gmom:
    if ord(char) < 83:
        num = (ord(char)+1) //3 -20
    elif ord(char) < 90:
        num = (ord(char)) //3 -20
    else:
        num = 9
    time += num + 1
print(time)