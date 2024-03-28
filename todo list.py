import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            messagebox.showinfo("Tasks", "\n".join(self.tasks))
        else:
            messagebox.showinfo("Tasks", "No tasks.")

    def mark_task_complete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] += " - Completed"
            messagebox.showinfo("Success", "Task marked as complete.")
        else:
            messagebox.showerror("Error", "Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            messagebox.showinfo("Success", "Task deleted.")
        else:
            messagebox.showerror("Error", "Invalid task index.")

def add_task():
    task = entry_task.get()
    if task:
        todo_list.add_task(task)
        messagebox.showinfo("Success", "Task added successfully.")
        entry_task.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task.")

def view_tasks():
    todo_list.view_tasks()

def mark_complete():
    try:
        index = int(entry_index.get())
        todo_list.mark_task_complete(index)
    except ValueError:
        messagebox.showerror("Error", "Invalid task index.")
    entry_index.delete(0, tk.END)

def delete_task():
    try:
        index = int(entry_index.get())
        todo_list.delete_task(index)
    except ValueError:
        messagebox.showerror("Error", "Invalid task index.")
    entry_index.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create TodoList instance
todo_list = TodoList()

# Create entry widgets
label_task = tk.Label(root, text="Task:")
label_task.grid(row=0, column=0, padx=5, pady=5)
entry_task = tk.Entry(root, width=30)
entry_task.grid(row=0, column=1, padx=5, pady=5)

label_index = tk.Label(root, text="Task Index:")
label_index.grid(row=1, column=0, padx=5, pady=5)
entry_index = tk.Entry(root, width=10)
entry_index.grid(row=1, column=1, padx=5, pady=5)

# Create buttons
button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.grid(row=0, column=2, padx=5, pady=5)

button_view = tk.Button(root, text="View Tasks", command=view_tasks)
button_view.grid(row=1, column=2, padx=5, pady=5)

button_complete = tk.Button(root, text="Mark Complete", command=mark_complete)
button_complete.grid(row=2, column=0, padx=5, pady=5)

button_delete = tk.Button(root, text="Delete Task", command=delete_task)
button_delete.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
