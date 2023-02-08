# 평균 점수
import statistics
scores = []
for stu in range(5):
    score = int(input())
    if score < 40:
        score = 40
    scores.append(int(score))
print(statistics.mean(scores))