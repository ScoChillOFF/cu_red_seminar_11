from main_manager import MainManager


def main_menu(manager):
    while True:
        print("Добро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            manager.manage_notes()
        elif choice == "2":
            manage_tasks()
        elif choice == "3":
            manage_contacts()
        elif choice == "4":
            manage_financial_records()
        elif choice == "5":
            manage_calculator()
        elif choice == "6":
            print("Спасибо за использование Персонального помощника! До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер из списка.")


def manage_notes():
    print("Вы выбрали управление заметками.")


def manage_tasks():
    print("Вы выбрали управление задачами.")


def manage_contacts():
    print("Вы выбрали управление контактами.")


def manage_financial_records():
    print("Вы выбрали управление финансовыми записями.")


def manage_calculator():
    print("Вы выбрали калькулятор.")


if __name__ == "__main__":
    manager = MainManager()
    main_menu(manager)
