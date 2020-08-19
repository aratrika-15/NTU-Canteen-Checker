'''The first page, with the function of check date and time'''

from tkinter import *
from PIL import Image, ImageTk
from all_menu import *
from get_date_and_time import *
from current import *

# create the front page, which contains 3 buttons corresponding to
root = Tk()
root.geometry('620x600')
root.title("Northspine canteen app")

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = PIL.Image.open('menupage.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)


menubutton1 = Button(root, fg='black',text='All stall menus and operating hours',
                     command=all_menu,
                     bg='white').place(x=400, y=450)
menubutton2 = Button(root, fg='black',text='Menu for today',bg='white',command=menu_current).place(x=400, y=500)
menubutton3 = Button(root, fg='black', text='Menu for a specific day/time', command=getdateandtime, bg='white').place(x=400, y=550)


root.mainloop()
