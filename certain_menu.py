from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
import numpy
import pandas as pd
from stall_info import *

# The function create_stall uses the same concept of create_button,
# because there is a big similarity of creating menu page for all stalls.
# It saves both time and space when writing program,
# and it is also reusable when this module is imported in other files.
def create_stall(stall_name, stall_no,time,weekday):
    stall_Window = Toplevel()
    stall_Window.geometry('300x300')
    stall_Window.title(stall_name)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # avoid garbage collection

    # Create background for menu of a specific stall
    image = PIL.Image.open('bg.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(stall_Window, image=photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand=YES)

    # The stall name is at the top
    l=Label(stall_Window, text=stall_name)
    l.place(x=100, y=30)
    # These five elements are used to get user input of number of queueing people
    # and then calculate waiting time
    # 1. An instruction
    le=Label(stall_Window, text="How many people?")
    le.place(x=20, y=230)
    # 2. Get user input
    e=Entry(stall_Window, show=None, width=6)
    e.place(x=200,y=230)
    no_of_pax=e.get()
    # 3. Display the time needed
    t2=Text(stall_Window,width=6,height=1.5)
    t2.place(x=200,y=260)
    l2=Label(stall_Window,text='minutes')
    l2.place(x=246,y=263)
    # 4. Press the button to calculate
    b2=Button(stall_Window,text='Calculate waiting time',width= 20,bg='white',
                  command=lambda no=stall_no, entry=e, output=t2: find_waiting_time(no, entry.get(), output)
                  )
    b2.place(x=20,y=260)
    # This text lists the menus of a stall(dishes&price)
    # Now it is empty.
    t3=Text(stall_Window,width=34,height=13)
    # After the following function is called, the menu can be displayed.
    stall_info(stall_name,time,weekday,t3,le,e,t2,l2,b2)

    stall_Window.mainloop()
