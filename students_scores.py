students_scores = [1, 21, 19, 6, 5]

scores_sum = 0
for score in students_scores:
        scores_sum +=score
        print(scores_sum)

scores_avg = scores_sum / len(students_scores)
print(f"Средняя оценка {scores_avg}")
