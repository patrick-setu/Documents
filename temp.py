from tkinter import *
import sys

display = Tk()
display.title("Temperature Converter")
display.geometry("500x500")
display.config(background = "#262626")

input_storage = []
conversion_storage = []

input_copy = []
coversion_copy = []

def clear_entry(e):
    sentence_len = len("Enter a temperature")

    for letters in range(sentence_len):
        entry.delete(first=0, last=None)

    entry.unbind("<Button-1>")
    entry.config(foreground="black")


def view_history():
    if len(input_storage) > 0:
        data = ""
        while True:
            if len(input_storage) <= 5:
                break
            input_storage.pop(0)
            conversion_storage.pop(0)

        for one, two in zip(input_storage, conversion_storage):
            data += f"{one} To {two}\n"

        output_screen.config(text = data)
        
    else:
        output_screen.config(text = "There are no conversions in history!")
        output_screen.after(3000, clear_screen)


def clear_screen():
    output_screen.config(text = "")


def export():
    if len(input_copy) > 0:
        print(input_copy)
        export_data = open("Converted Temperatures.txt", "a")
        copy = "Recent conversions:\n"
        for one, two in zip(input_copy, coversion_copy):
                copy += f"{one} To {two}\n"
        export_data.write(f"{copy}\n")
        export_data.close()
        output_screen.config(text = "File has been successfully exported!")
        output_screen.after(3000, clear_screen)

    else:
        output_screen.config(text = "No conversions to export!")
        output_screen.after(3000, clear_screen)
        

def to_cels():
    cels_val = entry.get()
    try:
        check_cels = float(cels_val)
        if check_cels > -237.59:
            input_storage.append(f"{check_cels}°F")
            input_copy.append(f"{check_cels}°F")
            cels_answer = round(((check_cels - 32) * (5/9)), 2)
            output_screen.config(text = f"{cels_answer}°C")
            conversion_storage.append(f"{cels_answer}°C")
            coversion_copy.append(f"{cels_answer}°C")
        else:
            output_screen.config(text="Temperature not possible. Try again")

    except:
        output_screen.config(text="That was not a valid temperature!")
        output_screen.after(3000, clear_screen)


def to_fahr():
    fahr_val = entry.get()
    try:
        check_fahr = float(fahr_val)
        if check_fahr > -459.67:
            input_storage.append(f"{check_fahr}°C")
            input_copy.append(f"{check_fahr}°C")
            fahr_answer = round(((check_fahr * 9/5) + 32), 2)
            output_screen.config(text = f"{fahr_answer}°F")
            conversion_storage.append(f"{fahr_answer}°F")
            coversion_copy.append(f"{fahr_answer}°F")
        else:
            output_screen.config(text="Temperature not possible. Try again")

    except:
        output_screen.config(text="That was not a valid temperature!")


#Input box
entry = Entry(display, font=("Inter", 20), width = 25, relief = FLAT, foreground ="grey")
entry.grid(row=0, column=1, columnspan=5, pady = 40, padx = 60, ipady = 20)
entry.insert(0, "Enter a temperature")
entry.bind("<Button-1>", clear_entry)

#Print output
output_screen = Label(display, font=("Inter", 20), width =24, height = 2,
 background = "white", foreground = "#262626", relief= FLAT, wraplength = 175)
output_screen.grid(row=4, column=1, columnspan=5, pady = 20, padx = 60, ipady = 20)

#Celsius converter button
celsius_button = Button(display, text="To Celsius", font=("Inter", 15), width = 10, cursor = "hand2",
 command = to_cels, background = "#c418de", activebackground = "#c418de", foreground = "#262626")
celsius_button.grid(row=2, column=1, columnspan=2, padx = (60,20), pady = 20)

#Fahrenheit coverter button
fahrenheit_button = Button(display, text="To Fahrenheit", font=("Inter", 15), width = 10, cursor = "hand2",
 command = to_fahr, background = "#c418de", activebackground = "#c418de", foreground = "#262626")
fahrenheit_button.grid(row=2, column=4, columnspan=5, padx = (20,60), pady = 20)

#View history button
history = Button(display, text="View history", font=("Inter", 15), width = 10, cursor = "hand2",
 background = "#c418de", activebackground = "#c418de", foreground = "#262626", command = view_history)
history.grid(row=6, column=1, columnspan=2, padx = (60, 20), pady = 40)

#Export button
export = Button(display, text="Export as", font=("Inter", 15), width = 10, cursor = "hand2",
 background = "#c418de", activebackground = "#c418de", foreground = "#262626", command = export)
export.grid(row=6, column=4, columnspan=5, padx = (20, 60),  pady = 40)

display.mainloop()
