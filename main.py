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
def set_cursor_position(event):
    task_entry.icursor(5)
root = Tk()
root.title("To-Do List App")
root.iconbitmap("to_do_list_icon.ico")
root.resizable(False,False)
root.geometry("400x550+400+80")
root.config()
db_connect = sql.connect("TodoTaskLists.db")
cursor = db_connect.cursor()
cursor.execute("create table if not exists tasks (title text)")
tasks = []
topbar_image = PhotoImage(file="topbar.png")
Label(root, image=topbar_image).pack()
head_text = Label(root, text="TO-DO LIST", font=(font_name1, 16 ,"bold"), background=color1, foreground=color5)
head_text.place(x=141, y=26)
task_here = Label(root, text="Enter task:", font=(font_name2, 14, "italic", "bold"), padx=7, pady=5)
task_here.place(y=105)
task_entry = Entry(root, font=(font_name1, 12, "bold"), width=25, background=color2, foreground=color5)
task_entry.place(x=107, y=105, height=33)
task_entry.focus()
add_button = Button(
    root,
    text="ADD",
    font=(font_name1, 12, "bold"),
    width=4,
    background=color4,
    foreground=color5,
    activebackground=color3,
    activeforeground=color4)
add_button.place(x=337, y=105)
delete_button = Button(
    root,
    text="Delete",

)
root.mainloop()
