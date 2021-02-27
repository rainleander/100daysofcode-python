from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #


# ---------------------------- FLIP THE CARDS ------------------------------- #


# ---------------------------- SAVE PROGRESS ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_image)
card_text_title = canvas.create_text(400, 163, text="Title", fill="black", font=("Arial", 40, "italic"))
card_text_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

red_button_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_button_image, highlightthickness=0)
red_button.grid(column=0, row=1)

green_button_image = PhotoImage(file="images/right.png")
green_button = Button(image=green_button_image, highlightthickness=0)
green_button.grid(column=1, row=1)

window.mainloop()

