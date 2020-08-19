import pandas as pd
import numpy
from waiting_time import *
# importing mudule with waiting_time function

# This is a function to select data based on time,
# because the menu at different time is different.
def stall_info(name_of_stall, time_given, weekday,t3,le,e,t2,l2,b2):
    # function used to print menus of stalls based on current date and time or user defined date and time

    operating_hours_data = pd.read_csv("operating_hours.csv", sep=",")
    stall_menus_data = pd.read_csv("stall_menus.csv", sep=",")
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    # defining a list to store the days of the week
    day_no = days_of_week.index(weekday)
    # find the index from list of days of the week
    dish = stall_menus_data["Dish"]
    # read columns in DataFrames
    price = stall_menus_data["Price"]
    Stall = stall_menus_data["Stall"]
    shop = operating_hours_data["Shop"]

    days_given = stall_menus_data["Days"]
    weekday_chosen = operating_hours_data[weekday]

    days_given1 = list(numpy.array((days_given)))
    # convert the columns of DataFrames into lists

    shop1 = list(numpy.array((shop)))

    dish1 = list(numpy.array((dish)))
    price1 = list(numpy.array((price)))
    Stall1 = list(numpy.array((Stall)))
    weekday_chosen = operating_hours_data[weekday]
    weekday_chosen1 = list(numpy.array(weekday_chosen))

    index_of_shop = shop1.index(name_of_stall)
    m = index_of_shop
    # find the index of stall name from the list of all stalls

    # for m in range(len(shop1)):
    # print the stall name
    t3.insert('insert',"\t\t"+ shop1[m])

    t3.insert('insert','\n')
    if (weekday_chosen1[m]) == "Closed":
        t3.insert('insert',"Shop closed")
        # If the stall is closed on that day,
        # then the function of calculating waiting time will be disabled.
        le.place_forget()
        e.place_forget()
        t2.place_forget()
        l2.place_forget()
        b2.place_forget()
    else:
        # In the previous 'if' statement,
        # it only tells whether the stall is closed on that day,
        # but cannot tell if it is open on that day but closed after operating hours.
        # The 'else' statement make a complementary to that.

        opening_time = (weekday_chosen1[m])[:weekday_chosen1[m].find('-')]
        # gets opening time from the string storing operating hour in format:-opening time-closing time
        closing_time = (weekday_chosen1[m])[weekday_chosen1[m].find('-') + 1:]
        # gets closing time from the string storing operating hour in format:-opening time-closing time
        opening_time_hours = int(opening_time[:opening_time.find(':')])
        # gets opening time hours
        opening_time_minutes = int(opening_time[opening_time.find(':') + 1:])
        # gets the minutes of opening time
        closing_time_hours = int(closing_time[:closing_time.find(':')])
        # gets closing time hours
        closing_time_minutes = int(closing_time[closing_time.find(':') + 1:])
        # gets the minutes of closing time
        time_given_hours = int(time_given[0])
        # extracts the hours from the tuple (hours, minutes)
        time_given_minutes = int(time_given[1])
        # extracts the minutes from the tuple (hours, minutes)

        if time_given_hours < opening_time_hours or time_given_hours> closing_time_hours or (
                time_given_hours == opening_time_hours and time_given_minutes < opening_time_minutes) or (
                time_given_hours == closing_time_hours and time_given_minutes > closing_time_minutes):
            t3.insert('insert',"Shop closed")

            # If the stalled is open on that day but exceeds opening hours,
            # the calculation of waiting time is also disabled.
            le.place_forget()
            e.place_forget()
            t2.place_forget()
            l2.place_forget()
            b2.place_forget()

        else:
            t3.insert('insert','\n')
            t3.insert('insert',"MENU::")
            t3.insert('insert','\n')
            t3.insert('insert','Dish'+'\t\t\t'+'Price(SGD)'+'\n')

            if time_given_hours < 12:
                served_in_breakfast = stall_menus_data["Breakfast"]
                served_in_breakfast1 = list(numpy.array((served_in_breakfast)))
                for j in range(len(Stall1)):
                    if (Stall1[j] == shop1[m]):
                        bits = str(days_given1[j])
                        # finds out whether dish is served on the particular week-day
                        if (bits[day_no] == '1'):
                            if (served_in_breakfast1[j] == 1):
                                t3.insert('insert',dish1[j]+"\t\t\t"+str(price1[j])+'\n')
                                # prints dish and price if served on that week-day and for breakfast
                t3.insert('insert','\n')

            if time_given_hours >= 12 and time_given_hours <= 16:
                # finds out dishes served for lunch
                served_in_lunch = stall_menus_data["Lunch"]
                served_in_lunch1 = list(numpy.array((served_in_lunch)))
                for j in range(len(Stall1)):
                    if (Stall1[j] == shop1[m]):
                        bits = str(days_given1[j])
                        if (bits[day_no] == '1'):
                            if (served_in_lunch1[j] == 1):
                                t3.insert('insert',dish1[j]+"\t\t\t"+str(price1[j])+'\n')
                                # prints dish and price if served on that week-day and for lunch
                t3.insert('insert','\n')

            if time_given_hours > 16:
                # finds out dishes served for dinner
                served_in_dinner = stall_menus_data["Dinner"]
                served_in_dinner1 = list(numpy.array((served_in_dinner)))
                for j in range(len(Stall1)):
                    if (Stall1[j] == shop1[m]):
                        bits = str(days_given1[j])
                        # finds out whether dish is served on the particular week-day
                        if (bits[day_no] == '1'):
                            if (served_in_dinner1[j] == 1):
                                # prints dish and price if served on that week-day and for dinner
                                t3.insert('insert',dish1[j]+"\t\t\t"+str(price1[j])+'\n')

                t3.insert('insert','\n')

    t3.place(x=30,y=20)


