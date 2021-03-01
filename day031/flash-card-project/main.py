from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
data_dict = {}
# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_word():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(data_dict)
    random_french = random_card["french_word"]
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_text_title, text="French", fill="black")
    canvas.itemconfig(card_text_word, text=f"{random_french}", fill="black")
    flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP THE CARDS ------------------------------- #
def flip_card():
    global random_card
    random_english = random_card["english_word"]
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_text_title, text="English", fill="white")
    canvas.itemconfig(card_text_word, text=f"{random_english}", fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #
def save_progress():
    data_dict.remove(random_card)
    unknown_data = pandas.DataFrame(data_dict)
    unknown_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# ---------------------------- TKINTER UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy McFlasherton Flashface")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_text_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_text_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

red_button_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_button_image, highlightthickness=0, command=next_word)
red_button.grid(column=0, row=1)

green_button_image = PhotoImage(file="images/right.png")
green_button = Button(image=green_button_image, highlightthickness=0, command=save_progress)
green_button.grid(column=1, row=1)

next_word()

window.mainloop()
