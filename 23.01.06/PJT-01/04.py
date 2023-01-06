dict_fruit = {}
with open('data/fruits.txt') as f:
    for i in f.readlines():
        if i[0:len(i)-2] not in dict_fruit:
            dict_fruit[i[0:len(i)-2]] = 1
        else:
            dict_fruit[i[0:len(i)-2]] += 1

with open('04.txt', 'w') as f:
    for i in dict_fruit:
        f.write(i + ' ' + str(dict_fruit[i]) + '\n')