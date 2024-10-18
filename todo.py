import tkinter as tk
from tkinter import messagebox
import json

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed
        }

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = self.load_tasks()

        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        self.task_list_box = tk.Listbox(self.task_list_frame, width=40, selectmode=tk.SINGLE)
        self.task_list_box.pack(side="left", fill="both", expand=True)

        self.task_scrollbar = tk.Scrollbar(self.task_list_frame)
        self.task_scrollbar.pack(side="right", fill="y")
        self.task_list_box.config(yscrollcommand=self.task_scrollbar.set)
        self.task_scrollbar.config(command=self.task_list_box.yview)

        self.task_details_frame = tk.Frame(self.root)
        self.task_details_frame.pack(fill="both", expand=True)

        self.task_title_label = tk.Label(self.task_details_frame, text="Title:")
        self.task_title_label.pack()

        self.task_title_entry = tk.Entry(self.task_details_frame, width=40)
        self.task_title_entry.pack()

        self.task_description_label = tk.Label(self.task_details_frame, text="Description:")
        self.task_description_label.pack()

        self.task_description_entry = tk.Text(self.task_details_frame, width=40, height=5)
        self.task_description_entry.pack()

        self.task_category_label = tk.Label(self.task_details_frame, text="Category:")
        self.task_category_label.pack()

        self.task_category_entry = tk.Entry(self.task_details_frame, width=40)
        self.task_category_entry.pack()

        self.add_task_button = tk.Button(self.task_details_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.mark_completed_button = tk.Button(self.task_details_frame, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack()

        self.delete_task_button = tk.Button(self.task_details_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.update_task_list()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                return [Task(**data) for data in json.load(f)]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def update_task_list(self):
        self.task_list_box.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            self.task_list_box.insert(tk.END, f"{i}. {task.title} ({status}) - {task.category}")

    def add_task(self):
        title = self.task_title_entry.get()
        description = self.task_description_entry.get("1.0", tk.END).strip()  # Strip trailing newline
        category = self.task_category_entry.get()

        if title and category:
            self.tasks.append(Task(title, description, category))
            self.save_tasks()
            self.update_task_list()

    def mark_completed(self):
        selected_task_id = self.task_list_box.curselection()
        if selected_task_id:
            task_id = selected_task_id[0]
            task = self.tasks[task_id]
            task.mark_completed()
            self.save_tasks()
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_task_id = self.task_list_box.curselection()
        if selected_task_id:
            task_id = selected_task_id[0]
            task = self.tasks[task_id]
            if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{task.title}'?"):
                del self.tasks[task_id]
                self.save_tasks()
                self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

root = tk.Tk()
root.title("Personal To-Do List App")
app = ToDoListApp(root)
root.mainloop()
