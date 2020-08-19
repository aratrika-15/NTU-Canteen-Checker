from certain_menu import*
# importing module so that function to display specific menus can be used

import datetime
# importing external library datetime

from PIL import Image, ImageTk

# This is a function used to get current date&time from system
# a module called 'datetime' is imported here
def get_current_date_time():
    from datetime import datetime
    # datetime object containing current date and time
    now = datetime.now()
    current_weekday = now.weekday()
    # index number of weekday stored

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    # converting datetime object into a string
    current_time = dt_string[dt_string.find(' ') + 1:]
    # current_time in hours and minutes obtained using string operations
    return [current_weekday, current_time]

def menu_current():
    current_list = get_current_date_time()
    current_time= current_list[1]
    time = (int(current_time[:current_time.find(':')]), int(current_time[current_time.find(':') + 1:]))
    # time is a tuple of (hours,minutes)
    days_of_the_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    # list storing days of the week
    current_weekday = (days_of_the_week[(current_list[0] + 2) % 7])
    # current_weekday stores name of the day of week

    window = Toplevel()
    window.geometry('400x410')
    selectprompt = Label(window, text="please select your designated restaurant")
    selectprompt.pack()

    #The following function creates background for the choosing restaurants page.

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

    # In case the pictures on the buttons cannot display (inside the create_button function),
    # we have to use a list to store them outside the function
    # or it will be collected as garbage
    photo_list = []

    # Since there is total 10 restaurants to be selected,
    # it will be a tedious work for us to create buttons for each stall one by one,
    # so we define a function to reduce the repetitive process
    # common features are stated in the function,
    # different features are regarded as parameters
    # [The same thing is done for the create_stall function, which is called inside the create_button function]
    def create_button(stall_name, stall_no, img_file, px, py, time, weekday):
        # After users choose a specific time, then they have to select a specific restaurant
        # in this interface, we use the logo images to serve as buttons as well as the stall names as labels
        # therefore, this page is both beautiful and user-friendly

        photo = ImageTk.PhotoImage(file=img_file)
        photo_list.append(photo)
        stall_button = Button(window, image=photo, width="70", height="57"
                              , command=lambda name=stall_name, no=stall_no,
                                               time=time, weekday=weekday:
                               create_stall(name, no, time, weekday))
        stall_button.place(x=px, y=py)
        stall_label = Label(window, text=stall_name, bg='gold')
        stall_label.place(x=px, y=py + 65)

    # After defining the function, we can just pass all the arguments and call it
    create_button('McDonalds', 0, "macs.jpg", 72, 50, time,  current_weekday)
    create_button('Mr.Bean', 1, "mrbean.jpg", 162, 50, time,  current_weekday)
    create_button('Subway', 2, "Subway.png", 252, 50, time,  current_weekday)
    create_button('BakeryCuisine', 3, "bakery.jpg", 72, 140, time,  current_weekday)
    create_button('MalaHotPot', 4, "mala.jpg", 162, 140, time,  current_weekday)
    create_button('Italian', 5, "italian.jpg", 252, 140, time,  current_weekday)
    create_button('Salad', 6, "salad.jpg", 72, 230, time,  current_weekday)
    create_button('FruitJuice', 7, "fruitjuice.jpg", 162, 230, time,  current_weekday)
    create_button('ChickenRice', 8, "chickenrice.jpg", 252, 230, time,  current_weekday)
    create_button('Indian', 9, "indian.jpg", 162, 320, time,  current_weekday)

    window.mainloop()
