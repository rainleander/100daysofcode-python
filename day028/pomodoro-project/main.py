from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    while reps < 9:
        if reps == 0 or reps == 2 or reps == 4 or reps == 8:
            count_down(work_sec)
            timer_label.config(text="Work", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
        elif reps == 7:
            count_down(long_break_sec)
            timer_label.config(text="Break", font=(FONT_NAME, 50), fg=RED, bg=YELLOW)
        else:
            count_down(short_break_sec)
            timer_label.config(text="Break", font=(FONT_NAME, 50), fg=PINK, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    if count_min == 0:
        count_min = "00"
    elif count_min < 10:
        count_min = f"0{count_min}"
    else:
        count_min = count_min
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    else:
        count_sec = count_sec
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = "✓"
        if reps % 2 == 0:
            checks = ''.join([char*(reps/2) for char in check])
            checkmarks.config(text=checks, font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=20, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmarks = Label(text="", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
