from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
color1 = "#677580"
color2 = "#808F9A"
color3= "#D1E0ED"
color4 = "#000000"
color5 = "#FFFFFF"
font_name1 = "Arial"
font_name2 = "Times New Roman"
font_name3 = "Comic Sans MS"
def onclick_add_button():
    retr_task = task_entry.get()
    if retr_task:
        tasks.append(retr_task)
        cursor.execute("insert into tasks values (?)", (retr_task,))
        listbox.delete(0, "END")
        listbox.insert(END, retr_task)
        task_entry.delete(0, END)
    else:
        messagebox.showinfo("Error", "No task in the field.")
def onclick_delete_button():
    try:
        spec_task = listbox.curselection()[0]
        listbox.delete(spec_task)
        tasks.pop(spec_task)
    except:
        messagebox.showinfo("Error", "Select a task to delete.")

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
delete_button.place(x=12, y=150)
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
    # command=onclick_edit_button
)
edit_button.place(x=147, y=150)
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
delete_all_button.place(x=280, y=150)
frame = Frame(root, bd=3, width=700, height=280, background=color2)
frame.pack(pady=(115,0))
listbox = Listbox(frame, font=(font_name2, 10), width=62, height=20, background=color2, foreground=color4)
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
root.mainloop()
