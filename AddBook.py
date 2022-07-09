from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)

    root.destroy()


def addBook(): 
    
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
    
    mypass = "Aadi2606"
    mydatabase="db"
    con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    bookTable = "books"     

    root = Tk()
    root.title("Library")
    root.geometry("600x500")
    background = PhotoImage(file ="F:\\12th project\\img\\add_books.png")
    bg1_label = Label(root, image = background) 
    bg1_label.place(x = 0, y = 0)               

    # Book ID
    lb1 = Label(root)
    lb1.place(relx=0.05,rely=0.35, relheight=0)
    bookInfo1 = Entry(root)
    bookInfo1.place(relx=0.3,rely=0.33 , relwidth=0.45, relheight=0.07)
        
    # Title
    lb2 = Label(root)
    lb2.place(relx=0.05,rely=0.45, relheight=0)
    bookInfo2 = Entry(root)
    bookInfo2.place(relx=0.3,rely=0.5, relwidth=0.45, relheight=0.07)
       
    # Book Author
    lb3 = Label(root)
    lb3.place(relx=0.05,rely=0.55, relheight=0)
    bookInfo3 = Entry(root)
    bookInfo3.place(relx=0.3,rely=0.65, relwidth=0.45, relheight=0.07)
        
    # Book Status
    lb4 = Label(root)
    lb4.place(relx=0.05,rely=0.65, relheight=0)
    bookInfo4 = Entry(root)
    bookInfo4.place(relx=0.4,rely=0.81, relwidth=0.38, relheight=0.07)
        
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.1,rely=0.9, relwidth=0.18,relheight=0.08)
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.43,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

addBook()