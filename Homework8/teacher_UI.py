from Data_work import add_student, add_score

def add_student():
    surname = input("Введите Фамилию: ")
    name = input("Введите имя: ")
    group = input("Введите класс: ")
    add_student([surname, name, group])


def add_score():
    last_name = input("Введите фамилию ученика: ")
    subject = input("Введите предмет: ")
    score = input("Введите оценку или оценки через пробел: ").split()
    add_score(last_name, subject, score)