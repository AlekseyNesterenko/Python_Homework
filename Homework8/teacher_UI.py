import Data_work

def add_student():
    name = input("Введите имя: ")
    surname = input("Введите Фамилию: ")
    group = input("Введите группу: ")
    return Student(name, surname, group)


def add_score(student):
    subject = input("Введите предмет: ")
    score = input("Введите оценку: ")
    student.add_score(subject, score)


def input_action():
    print("| Добавить ученика: 1 | "
        "Добавить оценку: 2 | "
        "Сохранить базу и выйти: 3 | "
        "Вывести данные: 4 | ")
    action = int(input("Введите действие: "))
    if action == '1':
        add_student()
    if action == '2':
        add_score()
    if action == '3':
            pass
    if action == '4':
            Data_work.load_db()
            


def print_data(data):
    sep = max(len(str(i)) for i in data) * "-"
    print(sep)
    for value in data:
        print(value)
    print(sep)