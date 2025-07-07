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
                task = dict(text=text, status=False)
                self.tasks.append(task)
            else:
                with open(self.filename, 'w', encoding='utf-8') as file:
                    json.dump(self.tasks, file, ensure_ascii=False, indent=2)

        def read_list(self):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.tasks = json.load(file)
                for i, dict_task in enumerate(self.tasks, 1):
                    print(f'{i}) {dict_task.get('text')} статус: {dict_task.get('status')}')

        def delete_task(self):
            pass

        def task_completed(self):
            pass

    my_todo = ToDoList()
    my_todo.create_task_list()
    my_todo.read_list()


if __name__ == "__main__":
    main()
