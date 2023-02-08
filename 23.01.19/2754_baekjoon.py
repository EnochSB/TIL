# 학점계산
grade = input()
score = 69.0 - ord(grade[0])
if len(grade) == 1:
    score = 0.0
elif grade[1] == '-':
    score -= 0.3
elif grade[1] == '+':
    score += 0.3
print(score)