import os
import json


def main():
    class ToDoList:
        def __init__(self, tasks=None, filename='list.json'):
            self.tasks = tasks if tasks is not None else []
            self.filename = filename

        def create_task_list(self):
            print(
                'Чтобы создать лист задач нажмите любую кнопку. Для выхода введите: exit')
            next_step = input()
            if next_step == 'exit':
                exit()
            else:
                self.add_task()

        def add_task(self):
            while (text := input('Введите задачу: ')) != 'exit':
                task = dict(text=text.capitalize(), status='не завершена')
                self.tasks.append(task)
            else:
                with open(self.filename, 'w', encoding='utf-8') as file:
                    json.dump(self.tasks, file, ensure_ascii=False, indent=2)

        def read_list(self):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.tasks = json.load(file)
                if len(self.tasks) == 0:
                    print('Список задач пуст')
                else:
                    for i, dict_task in enumerate(self.tasks, 1):
                        print(
                            f'{i}) {dict_task.get('text')} статус: {dict_task.get('status')}')

        def delete_task(self):
            task_to_be_deleted = input(
                'Введите задачу для удаления: ').capitalize()
            with open(self.filename, 'r', encoding='utf-8') as input_file:
                self.tasks = json.load(input_file)

            i = 0
            while i < len(self.tasks):
                if self.tasks[i]['text'] == task_to_be_deleted:
                    del self.tasks[i]
                    print('Задача удалена')
                    break
                else:
                    i += 1
            else:
                print('Задача в списке не найдена')

            with open(self.filename, 'w', encoding='utf-8') as output_file:
                json.dump(self.tasks, output_file,
                          ensure_ascii=False, indent=2)

        def task_completed(self):
            task_completed = input(
                'Введите завершённую задачу: ').capitalize()
            with open(self.filename, 'r', encoding='utf-8') as input_file:
                self.tasks = json.load(input_file)
            i = 0
            while i < len(self.tasks):
                if self.tasks[i]['text'] == task_completed:
                    self.tasks[i]['status'] = 'завершена'
                    print('Задача отмечена, как выполненная')
                    break
                else:
                    i += 1
            else:
                print('Задача в списке не найдена')

            with open(self.filename, 'w', encoding='utf-8') as output_file:
                json.dump(self.tasks, output_file,
                          ensure_ascii=False, indent=2)

        def menu(self):

            comands = {1: self.create_task_list, 2: self.add_task, 3: self.read_list,
                       4: self.task_completed, 5: self.delete_task, 6: exit}

            print('''===== To-Do List Menu =====
1. Создать список задач
2. Добавить задачу
3. Вывести список задач
4. Отметить задачу как выполненную
5. Удалить задачу
6. Выйти
''')
            while (waiting_for_command := int(input())) != 6:
                comands[waiting_for_command]()

    my_todo = ToDoList()
    my_todo.menu()


if __name__ == "__main__":
    main()
