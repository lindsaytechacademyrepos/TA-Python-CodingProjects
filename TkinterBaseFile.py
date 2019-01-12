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

        self.varFname = StringVar() 
        self.varLname = StringVar() #define vars as a string

        """
        self.varFname.set('Bob')
        self.varLname.set('Smith') #set vars using var.set()
        not necessary for real programs but this is how you'd do it
        """

        self.txtFname = Entry(self.master,text=self.varFname,font=("Helvetica",16), fg ='black',bg='lightblue')
        #defines a firstName text box using Tkinter's Entry library, passing in self.master which means the text box belongs on the main screen, and
        #passing in text variable, which will set the value of the text field
        #setting font, foreground, and background as well
        self.txtFname.pack()
        #the command that actually paints it onto the window
        self.txtLname = Entry(self.master,text=self.varLname,font=("Helvetica",16), fg ='black',bg='lightblue')
        #self.txtLname.pack()        


if __name__ =="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
