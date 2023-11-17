from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
bg_color1 = "#677580"
font_name1 = "Arial"
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
Label(root, text="ALL TASKS", font=(font_name1, 12 ,"bold"), bg=bg_color1, fg= "white").place(x=80, y=20)



root.mainloop()
