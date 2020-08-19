import pandas as pd
import numpy
from tkinter import*
# Importing the external libraries

# This function define how to calculate waiting times.
# Different stalls have different waiting time per person,
# thus data search is necessary.
# String operation is used here.

def find_waiting_time(stall_no, pax_str, output):
    # print("receive" ,pax_str)
    operating_hours_data = pd.read_csv("operating_hours.csv")
    waiting_time_per_pax = operating_hours_data["WaitingTime"]
    stall_names = operating_hours_data["Shop"]
    waiting_time_per_pax1 = list(numpy.array((waiting_time_per_pax)))
    stall_names1 = list(numpy.array((stall_names)))

    # Create a dictionary to store the waiting time per person for each stall.
    waiting_time_dic = {}
    for i in range(len(stall_names1)):
        waiting_time_dic[stall_names1[i]] = waiting_time_per_pax1[i]
    #     The key is stall_name, value is waiting time per person.


    try:
        pax = int(pax_str)
        if pax < 0:
            messagebox.showinfo("Error", "Sorry, try entering a POSITIVE integer")
        else:
            waiting_time = pax * waiting_time_per_pax1[stall_no]
            output.delete(1.0, 1e10)
            output.insert(1.0, str(waiting_time))
            return waiting_time

    except:
        messagebox.showinfo("Error", "Sorry, try entering an integer")
        return


