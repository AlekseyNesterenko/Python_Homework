import teacher_UI, student_UI

def controller():
    while True:
        print("Учитель: 1 \nУченик: 2")
        action = input("Выберите действие: ")
        if action== "1":
            teacher_UI.input_action()
        elif action == "2":
            student_UI.student()
        else:
            print("Неверный ввод! Попробуйте еще раз.")
            controller()
