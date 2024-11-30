from notes import NotesManager
from tasks import TasksManager
from contacts import ContactsManager
from financial_records import FinanceManager
from calculator import Calculator


class MainManager:
    def __init__(self):
        self.notes_manager = NotesManager()
        self.tasks_manager = TasksManager()
        self.contacts_manager = ContactsManager()
        self.finance_manager = FinanceManager()
        self.calculator = Calculator()

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

    @staticmethod
    def show_contacts_menu():
        print("\nУправление контактами:")
        print("1. Добавить новый контакт")
        print("2. Найти контакт")
        print("3. Редактировать контакт")
        print("4. Удалить контакт")
        print("5. Экспорт контактов в CSV")
        print("6. Импорт контактов из CSV")
        print("7. Выход")

    def manage_contacts(self):
        while True:
            self.show_contacts_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                self.contacts_manager.add_contact()
            elif choice == "2":
                self.contacts_manager.search_contacts()
            elif choice == "3":
                self.contacts_manager.edit_contact()
            elif choice == "4":
                self.contacts_manager.delete_contact()
            elif choice == "5":
                self.contacts_manager.export_contacts_to_csv()
            elif choice == "6":
                self.contacts_manager.import_contacts_from_csv()
            elif choice == "7":
                break
            else:
                print("Ошибка: неверный выбор. Попробуйте снова.")

    @staticmethod
    def show_finance_menu():
        print("\nУправление финансовыми записями:")
        print("1. Добавить новую финансовую запись")
        print("2. Просмотр финансовых записей")
        print("3. Генерация отчёта о финансовой активности")
        print("4. Экспорт финансовых записей в CSV")
        print("5. Импорт финансовых записей из CSV")
        print("6. Выход")

    def manage_finances(self):
        while True:
            self.show_finance_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                self.finance_manager.add_record()
            elif choice == "2":
                self.finance_manager.filter_records()
            elif choice == "3":
                self.finance_manager.generate_report()
            elif choice == "4":
                self.finance_manager.export_records_to_csv()
            elif choice == "5":
                self.finance_manager.import_records_from_csv()
            elif choice == "6":
                break
            else:
                print("Ошибка: неверный выбор. Попробуйте снова.")

    @staticmethod
    def show_calculator_menu():
        print("\nВыберите операцию:")
        print("1. Ввести арифметическое выражение")
        print("2. Выход")

    def manage_calculator(self):
        while True:
            self.show_calculator_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                expression = input("Введите арифметическое выражение: ")
                self.calculator.calculate(expression)
            elif choice == "2":
                break
            else:
                print("Ошибка: неверный выбор. Попробуйте снова.")
