from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km")
window.minsize(width=200, height=200)
window.config(padx=10, pady=10)

miles_label = Label(text="Enter Miles :")
miles_label.grid(column=0, row=0)
miles_label.config(padx=10, pady=10)

entry = Entry(width=20)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

km_label = Label(text="Kilometer equal to")
km_label.grid(column=0, row=1)
km_label.config(padx=10, pady=10)

convert_label = Label(text="0 km")
convert_label.grid(column=1, row=1)
convert_label.config(padx=10, pady=10)

def miles_to_km():
    miles = int(entry.get())
    km = round(1.609344 * miles)
    return km

def cal():
    convert_label.config(text=f"{miles_to_km()} km")

button = Button(text="Calulate", command=cal)
button.grid(column=1, row=2)





window.mainloop()

