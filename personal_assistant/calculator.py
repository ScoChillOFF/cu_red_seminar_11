class Calculator:
    def __init__(self):
        self.allowed_operators = ["+", "-", "*", "/", "(", ")"]

    def calculate(self, expression):
        if all(char.isdigit() or char.isspace() or char in self.allowed_operators for char in expression):
            try:
                result = eval(expression)
                print(result)
            except ZeroDivisionError:
                print("Ошибка: деление на ноль")
            except Exception as e:
                print(f"Ошибка: {str(e)}")
        else:
            print("Ошибка: недопустимые символы в выражении")
