import os
import sys
import json


class ToDoList:
    def __init__(self, tasks=None, filename='list.json'):
        self.tasks = tasks if tasks is not None else []
        self.filename = filename

    def load_tasks(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=2)

    def create_task_list(self):
        print(
            'Для выхода из режима ввода введите: exit')
        while (text := input('Введите задачу: ')) != 'exit':
            task = dict(text=text, status=False)
            self.tasks.append(task)
        else:
            self.save_tasks()
            self.read_list()

    def add_task(self):
        print(
            'Для выхода из режима ввода введите: exit')
        text = input('Введите задачу: ')
        if text == 'exit':
            return
        else:
            task = dict(text=text, status=False)
            self.tasks.append(task)
            self.save_tasks()
            self.read_list()

    def edit_task(self):
        pass

    def read_list(self):
        self.load_tasks()
        if len(self.tasks) == 0:
            print('Список задач пуст')
        else:
            print()
            print('===== Ваш список задач =====')
            for i, dict_task in enumerate(self.tasks, 1):
                print(
                    f'{i}) {dict_task.get('text')}  {'✓' if dict_task.get('status') == True else '✗'}')
            print()

    def delete_task(self):
        self.load_tasks()
        if not self.tasks:
            print('Список задач пуст')
            return
        try:
            task_to_be_deleted = int(
                input('Введите номер задачи для удаления: '))
            if 1 <= task_to_be_deleted <= len(self.tasks):
                confirm = input('Вы уверены? (Да/Нет): ')
                if confirm == 'Да':
                    del self.tasks[task_to_be_deleted - 1]
                    print('Задача удалена')
                    self.save_tasks()
                    self.read_list()
                else:
                    print('Задача не удалена')
                    self.read_list()
            else:
                print('Нет задачи с таким номером')
        except ValueError:
            print('Введите корректный номер задачи')

    def task_completed(self):
        self.load_tasks()
        if not self.tasks:
            print('Список задач пуст')
            return
        try:
            task_completed = int(input('Введите номер завершённой задачи: '))
            if 1 <= task_completed <= len(self.tasks):
                self.tasks[task_completed - 1]['status'] = True
                print('Задача отмечена, как выполненная')
                self.save_tasks()
                self.read_list()
            else:
                print('Нет задачи с таким номером')
        except ValueError:
            print('Введите корректный номер задачи')

    def menu(self):
        comands = {'1': self.create_task_list, '2': self.add_task, '3': self.read_list,
                   '4': self.task_completed, '5': self.delete_task, '6': sys.exit}
        # comand = input()
        while True:

            print('''===== To-Do List Menu =====
    1. Создать список задач
    2. Добавить задачу
    3. Вывести список задач
    4. Отметить задачу как выполненную
    5. Удалить задачу
    6. Выйти
    ''')
            comand = input()
            if comand not in comands:
                print('Некорректный ввод')
            else:
                comands[comand]()


def main():

    my_todo = ToDoList()
    my_todo.menu()


if __name__ == "__main__":
    main()
