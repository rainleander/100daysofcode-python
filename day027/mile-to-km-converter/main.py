from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300, height=100)
window.config(padx=50, pady=50)


def calculate_button():
    kms = int(input.get()) * 1.60934
    km_calculation_label.config(text=kms)


input = Entry(width=10)
input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_calculation_label = Label(text="0")
km_calculation_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=calculate_button)
calc_button.grid(row=2, column=1)

window.mainloop()
