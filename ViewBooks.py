from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "Aadi2606"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books" 
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.geometry("600x500")

    background = PhotoImage(file = "F:\\12th project\\img\\view_books.png") 
   
    label4 = Label( root, image = background) 
    label4.place(x = 0, y = 0) 
    
    y = 0.35
    
    Label(root, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.06,rely=0.37)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(root,text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
           
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

View()