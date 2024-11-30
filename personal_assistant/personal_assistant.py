from main_manager import MainManager


def main_menu(manager):
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
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
            manager.manage_tasks()
        elif choice == "3":
            manager.manage_contacts()
        elif choice == "4":
            manager.manage_finances()
        elif choice == "5":
            manager.manage_calculator()
        elif choice == "6":
            print("Спасибо за использование Персонального помощника! До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер из списка.")


if __name__ == "__main__":
    manager = MainManager()
    main_menu(manager)
