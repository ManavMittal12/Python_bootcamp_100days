from turtle import Turtle

import pandas
import turtle

from pandas.core.interchange.dataframe_protocol import DataFrame

screen = turtle.Screen()
screen.title("US States game")




# working with images in turtle
# we can set turtle shape to new shape
# we can load in an image as a new shape

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

us_states = pandas.read_csv("50_states.csv")
list_of_states = us_states.state.to_list()

is_game_on = True
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name ?").title()

    if answer_state.lower() == "exit":
        break
    if answer_state in list_of_states:
        writer = Turtle()
        writer.penup()
        writer.hideturtle()
        state_data = us_states[us_states.state == answer_state]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(state_data.state.item())
        guessed_states.append(answer_state)

      # we can use the break statement to break the flow of while loop


# states_to_learn.csv
missed_states = []
for miss in list_of_states:
    if miss not in guessed_states:
        missed_states.append(miss)



missed_states_df = pandas.DataFrame(missed_states)
missed_states_df.to_csv("states_to_learn.csv")
