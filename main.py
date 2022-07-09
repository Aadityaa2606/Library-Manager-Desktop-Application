from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *


mypass = "Aadi2606"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root",
                      password=mypass, database=mydatabase)

cur = con.cursor()
root = Tk()
root.title("Library Manager")
root.geometry("600x500")
background = PhotoImage(file="F:\\12th project\\img\\SISHYA SCHOOL.png")
label1 = Label(root, image=background)
label1.place(x=0, y=0)

b1 = PhotoImage(file="F:\\12th project\\img\\addbooks.png")
b2 = PhotoImage(file="F:\\12th project\\img\\deletebooks.png")
b3 = PhotoImage(file="F:\\12th project\\img\\booklist.png")
b4 = PhotoImage(file="F:\\12th project\\img\\issuebook.png")
b5 = PhotoImage(file="F:\\12th project\\img\\returnbooks.png")

btn1 = Button(root, image=b1, command=addBook)
btn1.place(relx=0.08, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, image=b2, command=delete)
btn2.place(relx=0.08, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, image=b3, command=View)
btn3.place(relx=0.08, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, image=b4, command=issueBook)
btn4.place(relx=0.08, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, image=b5, command=returnBook)
btn5.place(relx=0.08, rely=0.8, relwidth=0.45, relheight=0.1)


root.mainloop()
