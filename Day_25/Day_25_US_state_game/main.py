import turtle
import pandas

screen = turtle.Screen()
screen.title("u.s state game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
gussed_state = []

while len(gussed_state) < 50:
    user_state = screen.textinput(title=f"states", prompt="Enter state's name")
    if user_state in all_state:
        gussed_state.append(user_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()