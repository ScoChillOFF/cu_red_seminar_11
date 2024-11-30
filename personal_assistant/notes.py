import json
import pandas as pd
from datetime import datetime


class Note:
    def __init__(self, note_id, title, content, timestamp=None):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def from_dict(data):
        return Note(
            note_id=data["id"],
            title=data["title"],
            content=data["content"],
            timestamp=data["timestamp"],
        )


class NotesManager:
    def __init__(self, file_name="notes.json"):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return [Note.from_dict(note) for note in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_notes(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump([note.to_dict() for note in self.notes], file, indent=4, ensure_ascii=False)

    def create_note(self):
        note_id = max([note.id for note in self.notes], default=0) + 1
        title = input("Введите заголовок заметки: ").strip()
        if not title:
            print("Ошибка: заголовок не может быть пустым.")
            return
        content = input("Введите содержимое заметки: ").strip()
        new_note = Note(note_id, title, content)
        self.notes.append(new_note)
        self.save_notes()
        print(f"Заметка с ID {note_id} успешно создана.")

    def view_notes(self):
        if not self.notes:
            print("Список заметок пуст.")
            return
        print("Список заметок:")
        for note in self.notes:
            print(f"[ID: {note.id}] {note.title} - {note.timestamp}")

    def view_note_details(self):
        try:
            note_id = int(input("Введите ID заметки для просмотра: "))
            note = next((note for note in self.notes if note.id == note_id), None)
        except ValueError:
            print("Ошибка: ID должен быть числом.")
            return
        if note:
            print(f"Заголовок: {note.title}")
            print(f"Содержимое: {note.content}")
            print(f"Дата создания/изменения: {note.timestamp}")
        else:
            print("Ошибка: заметка с таким ID не найдена.")

    def edit_note(self):
        try:
            note_id = int(input("Введите ID заметки для редактирования: "))
            note = next((note for note in self.notes if note.id == note_id), None)
        except ValueError:
            print("Ошибка: ID должен быть числом.")
            return
        if note:
            new_title = input("Введите новый заголовок заметки (оставьте пустым для сохранения текущего): ").strip()
            new_content = input("Введите новое содержимое заметки (оставьте пустым для сохранения текущего): ").strip()
            if new_title:
                note.title = new_title
            if new_content:
                note.content = new_content
            note.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.save_notes()
            print(f"Заметка с ID {note_id} успешно обновлена.")
        else:
            print("Ошибка: заметка с таким ID не найдена.")

    def delete_note(self):
        try:
            note_id = int(input("Введите ID заметки для удаления: "))
        except ValueError:
            print("Ошибка: ID должен быть числом.")
            return
        if any(note.id == note_id for note in self.notes):
            self.notes = [note for note in self.notes if note.id != note_id]
            self.save_notes()
            print(f"Заметка с ID {note_id} успешно удалена.")
        else:
            print("Ошибка: заметка с таким ID не найдена.")

    def export_notes_to_csv(self):
        if not self.notes:
            print("Нет заметок для экспорта.")
            return
        file_name = input("Введите имя файла для экспорта (например, notes.csv): ").strip()
        if not file_name.endswith(".csv"):
            print("Ошибка: имя файла должно заканчиваться на .csv.")
            return
        try:
            df = pd.DataFrame([note.to_dict() for note in self.notes])
            df.to_csv(file_name, index=False, encoding="utf-8")
            print(f"Заметки успешно экспортированы в файл {file_name}.")
        except Exception as e:
            print(f"Ошибка при экспорте: {e}")

    def import_notes_from_csv(self):
        file_name = input("Введите имя файла для импорта (например, notes.csv): ").strip()
        try:
            df = pd.read_csv(file_name, encoding="utf-8")
            if not {"title", "content", "timestamp"}.issubset(df.columns):
                print("Ошибка: некорректный формат файла.")
                return
            max_id = max([note.id for note in self.notes], default=0)
            for _, row in df.iterrows():
                max_id += 1
                self.notes.append(Note(max_id, row["title"], row["content"], row["timestamp"]))
            self.save_notes()
            print(f"Заметки успешно импортированы из файла {file_name}.")
        except FileNotFoundError:
            print("Ошибка: файл не найден.")
        except pd.errors.EmptyDataError:
            print("Ошибка: файл пустой.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")
