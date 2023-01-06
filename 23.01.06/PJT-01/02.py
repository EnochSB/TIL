with open('data/fruits.txt') as f:
    line = f.readlines()
with open('02.txt', 'w') as f:
    f.write(str(len(line)))