"""
Diffraction grating calculator made by Nekoto
Made during Physics and Biology classes
"""

import math #Math library so we can do trigs and stuff
import tkinter as tk #Tkinter for GUI

window = tk.Tk()
window.geometry("300x170")

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

#Math functions
def find_theta():
    global values
    global theta
    result = values['n'] * values['lam']
    result /= values['d']
    result = math.asin(result)
    theta.delete(1.0, "end")
    theta.insert(1.0, str(result))
    return result

def find_n():
    global values
    global n
    result = math.sin(values["theta"])
    result *= values["d"]
    result /= values["lam"]
    n.delete(1.0, "end")
    n.insert(1.0, str(result))
    return result

def find_d():
    global values
    global d
    result = values["n"] * values["lam"]
    result /= math.sin(values["theta"])
    d.delete(1.0, "end")
    d.insert(1.0, str(result))
    return result

def find_lam():
    global values
    global lam
    result = values["d"] * math.sin(values["theta"])
    result /= values["n"]
    lam.delete(1.0, "end")
    lam.insert(1.0, str(result))
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
     

#Function to clear the buttons
def clear_all_buttons():
    button_list = [n, lam, d, theta]
    for b in button_list:
        b.delete(1.0, "end")

#Create Label and text input for variables
n_label = tk.Label(window, text = "n:")
n_label.config(font = ("Calibri", 14))
n = tk.Text(window, height = 1, width = 52)

lam_label = tk.Label(window, text = "lambda:")
lam_label.config(font = ("Calibri", 14))
lam = tk.Text(window, height = 1, width = 52)

d_label = tk.Label(window, text = "d:")
d_label.config(font = ("Calibri", 14))
d = tk.Text(window, height = 1, width = 52)

theta_label = tk.Label(window, text = "theta:")
theta_label.config(font = ("Calibri", 14))
theta = tk.Text(window, height = 1, width = 52)


calc_button = tk.Button(window, text = "Calculate!", command = take_values)
clear_button = tk.Button(window, text = "Clear values", command = clear_all_buttons)
exit_button = tk.Button(window, text = "Exit", command = window.destroy)

#Arrange all UI elements
n_label.grid(column = 0, row = 0)
n.grid(column = 1, row = 0)

lam_label.grid(column = 0, row = 1)
lam.grid(column = 1, row = 1)

d_label.grid(column = 0, row = 2)
d.grid(column = 1, row = 2)

theta_label.grid(column = 0, row = 3)
theta.grid(column = 1, row = 3)

calc_button.grid(column = 0, row = 4)
clear_button.grid(column = 1, row = 4, sticky = "w")
exit_button.grid(row = 5)

window.mainloop()















