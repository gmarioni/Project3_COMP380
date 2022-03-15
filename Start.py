import tkinter as tk
from tkinter import *
from tkinter import ttk

print("Here we start the coding for project 3!")

class karl ( Frame ):
    def _init_( self ):
        tk.Frame._init_(self)
        self.pack()
        self.master()
        self.master.title("Karlos")
        self.button1 = Button ( self, text = "Click Here", width = 25, command = self.new_window )
        self.button1.grid ( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()
class karl2(Frame):
    def _init_(self):
        new = tk.Frame._init_(self)
        new = Toplevel(self)
        new.title("More window")
        new.button = tk.Button( text = "press to close", width = 25, command = self.close_window)
        new.button.pack()
    def close_window(self):
        self.destroy()
def main():
    karl().mainloop()
if __name__ == '__main__':
    main()