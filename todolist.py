import os
import json


class ToDoList:
    """
    Класс для управления списком задач.

    Attributes:
        tasks (list): Список задач.
        filename (str): Имя файла для хранения задач.

    Methods:
        load_tasks(): Загружает список задач из файла.
        save_tasks(): Сохраняет список задач в файл.
        add_task(text): Добавляет новую задачу.
        edit_task(task_number, new_text): Редактирует выбранную задачу.
        read_list(): Возвращает список задач.
        delete_task(task_number): Удаляет задачу по номеру.
        task_completed(task_number): Отмечает задачу, как выполненную.
    """

    def __init__(self, tasks=None, filename='list.json'):
        self.tasks = tasks if tasks is not None else []
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        """
        Загружает список задач из файла.

        Args:
            Нет

        Returns:
            None
        """
        if not os.path.exists(self.filename):
            self.tasks = []
            return
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)

    def save_tasks(self):
        """
        Сохраняет список задач в файл.

        Args:
            Нет

        Returns:
            None
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=2)

    def add_task(self, text):
        """
        Добавляет новую задачу в список и сохраняет задачу в файл.

        Args:
            text (str): Текст задачи.

        Returns:
            None
        """
        task = dict(text=text, status=False)
        self.tasks.append(task)
        self.save_tasks()

    def edit_task(self, task_number, new_text):
        """
        Редактирует выбранную задачу из списка и сохраняет задачу в файл.

        Args:
            task_number (int): Номер задачи.
            new_text (str): Текст задачи.

        Returns:
            True, если задача отредактирована.
            False в остальных случаях.
        """
        if not self.tasks or not (1 <= task_number <= len(self.tasks)):
            return False
        self.tasks[task_number - 1]['text'] = new_text
        self.save_tasks()
        return True

    def read_list(self):
        """
        Возвращает список задач.

        Args:
            Нет.

        Returns:
            tasks
        """
        return self.tasks

    def delete_task(self, task_number):
        """
        Удаляет выбранную задачу из списка и сохраняет задачу в файл.

        Args:
            task_number (int): Номер задачи.

        Returns:
            True, если задача удалена.
            False в остальных случаях.
        """
        if not self.tasks or not (1 <= task_number <= len(self.tasks)):
            return False
        del self.tasks[task_number - 1]
        self.save_tasks()
        return True

    def task_completed(self, task_number):
        """
        Изменяет статус выбранной задачи из списка и сохраняет задачу в файл.

        Args:
            task_number (int): Номер задачи.
            new_text (str): Текст задачи.

        Returns:
            True, если статус задачи изменён.
            False в остальных случаях.
        """
        if not self.tasks or not (1 <= task_number <= len(self.tasks)):
            return False
        self.tasks[task_number - 1]['status'] = True
        self.save_tasks()
        return True
