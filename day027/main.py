import tkinter

window = tkinter.Tk()
window.title("My First TKinter GUI Program")
window.minsize(width=500, height=300)

# How to create a Label
my_label = tkinter.Label(text="I Am A Label", font=("Arial", 24, "bold"))

# TKinter pack method https://docs.python.org/3/library/tkinter.html#the-packer
my_label.pack()

# while loop that keeps the window alive so that the user can interact
window.mainloop()
