import tkinter as tk
from tkinter import messagebox
import math

class MetaMathCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("MetaMath 1.0 - Математический калькулятор")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.operation_var = tk.StringVar(value="+")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="MetaMath 1.0", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        tk.Label(self.root, text="Первое число:").pack()
        tk.Entry(self.root, textvariable=self.num1_var, width=20).pack(pady=5)

        self.num2_frame = tk.Frame(self.root)
        self.num2_frame.pack()
        tk.Label(self.num2_frame, text="Второе число:").pack(side=tk.LEFT)
        tk.Entry(self.num2_frame, textvariable=self.num2_var, width=20).pack(side=tk.LEFT, padx=5)

        tk.Label(self.root, text="Операция:").pack(pady=(10,0))
        op_frame = tk.Frame(self.root)
        op_frame.pack()
        operations = ["+", "-", "*", "/", "** (степень)", "sqrt (корень)"]
        for op in operations:
            tk.Radiobutton(op_frame, text=op, variable=self.operation_var, value=op[0] if op != "sqrt (корень)" else "sqrt", command=self.toggle_num2).pack(side=tk.LEFT)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="Вычислить", command=self.calculate, bg="lightblue", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Новый расчёт", command=self.clear, bg="lightgreen", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Выход", command=self.root.quit, bg="lightcoral", width=10).pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.root, text="Результат: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def toggle_num2(self):
        op = self.operation_var.get()
        if op in ["sqrt", "log"]:
            self.num2_frame.pack_forget()
        else:
            self.num2_frame.pack()

    def clear(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.operation_var.set("+")
        self.result_label.config(text="Результат: ")
        self.num2_frame.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_var.get())
            op = self.operation_var.get()

            if op == "sqrt":
                if num1 < 0:
                    raise ValueError("Корень из отрицательного числа невозможен")
                result = math.sqrt(num1)
            elif op == "log":
                if num1 <= 0:
                    raise ValueError("Логарифм от неположительного числа невозможен")
                result = math.log(num1)
            else:
                num2 = float(self.num2_var.get())
                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    if num2 == 0:
                        raise ZeroDivisionError("Деление на ноль!")
                    result = num1 / num2
                elif op == "**":
                    result = num1 ** num2

            self.result_label.config(text=f"Результат: {result:.2f}")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
        except ZeroDivisionError as e:
            messagebox.showerror("Математическая ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Неизвестная ошибка", f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetaMathCalculator(root)
    root.mainloop()