import pandas as pd
import numpy
from tkinter import *
from tkinter import scrolledtext
#importing external libraries needed


# Create a new window for displaying all the menus and operating hours of all stalls
# regardless of time
def all_menu():
    all_menu=Toplevel()
    all_menu.title('All menus of North Spine')
    all_menu.geometry('500x400')

    l_all=Label(all_menu,text='All the menus of North Spine').pack()

    # Since the information is too much,
    # we use a tool called 'scrolledtext' in tkinter
    # which can avoid limitations of the window size
    t_all=scrolledtext.ScrolledText(all_menu)

    def print_all_stall_menu() :
        operating_hours_data = pd.read_csv("operating_hours.csv", sep=",")
        stall_menus_data = pd.read_csv("stall_menus.csv", sep=",")
        # storing data from csv files as DataFrames

        dish = stall_menus_data["Dish"]         # making lists out of the columns
        price = stall_menus_data["Price"]       # cuisines of stalls stored
        Stall = stall_menus_data["Stall"]       # locations of stalls stored
        shop = operating_hours_data["Shop"]     # shop names stored
        weekdays = operating_hours_data["Wkdays"]       # stores operating hours on weekdays
        saturday = operating_hours_data["Saturday"]     # stores operating hours on Saturday
        sunday = operating_hours_data["Sunday"]         # stores operating hours on Sunday
        cuisine = operating_hours_data["Cuisine"]       # stores dish names
        location = operating_hours_data["Location"]     # stores prices
        days_given = stall_menus_data["Days"]           # stores stall names

        days_given1 = list(numpy.array((days_given)))
        cuisine1 = list(numpy.array((cuisine)))
        location1 = list(numpy.array((location)))
        shop1 = list(numpy.array((shop)))
        weekdays1 = list(numpy.array((weekdays)))
        saturday1 = list(numpy.array((saturday)))
        sunday1 = list(numpy.array((sunday)))
        dish1 = list(numpy.array((dish)))
        price1 = list(numpy.array((price)))
        Stall1 = list(numpy.array((Stall)))

        for m in range(len(shop1)):
            t_all.insert('insert', '----------------------------------\n')
            t_all.insert('insert',"\n\n"+shop1[m]+'\n\n')
            t_all.insert('insert',"Cuisine:-"+ cuisine1[m]+'\n')
            t_all.insert('insert',"Location:-"+location1[m]+'\n')
            t_all.insert('insert','\n')
            # printing stall information

            t_all.insert('insert',"Operating hours on weekdays ::           "+ weekdays1[m]+'\n')
            t_all.insert('insert',"Operating hours on Saturday ::           "+saturday1[m]+'\n')
            t_all.insert('insert',"Operating hours on Sunday ::           "+sunday1[m]+'\n')
            t_all.insert('insert','\n')
            # printing operating hours
            t_all.insert('insert',"MENU::"+'\n')
            t_all.insert('insert','\n')
            for j in range(len(Stall1)):
                if (Stall1[j] == shop1[m]):
                    t_all.insert('insert',dish1[j]+"\n")
                    # printing menus

    print_all_stall_menu()
    t_all.pack()
    all_menu.mainloop()




