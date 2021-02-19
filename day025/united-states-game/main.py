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
