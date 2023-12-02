from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
# Defining colors and font names for various UI elements in the application
color1 = "#677580"
color2 = "#808F9A"
color3 = "#D1E0ED"
color4 = "#000000"
color5 = "#FFFFFF"
font_name1 = "Arial"
font_name2 = "Comic Sans MS"

# Function to add a new task to the Listbox and SQLite database
def onclick_add_button():
    # Retrieving task entered in the Entry widget
    retr_task = task_entry.get().strip()
    if retr_task:
        # Inserting the retrieved task in the listbox
        listbox.insert(END, retr_task)
        # Inserting the task into the SQLite database
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (retr_task,))
        db_connect.commit()
        # Clearing the Entry widget after adding the task in the listbox
        task_entry.delete(0, END)
    else:
        # Showing an error message if no task is entered and "ADD" is clicked
        messagebox.showinfo("Error", "No task in the field.")

# Function to mark a task as done by adding a tick mark at the beginning in the Listbox and updating SQLite database
def onclick_mark_as_done_button():
    try:
        # Getting the selected task index and its text from the Listbox
        selected_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_index)
        # Checking if the task is not already marked as done
        if not selected_task.startswith("✔ "):
            # Deleting the original task and inserting a tick mark in the beginning in the Listbox
            listbox.delete(selected_index)
            listbox.insert(selected_index, "✔ " + selected_task)
            updated_task = "✔ " + selected_task
            # Updating the task with a tick mark in the SQLite database
            cursor.execute("UPDATE tasks SET title = ? WHERE title = ?", (updated_task, selected_task))
            db_connect.commit()
    except:
        # Showing an error message if no task is selected to mark as done
        messagebox.showinfo("Error", "Select a task to mark as done.")

# Function to edit an existing task in the To-Do List
def onclick_edit_button():
    try:
        # Getting the selected task index and its text from the Listbox
        selected_index = listbox.curselection()[0]
        old_task = listbox.get(selected_index)
        # Getting the new task from the Entry widget
        new_task = task_entry.get().strip()
        if new_task:
            # Replacing the old task with the new task in the Listbox
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
            # Updating the task in the SQLite database with the new task
            cursor.execute("UPDATE tasks SET title = ? WHERE title = ?", (new_task, old_task))
            db_connect.commit()
            # Clearing the Entry widget after editing the task
            task_entry.delete(0, END)
        else:
            # Showing an error message if no new task is entered
            messagebox.showinfo("Error", "Please enter a new task to edit.")
    except:
        # Showing an error message if no task is selected to edit
        messagebox.showinfo("Error", "Select a task to edit.")

# Function to delete a selected task from the Listbox as well as SQLite database
def onclick_delete_button():
    try:
        # Getting the selected task index and its text from the Listbox
        index_value = listbox.curselection()[0]
        selected_task = listbox.get(index_value)
        # Deleting the selected task from the Listbox
        listbox.delete(index_value)
        # Deleting the selected task from the SQLite database
        cursor.execute("DELETE FROM tasks WHERE title = ?", (selected_task,))
        db_connect.commit()
    except:
        # Showing an error message if no task is selected for deletion
        messagebox.showinfo("Error", "Select a task to delete.")

# Function to delete all tasks from the To-Do List Listbox
def onclick_delete_all_button():
    try:
        # Deleting all tasks from the Listbox as well as SQLite database
        listbox.delete(0, END)
        cursor.execute("DELETE FROM tasks")
        db_connect.commit()
    except:
        # Showing an error message if there are no tasks to delete
        messagebox.showinfo("Error", "No task to delete.")

# Function to load tasks from the SQLite database into the Listbox
def database_load():
    listbox.delete(0, END)
    # Retrieving tasks from the database and ordering them by rowid in ascending order
    cursor.execute("SELECT title FROM tasks ORDER BY rowid ASC")
    rows = cursor.fetchall()
    # Iterating through the fetched rows and inserting tasks into the Listbox
    for row in rows:
        if row[0].endswith("(DONE)"):
            # Displaying tasks marked as "DONE" with a tick mark at the beginning
            listbox.insert(0, "✔ " + row[0][:-6])
        else:
            # Displaying regular tasks at the end of the Listbox
            listbox.insert(END, row[0])

# Creating the main Tkinter window
root = Tk()
root.title("To-Do List App")
root.iconbitmap("to_do_list_icon.ico")
root.resizable(False,False)
root.geometry("410x590+410+50")
root.config()
# Establishing connection to SQLite database and creating a cursor
db_connect = sql.connect("AllTasks.db")
cursor = db_connect.cursor()
cursor.execute("create table if not exists tasks (title text)")
tasks = []
# Defining and placing UI elements in the window (Buttons, Labels, Entry, Listbox, etc.)
topbar_image = PhotoImage(file="topbar.png")
Label(root, image=topbar_image).pack()
head_text = Label(root, text="TO-DO LIST", font=(font_name1, 16,"bold"), background=color1, foreground=color5)
head_text.place(x=141, y=26)
task_here = Label(root, text="Enter task:", font=(font_name2, 13), padx=7, pady=5)
task_here.place(y=96)
task_entry = Entry(root, font=(font_name1, 12, "italic", "bold"), width=26, background=color2, foreground=color5)
task_entry.place(x=107, y=99, height=33)
task_entry.focus()
# Creating button to add task and defining its design and placement
add_button = Button(
    root,
    text="ADD",
    font=(font_name1, 12, "bold"),
    width=4,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    command=onclick_add_button
)
add_button.place(x=347, y=99)
# Creating button to delete task and defining its design and placement
delete_button = Button(
    root,
    text="DELETE TASK",
    font=(font_name1, 12, "bold"),
    width=17,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    padx=5,
    command=onclick_delete_button
)
delete_button.place(x=12, y=186)
# Creating button to delete all tasks and defining its design and placement
delete_all_button = Button(
    root,
    text="DELETE ALL TASKS",
    font=(font_name1, 12, "bold"),
    width=17,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    padx=5,
    command=onclick_delete_all_button
)
delete_all_button.place(x=209, y=186)
# Creating button to mark specific task done and defining its design and placement
mark_as_done_button = Button(
    root,
    text="MARK AS DONE",
    font=(font_name1, 12, "bold"),
    width=17,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    padx=5,
    command=onclick_mark_as_done_button
)
mark_as_done_button.place(x=12, y=145)
# Creating button to edit task and defining its design and placement
edit_button = Button(
    root,
    text="EDIT TASK",
    font=(font_name1, 12, "bold"),
    width=17,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    padx=5,
    command=onclick_edit_button
)
edit_button.place(x=209, y=145)
frame = Frame(root, bd=3, width=700, height=280, background=color2)
frame.pack(pady=(150,0))
listbox = Listbox(frame, font=(font_name1, 14, "bold"), width=34, height=25, background=color2, foreground=color5)
listbox.pack(side=LEFT, fill=BOTH, padx=2, expand=True)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
# Loading tasks from the database when the application starts
database_load()
# Starting the Tkinter event loop
root.mainloop()
