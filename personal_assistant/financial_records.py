import json
import pandas as pd
from datetime import datetime


class FinanceRecord:
    def __init__(self, record_id, amount, category, date, description=""):
        self.id = record_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }

    @staticmethod
    def from_dict(data):
        return FinanceRecord(
            record_id=data["id"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data.get("description", ""),
        )


class FinanceManager:
    def __init__(self, file_name="finance.json"):
        self.file_name = file_name
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return [FinanceRecord.from_dict(record) for record in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_records(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump([record.to_dict() for record in self.records], file, indent=4, ensure_ascii=False)

    def add_record(self):
        record_id = max([record.id for record in self.records], default=0) + 1
        while True:
            try:
                amount = float(input("Введите сумму операции (положительное число для дохода, отрицательное для расхода): "))
                break
            except ValueError:
                print("Ошибка: сумма должна быть числом.")
        category = input("Введите категорию операции: ").strip()
        date = input("Введите дату операции (ДД-ММ-ГГГГ): ").strip()
        description = input("Введите описание операции (или оставьте пустым): ").strip()

        # Проверка даты
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Ошибка: неверный формат даты. Используйте формат ДД-ММ-ГГГГ.")
            return

        new_record = FinanceRecord(record_id, amount, category, date, description)
        self.records.append(new_record)
        self.save_records()
        print(f"Запись с ID {record_id} успешно добавлена.")

    def filter_records(self):
        filter_choice = input("Фильтровать по дате или категории? (введите 'дата' или 'категория' или оставьте пустым): ").strip().lower()
        if not filter_choice:
            filtered = self.records
        elif filter_choice == "дата":
            date_from = input("Введите начальную дату (ДД-ММ-ГГГГ): ").strip()
            date_to = input("Введите конечную дату (ДД-ММ-ГГГГ): ").strip()
            try:
                date_from_dt = datetime.strptime(date_from, "%d-%m-%Y")
                date_to_dt = datetime.strptime(date_to, "%d-%m-%Y")
            except ValueError:
                print("Ошибка: неверный формат даты.")
                return
            filtered = [record for record in self.records if date_from_dt <= datetime.strptime(record.date, "%d-%m-%Y") <= date_to_dt]
        elif filter_choice == "категория":
            category = input("Введите категорию для фильтрации: ").strip()
            filtered = [record for record in self.records if category.lower() in record.category.lower()]
        else:
            print("Ошибка: неверный выбор фильтра.")
            return

        if filtered:
            print("Фильтрованные записи:")
            for record in filtered:
                print(f"[ID: {record.id}] {record.date} | {record.category} | Сумма: {record.amount} | Описание: {record.description}")
        else:
            print("Записи не найдены.")

    def generate_report(self):
        date_from = input("Введите начальную дату для отчёта (ДД-ММ-ГГГГ): ").strip()
        date_to = input("Введите конечную дату для отчёта (ДД-ММ-ГГГГ): ").strip()
        try:
            datetime.strptime(date_from, "%d-%m-%Y")
            datetime.strptime(date_to, "%d-%m-%Y")
        except ValueError:
            print("Ошибка: неверный формат даты.")
            return

        filtered_records = [record for record in self.records if date_from <= record.date <= date_to]
        if not filtered_records:
            print("Нет записей для указанного периода.")
            return

        income = sum(record.amount for record in filtered_records if record.amount > 0)
        expense = sum(record.amount for record in filtered_records if record.amount < 0)
        balance = income + expense

        print(f"Отчёт за период с {date_from} по {date_to}:")
        print(f"Доходы: {income}")
        print(f"Расходы: {expense}")
        print(f"Баланс: {balance}")

        file_name = f"report_{date_from}_{date_to}.csv"
        df = pd.DataFrame([record.to_dict() for record in self.records])
        df.to_csv(file_name, index=False, encoding="utf-8")
        print(f"Подробная информация сохранена в файл {file_name}.")

    def export_records_to_csv(self):
        if not self.records:
            print("Нет финансовых записей для экспорта.")
            return
        file_name = input("Введите имя файла для экспорта (например, finance.csv): ").strip()
        if not file_name.endswith(".csv"):
            print("Ошибка: имя файла должно заканчиваться на .csv.")
            return
        try:
            df = pd.DataFrame([record.to_dict() for record in self.records])
            df.to_csv(file_name, index=False, encoding="utf-8")
            print(f"Финансовые записи успешно экспортированы в файл {file_name}.")
        except Exception as e:
            print(f"Ошибка при экспорте: {e}")

    def import_records_from_csv(self):
        file_name = input("Введите имя файла для импорта (например, finance.csv): ").strip()
        try:
            df = pd.read_csv(file_name, encoding="utf-8")
            if not {"amount", "category", "date"}.issubset(df.columns):
                print("Ошибка: некорректный формат файла.")
                return
            max_id = max([record.id for record in self.records], default=0)
            for _, row in df.iterrows():
                try:
                    amount = float(row["amount"])
                except ValueError:
                    print(f"Ошибка: некорректная сумма '{row['amount']}' в файле.")
                    continue
                category = row["category"].strip()
                date = row["date"].strip()
                description = row.get("description", "").strip()
                try:
                    datetime.strptime(date, "%d-%m-%Y")
                except ValueError:
                    print(f"Ошибка: некорректная дата '{date}' в файле.")
                    continue

                max_id += 1
                self.records.append(FinanceRecord(
                    record_id=max_id,
                    amount=amount,
                    category=category,
                    date=date,
                    description=description
                ))
            self.save_records()
            print(f"Финансовые записи успешно импортированы из файла {file_name}.")
        except FileNotFoundError:
            print("Ошибка: файл не найден.")
        except pd.errors.EmptyDataError:
            print("Ошибка: файл пустой.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")