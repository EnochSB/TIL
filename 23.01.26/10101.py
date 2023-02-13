# 삼각형 외우기
angs = []
for i in range(3):
    angs.append(int(input()))
if sum(angs) != 180:
    print('Error')
else:
    for ang in angs:
        if angs.count(ang) == 3:
            print('Equilateral')
            break
        elif angs.count(ang) == 2:
            print('Isosceles')
            break
        elif angs.index(ang) == 2:
            print('Scalene')