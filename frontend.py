from tkinter import *
import os
from backend import Database
from guiwidgets.listview import MultiListbox

database = Database("store.db")

creds = 'tempfile.temp'

def Signup():
        global pwordE
        global nameE
        global roots

        roots = Tk()
        roots.title('Signup')
        instruction = Label(roots, text='Please Enter new Credentials')
        instruction.grid(row=0, column=0, sticky=E)

        nameL = Label(roots, text='New Username: ')
        pwordL = Label(roots,text='New Password: ')
        nameL.grid(row=1, column=0, sticky=W)
        pwordL.grid(row=2, column=0, sticky=W)
        nameE = Entry(roots)
        pwordE = Entry(roots, show='*')
        nameE.grid(row=1, column=1)
        pwordE.grid(row=2, column=1)

        signupButton = Button(roots, text='Signup', command=FSSignup)
        signupButton.grid(columnspan=2, sticky=W)
        roots.mainloop()

def FSSignup():
        with open(creds, 'w') as f:
                f.write(nameE.get())
                f.write('\n')
                f.write(pwordE.get())
                f.close()

        roots.destroy()
        Login()

def Login():
        global nameEL
        global pwordEL
        global rootA

        rootA = Tk()
        rootA.title('Login')

        instruction = Label(rootA, text='Please Login\n')
        instruction.grid(sticky=E)

        nameL = Label(rootA, text='Username: ')
        pwordL = Label(rootA, text='Password: ')
        nameL.grid(row=1, sticky=W)
        pwordL.grid(row=2, sticky=W)

        nameEL = Entry(rootA)
        pwordEL = Entry(rootA, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)

        loginB = Button(rootA, text='Login', command=CheckLogin)
        loginB.grid(columnspan=2, sticky=W)

        rmuser = Button(rootA, text='Sign Up', fg='red', command=DelUser)
        rmuser.grid(columnspan=2, sticky=W)
        rootA.mainloop()

def CheckLogin():
        with open(creds) as f:
                data = f.readlines()
                uname = data[0].rstrip()
                pword = data[1].rstrip()

        if nameEL.get() == uname and pwordEL.get() == pword:
                r = Tk()
                r.title(':D')
                r.geometry('150x50')
                rlbl = Label(r, text='\n[+] Logged In')
                rlbl.pack()
                r.destroy()
                rootA.destroy()
                r.mainloop()
        else:
                r = Tk()
                r.title('D:')
                r.geometry('150x50')
                rlbl = Label(r, text='\n[! Invalid Login')
                rlbl.pack()
                r.mainloop()

def DelUser():
        os.remove(creds)
        rootA.destroy()
        Signup()

if os.path.isfile(creds):
        Login()
else:
        Signup()


class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("The Buyers Stop")

        l1 = Label(window, text="Product")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Seller")
        l2.grid(row=1, column=0)

        l3 = Label(window, text="Price")
        l3.grid(row=2, column=0)

        l4 = Label(window, text="Qty")
        l4.grid(row=3, column=0)

        l5 = Label(window, text="Your total")
        l5.grid(row=15, column=0)

        self.product_text = StringVar()
        self.e1 = Entry(window, textvariable=self.product_text)
        self.e1.grid(row=0, column=1)

        self.seller_text = StringVar()
        self.e2 = Entry(window, textvariable=self.seller_text)
        self.e2.grid(row=1, column=1)

        self.price_text = StringVar()
        self.e3 = Entry(window, textvariable=self.price_text)
        self.e3.grid(row=2, column=1)

        self.qty_text = StringVar()
        self.e4= Entry(window, textvariable=self.qty_text)
        self.e4.grid(row=3, column=1)

        self.sum_text = StringVar()
        self.e5= Entry(window, textvariable=self.sum_text)
        self.e5.grid(row=15, column=1)

        #self.window = Listbox(window, height=8, width=35)
        #self.window.grid(row=5, column=0, rowspan=8, columnspan=2)
        #self.window.bind('<<ListboxSelect>>', self.get_selected_row)
        self.list2 = MultiListbox(window,(('id',10),('Product',20),('Seller',20),('Price',20),('Qty',10)))
        self.list2.grid(row=6, column=0, rowspan=8, columnspan=2)
##        sb1 = Scrollbar(self.list2)
##        sb1.grid(row=5, column=2, rowspan=6)
##        self.list2.config(yscrollcommand=sb1.set)
##        sb1.config(command=self.list2.yview)
        b1 = Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=0, column=2)
        # b2 = Button(window, text="Search entry", width=12, command=self.search_command)
        # b2.grid(row=3, column=3)

        b2 = Button(window, text="Add entry", width=12, command=self.add_command)
        b2.grid(row=1, column=2)

        b3 = Button(window, text="Update selected", width=12, command=self.update_command)
        b3.grid(row=2, column=2)

        b4 = Button(window, text="Delete selected", width=12, command=self.delete_command)
        b4.grid(row=3, column=2)

        b5 = Button(window, text="Close", width=12, command=window.destroy)
        b5.grid(row=4, column=2)


    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list2.curselection()
            self.selected_tuple = self.list2.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def view_command(self):
        self.list2.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        for row in database.view():
            self.list2.insert(END, row)

    # def search_command(self):
    #     self.window.delete(0, END)
    #     for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()):
    #         self.window.insert(END, row)

    def add_command(self):
        database.insert(self.product_text.get(), self.seller_text.get(), self.price_text.get(), self.qty_text.get())
        self.list2.delete(0, END)
        self.list2.insert(END, (self.product_text.get(), self.seller_text.get(), self.price_text.get(), self.qty_text.get()))

    def delete_command(self):
        #database.delete(self.selected_tuple[0])
        
        window1=Tk()
        self.label=Label(window1, text="Enter Product Name you want to delete")
        self.label.grid(row=1,column=0)
        self.id_text = StringVar()
        self.entry=Entry(window1,textvariable=self.id_text)
        self.entry.grid(row=2,column=0)
        #self.x=self.name_text.get()
        self.but = Button(window1, text="Delete", width=12,command=database.delete(self.id_text.get()))
        self.but.grid(row=3, column=0)
        self.view_command()
        #l3 = Label(window1, text="Price")
        #l3.grid(row=2, column=0)

        


    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[0],self.product_text.get(), self.seller_text.get(), self.price_text.get(), self.qty_text.get())
        self.view_command()


#code for the GUI (front end)
window = Tk()
Window(window)
window.mainloop()
