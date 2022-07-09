from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


mypass = "Aadi2606"
mydatabase="db"
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


issueTable = "books_issued" 
bookTable = "books" 


def deleteBook():
    
    bid = bookInfo1.get()
    
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.geometry("600x500")

    
    background = PhotoImage(file ="F:\\12th project\\img\\delete_books.png")
    bg1_label = Label(root, image = background) 
    bg1_label.place(x = 0, y = 0)
    
   
    bookInfo1 = Entry(root)
    bookInfo1.place(relx=0.27,rely=0.53, relwidth=0.45, relheight=0.067)
    
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.1,rely=0.87, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.43,rely=0.87, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

delete()