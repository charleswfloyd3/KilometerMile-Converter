from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *

#tkinter packages and modules imported in order to build GUI.

class kilometerconverter:
'''class that creates a kmtom unit converter'''
    def __init__(self):
        self.root = Tk()
        self.title = self.root.title("KILOMETER TO MILE CONVERTER")
        self.font = Font(family = 'Courier', size = 15)
        self.label = Label(master=self.root, text="Enter km:",font=self.font)
        self.convert = Button(master=self.root, text='CONVERT', command=self.convert,font=self.font, width=7)
        self.text_entry = Entry(master=self.root)
        self.result = Label(master=self.root, text='Miles:',font=self.font)
        self.miles = Entry(master=self.root, text='')
        self.b2 = Button(master=self.root, text='CLEAR', command=self.clear, font=self.font, width=7)
        self.b3 = Button(master=self.root, text='QUIT', command=self.closeprogram,font=self.font, width=7)
        self.label.grid(row=0, column=0)
        self.text_entry.grid(row=0, column=1)
        self.convert.grid(row=0, column=2, padx=10, pady=5)
        self.miles.grid(row=1, column=1, padx=10, pady=5)
        self.result.grid(row=1, column=0, padx=10, pady=5)
        self.b2.grid(row=1, column=2, padx=10, pady=5)
        self.b3.grid(row=2, column=2, padx=10, pady=5)
        self.root.bind('<Return>', self.convert)
        self.root.bind('<c>', self.clear)
        self.root.bind('<q>', self.closeprogram)
        self.root.mainloop()
        
    def kmtom(self, event=None):
    '''function that converts kilometers to miles '''
        try:
            km = self.text_entry.get()
            mile = float(km) * 0.621371
            self.miles.insert(0, round(mile, 2))
        except ValueError:
            error_message = 'Oops...please enter a number and try again'
            self.clear()
            showerror(message=error_message)
            
    def mtokm(self, event=None):
    '''function that converts miles to kilometers'''
        try:
            km = self.miles.get()
            mile = (float(km) * 1.60934)
            self.text_entry.insert(0, round(mile,2))
        except:
            error_message = 'Oops...please enter a number and try again'
            self.clear()
            showerror(message=error_message)
            
    def clear(self,even=None):
    '''function that clears both miles and kilometers text entry fields'''
        self.text_entry.delete(0,END)
        self.miles.delete(0,END)
        
    def convert(self):
    '''function that is called when convert button is pushed. the convert function checks to see if miles are being converted to kilometers, or kilometers are
    being converted to miles, then calls either kmtom() or mtokm() accordingly. If content was entered into both the kilometers and miles entry fields, an
    error message box is displayed'''
        if len(self.text_entry.get()) > 0 and len(self.miles.get())>0:
            error_message = 'Oops...enter either km or miles, not both.'
            self.clear()
            showerror(message=error_message)
        elif len(self.miles.get()) > 0:
            self.mtokm()
        elif len(self.text_entry.get())>0:
            self.kmtom()
            
    def closeprogram(self,event=None):
    '''function that closes the program'''
        self.root.destroy()


c = kilometerconverter()

