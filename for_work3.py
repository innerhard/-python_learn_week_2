students_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                   {'school_class': '2a', 'scores': [3, 4, 4, 5, 3]},
                   {'school_class': '3a', 'scores': [3, 4, 4, 5, 3]}]
summ_class = 0
summ_school = 0
children_number = 0

for key in students_scores:
    for summ in key['scores']:
        summ_class += summ
        children_number += 1
    print(f"Средняя оценка класса {key['school_class']} равна \
            {summ_class/len(key['scores'])}")
    summ_school += summ_class
    summ_class = 0
print(f"Средняя оценка всех классов {round(summ_school/children_number,1)}")
