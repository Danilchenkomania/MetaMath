import tkinter as tk
from tkinter import messagebox
import math
import time

class MetaMathCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("MetaMath 2.0 - Простой калькулятор (обновленная версия)")
        self.root.geometry("550x400")  # Уменьшен размер
        self.root.configure(bg="#e0eafc")  # Градиентный фон
        self.root.resizable(True, True)

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.operation_var = tk.StringVar(value="+")
        self.step_by_step_var = tk.StringVar(value="")

        self.create_gui_elements()

    def create_gui_elements(self):
        # Основной фрейм для центрирования
        main_frame = tk.Frame(self.root, bg="#e0eafc")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Заголовок
        title_label = tk.Label(main_frame, text="MetaMath 2.0", font=("Arial", 22, "bold"), bg="#e0eafc", fg="#1a237e")
        title_label.pack(pady=15)

        # Ввод первого числа (только цифры)
        tk.Label(main_frame, text="Первое число:", font=("Arial", 12), bg="#e0eafc").pack()
        self.num1_entry = tk.Entry(main_frame, textvariable=self.num1_var, width=35, font=("Arial", 12))
        self.num1_entry.config(validate="key", validatecommand=(self.root.register(self.validate_numeric), "%P"))
        self.num1_entry.pack(pady=5)

        # Ввод второго числа (только цифры)
        tk.Label(main_frame, text="Второе число:", font=("Arial", 12), bg="#e0eafc").pack()
        self.num2_entry = tk.Entry(main_frame, textvariable=self.num2_var, width=35, font=("Arial", 12))
        self.num2_entry.config(validate="key", validatecommand=(self.root.register(self.validate_numeric), "%P"))
        self.num2_entry.pack(pady=5)

        # Выбор операции
        tk.Label(main_frame, text="Выберите операцию:", font=("Arial", 12), bg="#e0eafc").pack(pady=(15, 5))
        op_frame = tk.Frame(main_frame, bg="#e0eafc")
        op_frame.pack()
        operations = [
            ("Плюс (+)", "+"),
            ("Минус (-)", "-"),
            ("Умножение (*)", "*"),
            ("Деление (/)", "/"),
            ("Степень (**)", "**"),
            ("Процент (%)", "%"),
            ("Корень (sqrt)", "sqrt"),
            ("Кубический корень (cbrt)", "cbrt"),
            ("Тангенс (tan)", "tan"),
            ("Логарифм (log)", "log"),
            ("Модуль (abs)", "abs")
        ]
        for text, value in operations:
            tk.Radiobutton(op_frame, text=text, variable=self.operation_var, value=value,
                          font=("Arial", 10), command=self.update_input_field).pack(side=tk.LEFT, padx=5)

        # Кнопки
        button_frame = tk.Frame(main_frame, bg="#e0eafc")
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="Вычислить", command=self.perform_calculation, bg="#42a5f5", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Новый расчёт", command=self.reset_calculator, bg="#66bb6a", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Выход", command=self.exit_application, bg="#ef5350", fg="white", width=12).pack(side=tk.LEFT, padx=5)

        # Результат и пояснения
        self.result_label = tk.Label(main_frame, text="Результат: ", font=("Arial", 14), bg="#e0eafc", fg="#1a237e")
        self.result_label.pack(pady=10)
        self.step_label = tk.Label(main_frame, textvariable=self.step_by_step_var, font=("Arial", 10), bg="#e0eafc", fg="#27ae60", wraplength=500)
        self.step_label.pack(pady=5)

        # Метка для ошибок
        self.error_label = tk.Label(main_frame, text="", font=("Arial", 10), bg="#e0eafc", fg="red")
        self.error_label.pack(pady=5)

    def validate_numeric(self, new_value):
        # Проверка ввода только цифр и точки
        if new_value == "":
            return True
        return new_value.replace(".", "").replace("-", "").isdigit() and new_value.count(".") <= 1 and new_value.count("-") <= 1

    def update_input_field(self):
        op = self.operation_var.get()
        if op in ["sqrt", "cbrt", "tan", "log", "abs", "%"]:
            self.num2_entry.delete(0, tk.END)
            self.num2_entry.config(state="disabled", bg="#d3d3d3")
        else:
            self.num2_entry.config(state="normal", bg="white")

    def reset_calculator(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.operation_var.set("+")
        self.result_label.config(text="Результат: ")
        self.step_by_step_var.set("")
        self.error_label.config(text="")
        self.num2_entry.config(state="normal", bg="white")

    def perform_calculation(self):
        self.error_label.config(text="")
        self.step_by_step_var.set("")
        self.root.config(cursor="wait")
        self.root.update()
        time.sleep(0.5)

        if not self.num1_var.get() or (self.operation_var.get() not in ["sqrt", "cbrt", "tan", "log", "abs", "%"] and not self.num2_var.get()):
            self.error_label.config(text="Ошибка: введите числа и выберите операцию!")
            self.root.config(cursor="")
            return

        try:
            num1 = self.num1_var.get()
            op = self.operation_var.get()
            steps = []

            if op == "sqrt":
                if float(num1) < 0:
                    raise ValueError("Корень из отрицательного числа невозможен")
                result = math.sqrt(float(num1))
                steps.append(f"Шаг 1: Берем число {num1}")
                steps.append(f"Шаг 2: Извлекаем корень: √{num1} = {result:.2f}")
            elif op == "cbrt":
                num1_float = float(num1)
                if num1_float < 0:
                    result = -math.pow(abs(num1_float), 1/3)
                else:
                    result = math.pow(num1_float, 1/3)
                steps.append(f"Шаг 1: Берем число {num1}")
                steps.append(f"Шаг 2: Извлекаем кубический корень: ∛{num1} ≈ {result:.2f}")
            elif op == "tan":
                num1_float = float(num1)
                result = math.tan(math.radians(num1_float))
                steps.append(f"Шаг 1: Угол {num1}°")
                steps.append(f"Шаг 2: В радианы: {math.radians(num1_float):.2f} рад")
                steps.append(f"Шаг 3: tan({math.radians(num1_float):.2f}) = {result:.2f}")
            elif op == "log":
                num1_float = float(num1)
                if num1_float <= 0:
                    raise ValueError("Логарифм от неположительного числа невозможен")
                result = math.log(num1_float)
                steps.append(f"Шаг 1: Число {num1}")
                steps.append(f"Шаг 2: ln({num1}) = {result:.2f}")
            elif op == "abs":
                num1_float = float(num1)
                result = abs(num1_float)
                steps.append(f"Шаг 1: Число {num1}")
                steps.append(f"Шаг 2: |{num1}| = {result:.2f}")
            elif op == "%":
                num1_float = float(num1)
                result = num1_float / 100
                steps.append(f"Шаг 1: Берем число {num1}")
                steps.append(f"Шаг 2: Вычисляем процент: {num1} / 100 = {result:.2f}")
            else:
                num2 = self.num2_var.get()
                if op == "+":
                    result = float(num1) + float(num2)
                    steps.append(f"Шаг 1: {num1} + {num2}")
                    steps.append(f"Шаг 2: {result:.2f}")
                elif op == "-":
                    result = float(num1) - float(num2)
                    steps.append(f"Шаг 1: {num1} - {num2}")
                    steps.append(f"Шаг 2: {result:.2f}")
                elif op == "*":
                    result = float(num1) * float(num2)
                    steps.append(f"Шаг 1: {num1} * {num2}")
                    steps.append(f"Шаг 2: {result:.2f}")
                elif op == "/":
                    num2_float = float(num2)
                    if num2_float == 0:
                        raise ZeroDivisionError("Деление на ноль!")
                    result = float(num1) / num2_float
                    steps.append(f"Шаг 1: {num1} / {num2}")
                    steps.append(f"Шаг 2: {result:.2f}")
                elif op == "**":
                    result = float(num1) ** float(num2)
                    steps.append(f"Шаг 1: {num1} ^ {num2}")
                    steps.append(f"Шаг 2: {result:.2f}")

            self.result_label.config(text=f"Результат: {result:.2f}")
            self.step_by_step_var.set("\n".join(steps))
        except ValueError as e:
            self.error_label.config(text=f"Ошибка: {str(e)}")
        except ZeroDivisionError as e:
            self.error_label.config(text=f"Ошибка: {str(e)}")
        except Exception as e:
            self.error_label.config(text=f"Ошибка: {str(e)}")
        finally:
            self.root.config(cursor="")

    def exit_application(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MetaMathCalculator(root)
    root.mainloop()