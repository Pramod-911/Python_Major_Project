# Python_Major_Project
### Documentation for Personal To-Do List Application

This documentation provides an overview of the implementation of the Personal To-Do List Application using Python's `tkinter` library for the graphical user interface (GUI) and `json` for data storage.

#### Table of Contents
1. **Overview**
2. **Class Descriptions**
   - Task Class
   - ToDoListApp Class
3. **Features**
4. **Detailed Code Explanation**
5. **Dependencies**
6. **Usage Instructions**

---

### 1. **Overview**

This To-Do List Application allows users to:
- Add tasks with a title, description, and category.
- View all tasks in a list, with the status of "Pending" or "Completed".
- Mark tasks as completed.
- Delete tasks from the list.
- Save tasks to a file (`tasks.json`) and load them when the application starts.

The application uses a graphical interface built with `tkinter`, and the tasks are stored as JSON objects for persistence.

---

### 2. **Class Descriptions**

#### **Task Class**
The `Task` class defines the structure of each task. Each task has the following attributes:
- `title`: The name of the task.
- `description`: A description of the task (optional).
- `category`: The category the task belongs to.
- `completed`: A boolean to indicate whether the task is completed (default is `False`).

**Methods**:
- `mark_completed()`: Marks the task as completed by setting `self.completed = True`.
- `to_dict()`: Converts the task object into a dictionary format, suitable for saving as JSON.

#### **ToDoListApp Class**
This is the main class that handles the entire application interface and logic. It creates the GUI, manages tasks, and handles user interactions.

**Attributes**:
- `root`: The main window of the application.
- `tasks`: A list of `Task` objects, which are loaded from `tasks.json` or initialized as an empty list if the file doesn't exist.

**Methods**:
- `__init__(self, root)`: Initializes the application, sets up the GUI, and loads tasks.
- `load_tasks()`: Loads tasks from a JSON file (`tasks.json`). If the file is not found, it returns an empty list.
- `save_tasks()`: Saves the current tasks to a JSON file.
- `update_task_list()`: Updates the task list in the GUI, showing tasks with their status (Pending/Completed) and category.
- `add_task()`: Adds a new task to the list. The user provides a title, description, and category, and the task is saved.
- `mark_completed()`: Marks the selected task as completed. The user must select a task from the list to update it.
- `delete_task()`: Deletes the selected task from the list after user confirmation.

---

### 3. **Features**

- **Task Creation**: Users can add new tasks with a title, description, and category.
- **Mark Task as Completed**: Users can mark tasks as completed, which updates the task's status.
- **Task Deletion**: Users can delete tasks from the list.
- **Persistent Storage**: Tasks are saved in a `tasks.json` file and are loaded back into the app when it is reopened.
- **Scrollable Task List**: The task list is scrollable if there are many tasks.
- **Status Display**: Each task is displayed with a "Pending" or "Completed" status.

---

### 4. **Detailed Code Explanation**

**1. Task Class**:
```python
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
```
- This class represents a single task. It can be marked as completed using `mark_completed()` and converted to a dictionary using `to_dict()`.

**2. ToDoListApp Class (GUI Implementation)**:
```python
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = self.load_tasks()

        # Task list frame
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        # Task listbox with scrollbar
        self.task_list_box = tk.Listbox(self.task_list_frame, width=40, selectmode=tk.SINGLE)
        self.task_list_box.pack(side="left", fill="both", expand=True)

        self.task_scrollbar = tk.Scrollbar(self.task_list_frame)
        self.task_scrollbar.pack(side="right", fill="y")
        self.task_list_box.config(yscrollcommand=self.task_scrollbar.set)
        self.task_scrollbar.config(command=self.task_list_box.yview)

        # Task details frame
        self.task_details_frame = tk.Frame(self.root)
        self.task_details_frame.pack(fill="both", expand=True)

        # Input fields for task title, description, and category
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

        # Buttons for adding, marking completed, and deleting tasks
        self.add_task_button = tk.Button(self.task_details_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.mark_completed_button = tk.Button(self.task_details_frame, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack()

        self.delete_task_button = tk.Button(self.task_details_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.update_task_list()
```
- The GUI components are laid out in frames. The `Listbox` displays the task list, while `Entry` and `Text` widgets accept user input for new tasks.

**3. Task Management Methods**:
- `load_tasks()` and `save_tasks()` handle loading and saving tasks to/from `tasks.json`.
- `update_task_list()` updates the task list display.
- `add_task()` adds a new task based on the user's input.
- `mark_completed()` marks a selected task as completed.
- `delete_task()` deletes the selected task after confirmation.

---

### 5. **Dependencies**

- `tkinter`: The built-in Python library for creating GUIs.
- `json`: Standard library for handling JSON data.

---

### 6. **Usage Instructions**

1. Run the Python script.
2. The GUI will display with options to add tasks, mark them as completed, or delete them.
3. Task data is saved automatically in `tasks.json` and reloaded when the application is restarted.

--- 

This documentation should provide a clear understanding of how the application is structured and how to use it. Let me know if you need further details!
