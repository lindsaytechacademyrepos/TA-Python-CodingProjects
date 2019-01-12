import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varBrowse1 = StringVar() 
        self.varBrowse2 = StringVar() #define vars as a string

        """
        self.varFname.set('Bob')
        self.varLname.set('Smith') #set vars using var.set()
        not necessary for real programs but this is how you'd do it
        """

        self.lblBrowse1 = Label(self.master,text='First Name', font = ('Helvetica',16), fg ='black',bg='lightblue')
        self.lblBrowse1.grid(row=0,column=0, padx=(30,0),pady=(30,0))
        self.lblBrowse2 = Label(self.master,text='Last Name', font = ('Helvetica',16), fg ='black',bg='lightblue')
        self.lblBrowse2.grid(row=1,column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay=Label(self.master,text='', font = ('Helvetica',16), fg ='black',bg='lightblue')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))

        self.txtBrowse1 = Entry(self.master,text=self.varFname,font=("Helvetica",16), fg ='black',bg='lightblue') #defines a firstName text box using Tkinter's Entry library, passing in self.master which means the text box belongs on the main screen, and passing in text variable, which will set the value of the text field setting font, foreground, and background as well
        self.txtBrowse1.grid(row=0,column=1, padx=(30,0),pady=(30,0)) #the command that actually paints it onto the window
        self.txtBrowse2 = Entry(self.master,text=self.varLname,font=("Helvetica",16), fg ='black',bg='lightblue')
        self.txtBrowse2.grid(row=1,column=1,padx=(30,0),pady=(30,0))

        self.btnCheck = Button(self.master,text='Submit',font=("Helvetica",16), fg ='black',bg='lightblue',command=self.submit)
        self.btnCheck.grid(row=2,column=1, pady=(30,0),sticky=NE)
        self.btnClose = Button(self.master,text='Cancel',font=("Helvetica",16), fg ='black',bg='lightblue',command=self.cancel)
        self.btnClose.grid(row=2,column=1, padx=(0,90),pady=(30,0),sticky=NE)

    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()


if __name__ =="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
