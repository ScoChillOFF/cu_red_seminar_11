import json
import pandas as pd


class Contact:
    def __init__(self, contact_id, name, phone="", email=""):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            contact_id=data["id"],
            name=data["name"],
            phone=data.get("phone", ""),
            email=data.get("email", ""),
        )


class ContactsManager:
    def __init__(self, file_name="contacts.json"):
        self.file_name = file_name
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return [Contact.from_dict(contact) for contact in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4, ensure_ascii=False)

    def add_contact(self):
        contact_id = max([contact.id for contact in self.contacts], default=0) + 1
        name = input("Введите имя контакта: ").strip()
        if not name:
            print("Ошибка: имя контакта не может быть пустым.")
            return
        phone = input("Введите номер телефона (или оставьте пустым): ").strip()
        email = input("Введите адрес электронной почты (или оставьте пустым): ").strip()
        new_contact = Contact(contact_id, name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"Контакт с ID {contact_id} успешно добавлен.")

    def search_contacts(self):
        query = input("Введите имя или номер телефона для поиска: ").strip().lower()
        results = [contact for contact in self.contacts if query in contact.name.lower() or query in contact.phone]
        if results:
            print("Найденные контакты:")
            for contact in results:
                print(f"[ID: {contact.id}] {contact.name} | Телефон: {contact.phone} | Email: {contact.email}")
        else:
            print("Контакты не найдены.")

    def edit_contact(self):
        try:
            contact_id = int(input("Введите ID контакта для редактирования: "))
        except ValueError:
            print("Ошибка: ID должен быть числом.")
            return
        contact = next((contact for contact in self.contacts if contact.id == contact_id), None)
        if contact:
            new_name = input(f"Введите новое имя ({contact.name}): ").strip()
            new_phone = input(f"Введите новый номер телефона ({contact.phone}): ").strip()
            new_email = input(f"Введите новый адрес электронной почты ({contact.email}): ").strip()

            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email

            self.save_contacts()
            print(f"Контакт с ID {contact_id} успешно обновлён.")
        else:
            print("Ошибка: контакт с таким ID не найден.")

    def delete_contact(self):
        try:
            contact_id = int(input("Введите ID контакта для удаления: "))
        except ValueError:
            print("Ошибка: ID должен быть числом.")
            return
        if any(contact.id == contact_id for contact in self.contacts):
            self.contacts = [contact for contact in self.contacts if contact.id != contact_id]
            self.save_contacts()
            print(f"Контакт с ID {contact_id} успешно удалён.")
        else:
            print("Ошибка: контакт с таким ID не найден.")

    def export_contacts_to_csv(self):
        if not self.contacts:
            print("Нет контактов для экспорта.")
            return
        file_name = input("Введите имя файла для экспорта (например, contacts.csv): ").strip()
        if not file_name.endswith(".csv"):
            print("Ошибка: имя файла должно заканчиваться на .csv.")
            return
        try:
            df = pd.DataFrame([contact.to_dict() for contact in self.contacts])
            df.to_csv(file_name, index=False, encoding="utf-8")
            print(f"Контакты успешно экспортированы в файл {file_name}.")
        except Exception as e:
            print(f"Ошибка при экспорте: {e}")

    def import_contacts_from_csv(self):
        file_name = input("Введите имя файла для импорта (например, contacts.csv): ").strip()
        try:
            df = pd.read_csv(file_name, encoding="utf-8")
            if not {"name", "phone", "email"}.issubset(df.columns):
                print("Ошибка: некорректный формат файла.")
                return
            max_id = max([contact.id for contact in self.contacts], default=0)
            for _, row in df.iterrows():
                max_id += 1
                self.contacts.append(Contact(
                    contact_id=max_id,
                    name=row["name"],
                    phone=row.get("phone", ""),
                    email=row.get("email", "")
                ))
            self.save_contacts()
            print(f"Контакты успешно импортированы из файла {file_name}.")
        except FileNotFoundError:
            print("Ошибка: файл не найден.")
        except pd.errors.EmptyDataError:
            print("Ошибка: файл пустой.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")