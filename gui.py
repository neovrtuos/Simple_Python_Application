# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Fun Functions")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='Addition')
item.add_command(label='Multiplication')
menu.add_cascade(label='Math', menu=item)
root.config(menu=menu)

# Make the window resizable
root.resizable(True, True)

# Execute Tkinter
mainloop()