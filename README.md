

# To-Do List Application

## Introduction

This Python script implements a straightforward To-Do List application using Tkinter for the graphical user interface and SQLite for database management. The application provides a user-friendly interface to manage tasks efficiently.

## Features and Functionality

- **Adding Tasks**: Easily add tasks to the list by entering them in the provided field and clicking the "ADD" button.
- **Marking Tasks as Done**: Select a task and click the "MARK AS DONE" button to mark it as completed.
- **Editing Tasks**: Modify existing tasks by selecting them, entering the new task, and clicking the "EDIT TASK" button.
- **Deleting Tasks**: Remove individual tasks by selecting them and clicking the "DELETE TASK" button, or clear the entire list with the "DELETE ALL TASKS" button.

## Implementation

### Requirements
- **Python**: Ensure Python 3.x is installed.
- **Libraries**: Necessary Python libraries (`tkinter`, `sqlite3`) should be available.

### Running the Application
1. **Execution**: Run the Python script `todo_list.py`.
2. **Interface**: The To-Do List application window will open.
3. **Adding Tasks**: Enter tasks and click "ADD" to add them to the list.
4. **Managing Tasks**: Select a task to mark as done, edit, or delete using the respective buttons.
5. **Deleting Tasks**: Use the "DELETE TASK" button for individual tasks or "DELETE ALL TASKS" to clear the entire list.

### Additional Notes
- **Database Management**: The application uses SQLite to store tasks. A file named `AllTasks.db` manages the tasks.
- **Task Status**: Completed tasks have a "✔" symbol at the beginning of their description.
- **Image Files**: Ensure the necessary image files (`to_do_list_icon.ico`, `topbar.png`) are in the script's directory.

## Conclusion

The To-Do List application offers a simple yet effective way to manage tasks. Contributions are welcome to enhance functionality, improve the user interface, or fix any issues. Feel free to fork the repository, make modifications, and create pull requests to contribute to the project's development.

---

Make sure to update any specific paths or instructions regarding the image files and verify the script's compatibility with Python 3.x before usage or contribution.
