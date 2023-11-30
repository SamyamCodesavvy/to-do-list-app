from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
color1 = "#677580"
color2 = "#808F9A"
color3 = "#D1E0ED"
color4 = "#000000"
color5 = "#FFFFFF"
color6 = "#86DC3D"
font_name1 = "Arial"
font_name2 = "Times New Roman"
font_name3 = "Comic Sans MS"
def onclick_add_button():
    retr_task = task_entry.get()
    if retr_task:
        tasks.append(retr_task)
        cursor.execute("insert into tasks values (?)", (retr_task,))
        db_connect.commit()
        # Add numbers and two spaces to the beginning of the task
        task_number = len(tasks)  # Get the number of tasks
        listbox.insert(END, retr_task)  # Insert task with number at the beginning
        task_entry.delete(0, END)
    else:
        messagebox.showinfo("Error", "No task in the field.")
def onclick_mark_as_done_button():
    try:
        selected_index = listbox.curselection()[0]
        selected_task = tasks[selected_index]

        # Add a tick mark to the task if not already marked
        if not selected_task.startswith("✔"):
            tasks[selected_index] = f"✔ {selected_task}"
            listbox.delete(selected_index)
            listbox.insert(selected_index, tasks[selected_index])

            # Update the task with the tick mark in the database
            cursor.execute("UPDATE tasks SET title = ? WHERE rowid = ?", (tasks[selected_index], selected_index + 1))
            db_connect.commit()
    except IndexError:
        messagebox.showinfo("Error", "Select a task to mark as done.")


def onclick_delete_button():
    try:
        spec_task = listbox.curselection()[0]
        listbox.delete(spec_task)
        deleted_task = tasks.pop(spec_task)
        cursor.execute("DELETE FROM tasks WHERE rowid = ?", (spec_task + 1,))
        db_connect.commit()
    except:
        messagebox.showinfo("Error", "Select a task to delete.")
def onclick_edit_button():
    try:
        selected_index = listbox.curselection()[0]
        updated_task = task_entry.get()

        if updated_task:
            tasks[selected_index] = updated_task
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"{selected_index + 1}. {updated_task}")

            # Update the task in the SQL database
            cursor.execute("UPDATE tasks SET title = ? WHERE rowid = ?", (updated_task, selected_index + 1))
            db_connect.commit()

            task_entry.delete(0, END)
        else:
            messagebox.showinfo("Error", "No task entered.")
    except IndexError:
        messagebox.showinfo("Error", "Select a task to edit.")

    edit_button = Button(
        root,
        text="EDIT",
        font=(font_name1, 12, "bold"),
        width=10,
        background=color4,
        foreground=color5,
        activebackground=color3,
        activeforeground=color4,
        cursor="hand2",
        padx=5,
        command=onclick_edit_button  # Binding the function to the button
    )
    edit_button.place(x=147, y=195)
def load_tasks_from_db():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    for row in rows:
        tasks.append(row[0])
        listbox.insert(END, f"{len(tasks)}. {row[0]}")

root = Tk()
root.title("To-Do List App")
root.iconbitmap("to_do_list_icon.ico")
root.resizable(False,False)
root.geometry("410x530+400+80")
root.config()
db_connect = sql.connect("TodoTaskLists.db")
cursor = db_connect.cursor()
cursor.execute("create table if not exists tasks (title text)")
tasks = []
topbar_image = PhotoImage(file="topbar.png")
Label(root, image=topbar_image).pack()
head_text = Label(root, text="TO-DO LIST", font=(font_name1, 16 ,"bold"), background=color1, foreground=color5)
head_text.place(x=141, y=26)
task_here = Label(root, text="Enter task:", font=(font_name3, 13), padx=7, pady=5)
task_here.place(y=96)
task_entry = Entry(root, font=(font_name1, 12, "italic", "bold"), width=26, background=color2, foreground=color5)
task_entry.place(x=107, y=99, height=33)
task_entry.focus()
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
delete_button = Button(
    root,
    text="DELETE",
    font=(font_name1, 12, "bold"),
    width=10,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    padx=5,
    command=onclick_delete_button
)
delete_button.place(x=12, y=195)
edit_button = Button(
    root,
    text="EDIT",
    font=(font_name1, 12, "bold"),
    width=10,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    padx=5,
    command=onclick_edit_button
)
edit_button.place(x=147, y=195)
delete_all_button = Button(
    root,
    text="DELETE ALL",
    font=(font_name1, 12, "bold"),
    width=10,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4,
    cursor="hand2",
    padx=5
)
delete_all_button.place(x=280, y=195)
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
mark_as_done_button.place(x=12, y=150)
frame = Frame(root, bd=3, width=700, height=280, background=color2)
frame.pack(pady=(160,0))
listbox = Listbox(frame, font=(font_name1, 14, "bold"), width=34, height=20, background=color2, foreground=color5)
listbox.pack(side=LEFT, fill=BOTH, padx=2, expand=True)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
load_tasks_from_db()
root.mainloop()
