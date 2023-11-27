import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x300")
        self.root.config(bg="#265073")

        # Task list
        self.tasks = []

        # Entry widget for new tasks
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 12), bd=3)
        self.task_entry.pack(pady=10)
        self.task_entry.configure(bg="#9EB8D9")

        # Buttons
        add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4caf50", fg="white", font=("Helvetica", 10))
        add_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#ff3333", fg="white", font=("Helvetica", 10))
        delete_button.pack(pady=5)

        show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks, bg="#007bff", fg="white", font=("Helvetica", 10))
        show_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Task Added", f"Task '{task}' added successfully.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        task = self.task_entry.get()
        if task in self.tasks:
            self.tasks.remove(task)
            messagebox.showinfo("Task Deleted", f"Task '{task}' deleted successfully.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Task Not Found", f"Task '{task}' not found in the list.")

    def show_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks to display.")
        else:
            task_list = "\n".join(self.tasks)
            messagebox.showinfo("Task List", f"Task List:\n{task_list}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
