import sys
from todolist import ToDoList as td


def main():
    todo = td()

    def add_task():
        while True:
            task = input('Введите задачу, либо exit для выхода: \n')
            if task == 'exit':
                break
            if not task.strip():
                print('Задача не можкт быть пустой')
                continue
            todo.add_task(task)

    def edit_task():
        try:
            task_number = int(input('Введите номер задачи: \n'))
            text = input('Введите текст задачи: \n')
            if todo.edit_task(task_number, text):
                print('Задача отредактирована')
            else:
                print('Нет задачи с таким номером')
        except ValueError:
            print('Некорректный ввод')

    def output_tasks():
        tasks = todo.read_list()
        if tasks == []:
            print('Список задач пуст')
        else:
            print('===== Список задач =====')
            for i, task in enumerate(tasks, 1):
                status = "✓" if task['status'] else " "
                print(f"{i}) [{status}] {task['text']}")
            print()

    def complete_task():
        try:
            task_number = int(input('Введите номер задачи: \n'))
            if todo.task_completed(task_number):
                print('Задача завершена')
            else:
                print('Нет задачи с таким номером')
        except ValueError:
            print('Некорректный ввод')

    def delete_task():
        try:
            task_number = int(input('Введите номер задачи: \n'))
            if not (1 <= task_number <= len(todo.read_list())):
                print('Нет задачи с таким номером')
                return
            confirm = input('Вы уверены? (Да/Нет): ')
            if confirm == 'Да':
                if todo.delete_task(task_number):
                    print('Задача удалена')
            else:
                print('Удаление отменено')
        except ValueError:
            print('Некорректный ввод')

    def show_menu():
        print('''===== To-Do List Menu =====
1. Добавить задачу
2. Редактировать задачу
3. Вывести список задач
4. Отметить задачу как выполненную
5. Удалить задачу
6. Выйти
        ''')

    while True:
        show_menu()

        comands = {'1': add_task, '2': edit_task, '3': output_tasks,
                   '4': complete_task, '5': delete_task, '6': sys.exit}
        comand = input()
        if comand not in comands:
            print('Некорректный ввод')
        else:
            comands[comand]()


if __name__ == "__main__":
    main()
