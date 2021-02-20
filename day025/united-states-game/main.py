import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Naming Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answers = []

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list

while len(correct_answers) < 51:
    answer_state = screen.textinput("Guess the State", "What's another state's name?")
    answer_state.title()
    if answer_state in state_list():
        correct_answers.append(answer_state)
        print(correct_answers)

screen.exitonclick()
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Naming Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answers = []

df = pandas.read_csv("50_states.csv")
state_list = df.state.to_list


def write_the_state(answer, x, y):
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(x, y)
    label.write(f"{answer}")


while len(correct_answers) != 50:
    answer_state = screen.textinput(f"{len(correct_answers)}/50 Correct!", "What's another state's name?")
    titled_answer_state = answer_state.title()
    if titled_answer_state in state_list():
        correct_answers.append(titled_answer_state)
        state = df[df.state == titled_answer_state]
        write_the_state(titled_answer_state, int(state.x), int(state.y))

screen.exitonclick()
