# 오르막길
n = input()
recod = list(map(int, input().split())) + [0]
uphil = [recod[0]]
size = 0

for i in range(1, len(recod)):
    if recod[i-1] < recod[i]:
        uphil.append(recod[i])
    else:
        if max(uphil) - min(uphil) > size:
            size = max(uphil) - min(uphil)
        uphil = [recod[i]]

print(size)