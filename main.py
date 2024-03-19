from turtle import Screen
from turtle import Turtle
import pandas

screen = Screen()
text = Turtle()

screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
text.hideturtle()
text.penup()

correct_states = 0
game_is_on = True

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


while game_is_on:
    user_input = screen.textinput(f"{correct_states}/50 States Correct", "What's another state name.")
    if user_input in states_list:
        x = int(data[data.state == user_input].x)
        y = int(data[data.state == user_input].y)
        text.goto(x=x, y=y)
        text.write(user_input, True, font=('Arial', 8, 'normal'))
        correct_states += 1
        if correct_states == 50:
            screen.clearscreen()
            text = Turtle()
            text.hideturtle()
            text.penup()
            text.goto(0, 0)
            text.write("Congratulation you are a nerd.", True, font=('Arial', 8, 'normal'))
            game_is_on = False
    elif user_input == "exit" or user_input == "Exit":
        game_is_on = False

screen.exitonclick()
