from certain_menu import*
#import module so that function to print specific menu can be used
import datetime
# external library datetime imported
import PIL
from PIL import Image, ImageTk

# A function to get user input(specific date&time defined by them)
def getdateandtime():
    window1 = Tk()
    window1.title('Select based on time/date')
    window1.configure(background='orange')
    window1.geometry('300x150')

    # ask for date in dd/mm/yyyy format
    input1 = Label(window1,bg='orange',fg='black', text="Input date in DD/MM/YYYY format: ")
    input1.place(x=0, y=30)
    entrydate = Entry(window1,width=12)
    entrydate.place(x=210, y=30)
    entrydate.focus_set()

    # ask for time in HH:MM format
    input2 = Label(window1,bg='orange',fg='black', text="Input time in HH:MM format: ")
    input2.place(x=0, y=60)
    entrytime = Entry(window1,width=10)
    entrytime.place(x=170, y=60)
    entrytime.focus_set()


    #In case users may input an invalid date&time,
    # a part to do error handling is neccesary(try-except).
    # It can both remind users to key in correct date&time
    # as well as make sure the application would not be terminated

    def checkdateandtime():
        try:
            # fetching user input date and time
            date = entrydate.get()
            time = entrytime.get()

             # using string operations to get hours and minutes
            # strings are converted into integers
            hours = int(time[:time.find(':')])
            minutes = int(time[time.find(':') + 1:])

            if (hours < 0 or hours > 24 or minutes < 0 or minutes > 59 or (hours==24 and minutes>0)):
             # error handling for input time
                messagebox.showinfo("Error", "wrong format for date and time. please try again!")

            # datetime.datetime.strptime(time, '%H:%M')
            # time=str(time)
            day, month, year = date.split('/')
            # datetime.datetime(int(year), int(month), int(day))
            date=datetime.datetime(int(year), int(month), int(day))
            print(date)
            print(hours)
            print(minutes)

            #hours = int(time[:time.find(':')])
            # minutes = int(time[:time.find(':') + 1:])
            time=(hours,minutes)
            print(time)

            # name of weekday stored in week_day
            current_week_day=date.weekday()
            days_of_the_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            week_day = (days_of_the_week[(current_week_day + 2) % 7])
            print(week_day)

        except ValueError:
            # error handling for input date and time
            messagebox.showinfo("Error", "wrong format for date and time. please try again!")

        else:
            window = Toplevel()
            window.geometry('400x410')

            def resize_image(event):
                new_width = event.width
                new_height = event.height
                image = copy_of_image.resize((new_width, new_height))
                photo = ImageTk.PhotoImage(image)
                label.config(image=photo)
                label.image = photo  # avoid garbage collection

            image = PIL.Image.open('bg3.jpg')
            copy_of_image = image.copy()
            photo = ImageTk.PhotoImage(image)
            label = ttk.Label(window, image=photo)
            label.bind('<Configure>', resize_image)
            label.pack(fill=BOTH, expand=YES)

            selectprompt = Label(window, text="please select your designated restaurant")
            selectprompt.pack()

            photo_list = []
            # in case the pictures on the buttons cannot display

            # This create_function is used to create buttons for choosing restaurants,
            # the innovative part is that we use images of each stall to serve as button
            # so that the interface is quite user friendly.
            # The concept of using function is due to similarity of creating buttons for all stalls
            # The usage of function can make us focus more on how to create it
            # rather than to focus on differences among buttons.
            # The different features are just regarded as parameters.
            # Therefore, the structure is concise and not error-prone.
            def create_button(stall_name, stall_no, img_file, px, py,time,weekday):

                photo = ImageTk.PhotoImage(file=img_file)
                photo_list.append(photo)

                # When user click on the image button of a stall,
                # another function named create_stall is called,
                # which opens a new window with menu displayed and the function of calculating waiting time
                stall_button = Button(window, image=photo, width="70", height="57"
                                      , command=lambda name=stall_name, no=stall_no,
                                                       time=time,weekday=weekday:
                                        create_stall(name, no,time,weekday))
                stall_button.place(x=px, y=py)
                stall_label=Label(window,text=stall_name,bg='gold')
                stall_label.place(x=px,y=py+65)


            # Call the create_button function 10 times for 10 different times
            # The first 5 arguments passed to function are those different features,
            # the last 2 arguments are useful information for other functions inside the create_button.
            # It looks much clearer than not using function,
            # the space is also saved.
            create_button('McDonalds', 0, "macs.jpg", 72, 50,time,week_day)
            create_button('Mr.Bean', 1, "mrbean.jpg",162, 50, time, week_day)
            create_button('Subway', 2, "Subway.png",252, 50, time, week_day)
            create_button('BakeryCuisine', 3, "bakery.jpg", 72, 140, time, week_day)
            create_button('MalaHotPot', 4, "mala.jpg", 162, 140, time, week_day)
            create_button('Italian', 5, "italian.jpg", 252, 140, time, week_day)
            create_button('Salad', 6, "salad.jpg", 72, 230, time, week_day)
            create_button('FruitJuice', 7, "fruitjuice.jpg", 162, 230, time, week_day)
            create_button('ChickenRice', 8, "chickenrice.jpg", 252, 230, time, week_day)
            create_button('Indian', 9, "indian.jpg", 162, 320, time, week_day)

            window.mainloop()


    # After inputting a time and press confirm button,
    # the function checkdateandtime is called to check
    # whether it is a valid time or not.
    button_confirm = Button(window1,fg='black',bg='orange', text="Load Menus", command=checkdateandtime)
    button_confirm.place(x=110, y=90)
    window1.mainloop()
