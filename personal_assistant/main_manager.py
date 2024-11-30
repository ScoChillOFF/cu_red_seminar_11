from notes import NotesManager


class MainManager:
    def __init__(self):
        self.notes_manager = NotesManager()

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
