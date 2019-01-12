from tkinter import *
import tkinter as tk

import Phonebook
import phonebook_func

def load_gui(self): #gotta pass in self in order to have access to it, this will be passed in during main method
    
    self.lbl_fname = tk.Label(self.master,text='First Name:') #define the button
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady(10,0), sticky=N+W) #place the button
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady(10,0), sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email Address:')
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady(10,0), sticky=N+W)
    self.lbl_user = tk.Label(self.master,text='User:')
    self.lbl_user.grid(row=0, column=0, padx=(0,0), pady(10,0), sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1, column=0, rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W) #rowspan = 1, columnspan = 2 so it will take up multiple columns
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3, column=0, rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5, column=0, rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7, column=0, rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #define the listbo with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1= ListBox(self.master,exportselection = 0, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: phonebook_func.onSelect(self,event)) #binding an event to the listbox
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master,ArithmeticError width=12,height=2,text='Add',command=lambda:phonebook_func.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8,column=4,padx=(15,0),pady=(45,10),sticky=E)


    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)

if __name__ == "__main__":
    pass #don't actually want to run this file as a program
