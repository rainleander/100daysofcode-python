from tkinter import *

window = Tk()
window.title("My First TKinter GUI Program")
window.minsize(width=500, height=300)

# How to create a Label
my_label = Label(text="I Am A Label", font=("Arial", 24, "bold"))

# TKinter pack method https://docs.python.org/3/library/tkinter.html#the-packer
my_label.pack()

# Update the label
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Create a button


def button_clicked():
    print("I was clicked!")
    # Challenge: change the label when the button is clicked
    # my_label.config(text="The Button Was Clicked")
    something = input.get()
    my_label.config(text=something)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Create Entry (like input())
input = Entry(width=10)
input.pack()

# while loop that keeps the window alive so that the user can interact
window.mainloop()
