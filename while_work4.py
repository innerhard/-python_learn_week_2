def discounted(price, discount, max_discount=20):

    while price != "exit" or discount != "exit":

        try:
            price = abs(float(price))
            discount = abs(float(discount))
            max_discount = abs(float(max_discount))
            if max_discount > 99:
                raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                return print(price)
            else:
                return print(price - (price * discount / 100))
        except ValueError:
            print("Вы ввели не корректные данные")
            price = input("Введите значение цены ")
            discount = input("Введите значение и скидки ")


discounted(price=input("Введите значение цены "),
           discount=input("Введите значение и скидки "))
