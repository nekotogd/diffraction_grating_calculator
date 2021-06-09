"""
Diffraction grating calculator made by Nekoto
Made during Physics and Biology classes
"""

import math #Math library so we can do trigs and stuff
import tkinter as tk #Tkinter for GUI

window = tk.Tk()
window.geometry("300x200")

#Diffraction grating formula nl = d * sin(theta)

values = {}

#Function to check if string is a number
def is_number(value):
    if value.isnumeric():
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

#Function to clear the buttons
def clear_all_buttons():
    button_list = [n, lam, d, theta]
    for b in button_list:
        b.delete(1.0, "end")

#Math functions
def find_theta():
    global values
    global theta
    try:
        result = values['n'] * values['lam']
        result /= values['d']
        result = math.asin(result)
        theta.delete(1.0, "end")
        theta.insert(1.0, str(result))
    except:
        clear_all_buttons()
        values = {}
    return result

def find_n():
    global values
    global n
    try:
        result = math.sin(values["theta"])
        result *= values["d"]
        result /= values["lam"]
        n.delete(1.0, "end")
        n.insert(1.0, str(result))
    except:
        clear_all_buttons()
        values = {}
    return result

def find_d():
    global values
    global d
    try:
        result = values["n"] * values["lam"]
        result /= math.sin(values["theta"])
        d.delete(1.0, "end")
        d.insert(1.0, str(result))
    except:
        clear_all_buttons()
        values = {}
    return result

def find_lam():
    global values
    global lam
    try:
        result = values["d"] * math.sin(values["theta"])
        result /= values["n"]
        lam.delete(1.0, "end")
        lam.insert(1.0, str(result))
    except:
        clear_all_buttons()
        values = {}
    return result

#Function to collect values we'll need later
def take_values():
    global values
    #Make a dictionary so we go over each of the variables we need
    var_dic = {
        n : "n",
        lam : "lam",
        d : "d",
        theta : "theta"}
    #Clear any previous values
    values = {}
    #Go over each of the variables in the formula
    for item in var_dic:
        #Get the text from them in string data type and remove accidental whitespaces
        raw_text = item.get(1.0, "end-1c").strip()
        #Make sure that user entered numbers and values are not empty
        if is_number(raw_text) and raw_text != "":
            values[var_dic[item]] = float(raw_text)
    #Make sure that there are enough variables to solve an equation but not all values are filled, otherwise reset values dictionary
    func_dic = {
        "n" : find_n,
        "lam" : find_lam,
        "d" : find_d,
        "theta" : find_theta}
    if len(values) == 3:
        for key in func_dic:
            if not values.get(key, False):
                func_dic[key]()
    else:
        values = {}

#Create information UI elements
conversion_label = tk.Label(text = "2.5 x 10^-6 is the same as 2.5e-06")

#Create Label and text input for variables
n_label = tk.Label(window, text = "n:")
n_label.config(font = ("Calibri", 14))
n = tk.Text(window, height = 1, width = 22)

lam_label = tk.Label(window, text = "lambda:")
lam_label.config(font = ("Calibri", 14))
lam = tk.Text(window, height = 1, width = 22)

d_label = tk.Label(window, text = "d:")
d_label.config(font = ("Calibri", 14))
d = tk.Text(window, height = 1, width = 22)

theta_label = tk.Label(window, text = "theta:")
theta_label.config(font = ("Calibri", 14))
theta = tk.Text(window, height = 1, width = 22)


calc_button = tk.Button(window, text = "Calculate!", command = take_values)
clear_button = tk.Button(window, text = "Clear values", command = clear_all_buttons)
exit_button = tk.Button(window, text = "Exit", command = window.destroy)

#Arrange all UI elements
conversion_label.grid(column = 1, row = 0, sticky = 'nsew')

n_label.grid(column = 0, row = 1 , sticky = 'nsew')
n.grid(column = 1, row = 1, sticky = 'ew')

lam_label.grid(column = 0, row = 2, sticky = "nsew")
lam.grid(column = 1, row = 2, sticky = "ew")

d_label.grid(column = 0, row = 3, sticky = "nsew")
d.grid(column = 1, row = 3, sticky = "ew")

theta_label.grid(column = 0, row = 4, sticky = "nsew")
theta.grid(column = 1, row = 4, sticky = "ew")

calc_button.grid(column = 0, row = 5, sticky = "nsew")
clear_button.grid(column = 1, row = 5, sticky = "nsew")
exit_button.grid(row = 6, sticky = "nsew")

#Handle resizing for specific rows and/or columns
for i in range(6):
    window.rowconfigure(i, weight = 1)
    window.grid_columnconfigure(0, weight = 1)

window.mainloop()















