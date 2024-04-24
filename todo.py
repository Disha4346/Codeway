import tkinter as tk
from tkinter import messagebox
import json

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x300")
        
        self.tasks = []
        
        self.load_tasks()
        
        self.create_widgets()

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.list_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selection = self.list_tasks.curselection()
            task_index = selection[0]
            del self.tasks[task_index]
            self.list_tasks.delete(task_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def mark_complete(self):
        try:
            selection = self.list_tasks.curselection()
            task_index = selection[0]
            self.tasks[task_index]["completed"] = True
            self.list_tasks.itemconfig(task_index, {'fg': 'gray', 'font': ('Arial', 10, 'italic')})
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def create_widgets(self):
        frame_input = tk.Frame(self)
        frame_input.pack(pady=10)

        self.entry_task = tk.Entry(frame_input, width=30, font=('Arial', 12))
        self.entry_task.pack(side=tk.LEFT, padx=5)

        btn_add = tk.Button(frame_input, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=('Arial', 12))
        btn_add.pack(side=tk.LEFT, padx=5)

        frame_tasks = tk.Frame(self)
        frame_tasks.pack(padx=10, pady=5)

        scrollbar = tk.Scrollbar(frame_tasks)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list_tasks = tk.Listbox(frame_tasks, width=35, height=10, yscrollcommand=scrollbar.set, font=('Arial', 12))
        for task in self.tasks:
            self.list_tasks.insert(tk.END, task["task"])
            if task["completed"]:
                self.list_tasks.itemconfig(tk.END, {'fg': 'gray', 'font': ('Arial', 10, 'italic')})

        self.list_tasks.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=self.list_tasks.yview)

        btn_remove = tk.Button(self, text="Remove Task", command=self.remove_task, bg="#FF5733", fg="white", font=('Arial', 12))
        btn_remove.pack(pady=5)

        btn_complete = tk.Button(self, text="Mark Complete", command=self.mark_complete, bg="#3498DB", fg="white", font=('Arial', 12))
        btn_complete.pack(pady=5)

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()
