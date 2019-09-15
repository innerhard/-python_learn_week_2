AGE = input("Сколько тебе лет салага???")

def get_you_age(age):
    age = int(age)
    if age > 0 and age <=7:
        print("Ты должен быть в детском саду тебе " + str(age))
    elif age > 7 and age <=15:
        print("Ты должен быть в школе тебе " + str(age))
    elif age > 15 and age <=21:
        print("Ты должен быть в вузе тебе " + str(age))
    elif age > 21:
        print("Ты должен работать тебе " + str(age))
    else:
        print("Видимо ты не родился или ты вообще неторт")
get_you_age(AGE)