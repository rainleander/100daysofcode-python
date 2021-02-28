from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")


def next_word():
    random_card = random.choice(data_dict)
    random_french = random_card["french_word"]
    canvas.itemconfig(card_text_title, text="French")
    canvas.itemconfig(card_text_word, text=f"{random_french}")

# ---------------------------- FLIP THE CARDS ------------------------------- #
# TODO: flip the cards every three seconds (3000ms)

# ---------------------------- SAVE PROGRESS ------------------------------- #


# ---------------------------- TKINTER UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy McFlasherton Flashface")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_image)
card_text_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_text_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

red_button_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_button_image, highlightthickness=0, command=next_word)
red_button.grid(column=0, row=1)

green_button_image = PhotoImage(file="images/right.png")
green_button = Button(image=green_button_image, highlightthickness=0, command=next_word)
green_button.grid(column=1, row=1)

next_word()

window.mainloop()
