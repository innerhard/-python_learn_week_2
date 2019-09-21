from datetime import datetime


def ask_user():
    ask_me = input("Поговорим?")
    question_data = {"Как дела?": "Хорошо",
                     "Что делаешь?": "Программирую",
                     "Который час?": f"{datetime.now()}"}
    while ask_me != "Пока":
        try:
            print(question_data[ask_me])
            ask_me = input()
        except KeyError:
            print("Спроси что-нибудь другое...Или скажи Пока")
            ask_me = input()


ask_user()
