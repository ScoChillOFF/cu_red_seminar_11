from notes import NotesManager
from tasks import TasksManager


class MainManager:
    def __init__(self):
        self.notes_manager = NotesManager()
        self.tasks_manager = TasksManager()

    @staticmethod
    def show_notes_menu():
        print("\nУправление заметками:")
        print("1. Создать новую заметку")
        print("2. Просмотреть список заметок")
        print("3. Просмотреть подробности заметки")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Экспорт заметок в CSV")
        print("7. Импорт заметок из CSV")
        print("8. Назад в главное меню")

    def manage_notes(self):
        while True:
            self.show_notes_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                self.notes_manager.create_note()
            elif choice == "2":
                self.notes_manager.view_notes()
            elif choice == "3":
                self.notes_manager.view_note_details()
            elif choice == "4":
                self.notes_manager.edit_note()
            elif choice == "5":
                self.notes_manager.delete_note()
            elif choice == "6":
                self.notes_manager.export_notes_to_csv()
            elif choice == "7":
                self.notes_manager.import_notes_from_csv()
            elif choice == "8":
                break
            else:
                print("Ошибка: неверный выбор. Попробуйте снова.")

    @staticmethod
    def show_tasks_menu():
        print("\nУправление задачами:")
        print("1. Добавить новую задачу")
        print("2. Просмотреть список задач")
        print("3. Отметить задачу как выполненную")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Экспорт задач в CSV")
        print("7. Импорт задач из CSV")
        print("8. Выход")

    def manage_tasks(self):
        while True:
            self.show_tasks_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                self.tasks_manager.add_task()
            elif choice == "2":
                self.tasks_manager.view_tasks()
            elif choice == "3":
                self.tasks_manager.mark_task_done()
            elif choice == "4":
                self.tasks_manager.edit_task()
            elif choice == "5":
                self.tasks_manager.delete_task()
            elif choice == "6":
                self.tasks_manager.export_tasks_to_csv()
            elif choice == "7":
                self.tasks_manager.import_tasks_from_csv()
            elif choice == "8":
                break
            else:
                print("Ошибка: неверный выбор. Попробуйте снова.")
