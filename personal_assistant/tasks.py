import json
import pandas as pd
from datetime import datetime


class Task:
    def __init__(self, task_id, title, description, done=False, priority="Средний", due_date=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date or ""

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            done=data["done"],
            priority=data["priority"],
            due_date=data["due_date"],
        )


class TasksManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return [Task.from_dict(task) for task in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4, ensure_ascii=False)

    def mark_task_done(self):
        try:
            task_id = int(input("Введите ID задачи для отметки как выполненной: "))
            task = next((task for task in self.tasks if task.id == task_id), None)
        except ValueError:
            print("Ошибка: ID должен быть числом.")
            return
        if task:
            task.done = True
            self.save_tasks()
            print(f"Задача с ID {task_id} отмечена как выполненная.")
        else:
            print("Ошибка: задача с таким ID не найдена.")

    def add_task(self):
        task_id = max([task.id for task in self.tasks], default=0) + 1
        title = input("Введите краткое описание задачи: ").strip()
        if not title:
            print("Ошибка: описание задачи не может быть пустым.")
            return
        description = input("Введите подробное описание задачи: ").strip()
        priority = input("Введите приоритет задачи (Высокий, Средний, Низкий): ").strip()
        if priority not in ["Высокий", "Средний", "Низкий"]:
            print("Ошибка: неверный приоритет. Установлен приоритет по умолчанию — 'Средний'.")
            priority = "Средний"
        due_date = input("Введите срок выполнения задачи (ДД-ММ-ГГГГ) или оставьте пустым: ").strip()
        if due_date:
            try:
                datetime.strptime(due_date, "%d-%m-%Y")
            except ValueError:
                print("Ошибка: неверный формат даты. Задача сохранена без срока выполнения.")
                due_date = None
        new_task = Task(task_id, title, description, priority=priority, due_date=due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Задача с ID {task_id} успешно добавлена.")

    def view_tasks(self, filter_by=None, filter_value=None):
        if not self.tasks:
            print("Список задач пуст.")
            return

        tasks = self.tasks
        if filter_by == "status":
            tasks = [task for task in tasks if task.done == filter_value]
        elif filter_by == "priority":
            tasks = [task for task in tasks if task.priority == filter_value]
        elif filter_by == "due_date":
            tasks = [task for task in tasks if task.due_date == filter_value]

        if not tasks:
            print("Нет задач, соответствующих выбранным фильтрам.")
            return

        print("Список задач:")
        for task in tasks:
            status = "Выполнена" if task.done else "Не выполнена"
            print(f"[ID: {task.id}] {task.title} | Статус: {status} | Приоритет: {task.priority} | Срок: {task.due_date or 'Не задан'}")

    def edit_task(self):
        try:
            task_id = int(input("Введите ID задачи для редактирования: "))
            task = next((task for task in self.tasks if task.id == task_id), None)
            if task:
                new_title = input("Введите новое краткое описание задачи (оставьте пустым для сохранения текущего): ").strip()
                new_description = input("Введите новое подробное описание задачи (оставьте пустым для сохранения текущего): ").strip()
                new_priority = input("Введите новый приоритет задачи (Высокий, Средний, Низкий) или оставьте пустым: ").strip()
                new_due_date = input("Введите новый срок выполнения задачи (ДД-ММ-ГГГГ) или оставьте пустым: ").strip()

                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if new_priority in ["Высокий", "Средний", "Низкий"]:
                    task.priority = new_priority
                elif new_priority:
                    print("Ошибка: неверный приоритет. Сохранён текущий приоритет.")
                if new_due_date:
                    try:
                        datetime.strptime(new_due_date, "%d-%m-%Y")
                        task.due_date = new_due_date
                    except ValueError:
                        print("Ошибка: неверный формат даты. Срок выполнения сохранён без изменений.")

                self.save_tasks()
                print(f"Задача с ID {task_id} успешно обновлена.")
            else:
                print("Ошибка: задача с таким ID не найдена.")
        except ValueError:
            print("Ошибка: ID должен быть числом.")

    def delete_task(self):
        try:
            task_id = int(input("Введите ID задачи для удаления: "))
            if any(task.id == task_id for task in self.tasks):
                self.tasks = [task for task in self.tasks if task.id != task_id]
                self.save_tasks()
                print(f"Задача с ID {task_id} успешно удалена.")
            else:
                print("Ошибка: задача с таким ID не найдена.")
        except ValueError:
            print("Ошибка: ID должен быть числом.")

    def export_tasks_to_csv(self):
        if not self.tasks:
            print("Нет задач для экспорта.")
            return
        file_name = input("Введите имя файла для экспорта: ").strip()
        if not file_name.endswith(".csv"):
            print("Ошибка: имя файла должно заканчиваться на .csv.")
            return
        try:
            df = pd.DataFrame([task.to_dict() for task in self.tasks])
            df.to_csv(file_name, index=False, encoding="utf-8")
            print(f"Задачи успешно экспортированы в файл {file_name}.")
        except Exception as e:
            print(f"Ошибка при экспорте: {e}")

    def import_tasks_from_csv(self):
        file_name = input("Введите имя файла для импорта: ").strip()
        try:
            df = pd.read_csv(file_name, encoding="utf-8")
            if not {"title", "description", "done", "priority", "due_date"}.issubset(df.columns):
                print("Ошибка: некорректный формат файла.")
                return
            max_id = max([task.id for task in self.tasks], default=0)
            for _, row in df.iterrows():
                max_id += 1
                self.tasks.append(Task(
                    task_id=max_id,
                    title=row["title"],
                    description=row["description"],
                    done=row["done"],
                    priority=row["priority"],
                    due_date=row["due_date"]
                ))
            self.save_tasks()
            print(f"Задачи успешно импортированы из файла {file_name}.")
        except FileNotFoundError:
            print("Ошибка: файл не найден.")
        except pd.errors.EmptyDataError:
            print("Ошибка: файл пустой.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")
