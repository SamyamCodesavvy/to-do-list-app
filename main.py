from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
color1 = "#677580"
font_name1 = "Arial"
font_name2 = "Times New Roman"
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
# framing = Frame(root)
# framing.pack(side="top", expand=True, fill="both")
# task_label = Label(framing, text="Enter task here: ", font=(font_name1, 12, "bold"), background="black", foreground="white")
# task_label.place(x=5, y=5)
topbar_image = PhotoImage(file="topbar.png")
Label(root, image=topbar_image).pack()
head_text = Label(root, text="TO-DO LIST", font=(font_name1, 16 ,"bold"), bg=color1, fg= "white")
head_text.place(x=141, y=26)
task_here = Label(root, text="Enter task here:", font=(font_name2, 14, "italic", "bold"), padx=10, pady=5)
task_here.place(y=84)
task_entry = Entry(root, font = (font_name1, 12), width=26)
task_entry.place(x=143, y=84, height=31)

root.mainloop()
