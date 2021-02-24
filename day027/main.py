from tkinter import *

window = Tk()
window.title("My First TKinter GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)
# How to create a Label
my_label = Label(text="I Am A Label", font=("Arial", 24, "bold"))

# TKinter pack method https://docs.python.org/3/library/tkinter.html#the-packer
my_label.grid(row=0, column=0)

# Update the label
# my_label["text"] = "New Text"
my_label.config(text="Label", padx=50, pady=50)

# Create a button


def button_clicked():
    print("I was clicked!")
    # Challenge: change the label when the button is clicked
    # my_label.config(text="The Button Was Clicked")
    something = input.get()
    my_label.config(text=something)


def other_button_clicked():
    print("I was also clicked!")


button = Button(text="Button", command=button_clicked)
button.grid(row=1, column=1)

other_button = Button(text="New Button", command=other_button_clicked)
other_button.grid(row=0, column=2)

# Create Entry (like input())
input = Entry(width=10)
input.grid(row=2, column=3)

# while loop that keeps the window alive so that the user can interact
window.mainloop()
