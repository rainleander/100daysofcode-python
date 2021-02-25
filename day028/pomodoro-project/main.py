from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_label.config(text="Timer")
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_time)
        main_label.config(text="Break", font=(FONT_NAME, 50), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_time)
        main_label.config(text="Break", font=(FONT_NAME, 50), bg=YELLOW, fg=PINK)
    else:
        countdown(work_time)
        main_label.config(text="Work", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 != 0:
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += "✓"
            checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

main_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
main_label.grid(row=0, column=1)

checkmarks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
checkmarks.grid(row=3, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
