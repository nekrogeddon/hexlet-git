HELP = """
help - показать справку по программе
add - добавить задачу в список (название задачи пользователь вводит самостоятельно)
show - показать все добавленные задачи"""

tasks = []

command = input("Введите команду (help - показать справку): ")
if command == "help":
    print(HELP)
elif command == "show":
    print(tasks)
elif command == "add":
    task = input("Введите название задачи: ")
    tasks.append(task)
    print("Задача добавлена")
else:
    print("Неизвестная команда")