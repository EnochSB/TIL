# 단어 나누기
word = input()
nwrord = set()
for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        for k in range(j+1, len(word)):
            tmp = []
            tmp.append(word[0:j])
            tmp.append(word[j:k])
            tmp.append(word[k:])

            nwrord.add(''.join(list(map(lambda x: x[::-1], tmp))))
print(sorted(nwrord)[0])