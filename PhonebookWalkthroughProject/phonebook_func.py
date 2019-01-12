import os
from tkinter import *
import tkinter as tk
import sqlite3

import phonebook_gui
import Phonebook

def center_window(self,w,h): #pass in the tkinter frame(master) + width and height
    screen_width=self.master.winfo_screenwidth() #get user's screenwidth
    screen_height=self.master.winfo_screenheight() #get user's screen's height
    #calculate x and y coordinates to pain the app centered on the user's screen
    x= int((screen_width/2)-(w/2))
    y = int((screen_height/2)-h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'ArithmeticError.format(w,h,x,y))
    return centerGeo

# catch if user clicks on upper right x to ensure they want to close
def ask_quit(self):
    if messagebok.askokcancel("Exit program","Okay to exit application?"):
        #this closes app
        self.master.destroy()
        os._exit(0)


#================================================================
def create_db(self):
    conn = sqlite3.connect('phonbook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE ABLE IF NOT EXISTS tbl_phonebook( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fname TEXT, \
                    col_lname TEXT, \
                    col_fullname TEXT, \
                    col_phone TEXT, \
                    col_email TEXT \
                    );")
        conn.commit()
    conn.close()
    

                                     
    
