import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        password = generate_password(length)
        messagebox.showinfo("Generated Password", f"Your password:\n{password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create entry widget for password length
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)
entry_length = tk.Entry(root, width=10)
entry_length.pack(pady=5)

# Create generate button
button_generate = tk.Button(root, text="Generate Password", command=generate_and_display_password)
button_generate.pack(pady=5)

root.mainloop()
