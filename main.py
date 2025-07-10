import os
import json


class ToDoList:
    def __init__(self, tasks=None, filename='list.json'):
        self.tasks = tasks if tasks is not None else []
        self.filename = filename

    def load_tasks(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=2)

    def create_task_list(self):
        print(
            'Чтобы создать лист задач нажмите любую клавишу. Для выхода введите: exit')
        while (text := input('Введите задачу: ')) != 'exit':
            task = dict(text=text.capitalize(), status='не завершена')
            self.tasks.append(task)
        else:
            self.save_tasks()

    def add_task(self):
        text = input('Введите задачу: ')
        task = dict(text=text.capitalize(), status='не завершена')
        self.tasks.append(task)
        self.save_tasks()

    def read_list(self):
        self.load_tasks()
        if len(self.tasks) == 0:
            print('Список задач пуст')
        else:
            for i, dict_task in enumerate(self.tasks, 1):
                print(
                    f'{i}) {dict_task.get('text')} статус: {dict_task.get('status')}')

    def delete_task(self):
        task_to_be_deleted = int(input(
            'Введите номер задачи для удаления: '))
        self.load_tasks()

        i = 0
        while i < len(self.tasks):
            if i == task_to_be_deleted - 1:
                del self.tasks[i]
                print('Задача удалена')
                break
            else:
                i += 1
        else:
            print('Задача в списке не найдена')
        self.save_tasks()

    def task_completed(self):
        task_completed = int(input(
            'Введите номер завершённой задачи: '))
        self.load_tasks()
        i = 0
        while i < len(self.tasks):
            if i == task_completed - 1:
                self.tasks[i]['status'] = 'завершена'
                print('Задача отмечена, как выполненная')
                break
            else:
                i += 1
        else:
            print('Задача в списке не найдена')
        self.save_tasks()

    def menu(self):

        comands = {'1': self.create_task_list, '2': self.add_task, '3': self.read_list,
                   '4': self.task_completed, '5': self.delete_task, '6': exit}

        print('''===== To-Do List Menu =====
1. Создать список задач
2. Добавить задачу
3. Вывести список задач
4. Отметить задачу как выполненную
5. Удалить задачу
6. Выйти
''')
        while (comand := input()) != '6':
            if comand not in comands:
                print('Некорректный ввод')
            else:
                comands[comand]()


def main():

    my_todo = ToDoList()
    my_todo.menu()


if __name__ == "__main__":
    main()
