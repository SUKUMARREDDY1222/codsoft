import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            else:
                result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        messagebox.showinfo("Result", f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input")


# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Create operation dropdown
operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")  # Default operation
operation_dropdown = tk.OptionMenu(root, operation_var, *operation_choices)
operation_dropdown.grid(row=0, column=2, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, columnspan=3, padx=5, pady=5)

root.mainloop()
