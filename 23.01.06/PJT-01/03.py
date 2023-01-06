berry = []
with open('data/fruits.txt') as f:
    for i in f.readlines():
        if 'berry' in i[-6:-1]:
            if i in berry:
                continue
            else:
                berry.append(i)

with open('03.txt', 'w') as f:
    f.write(str(len(berry)) + '\n')
    for i in berry:
        f.write(i)