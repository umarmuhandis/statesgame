import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

guessed_states = []


def get_state_coordinates(state_name):
    state_info = data[data.state == state_name]
    return int(state_info.x), int(state_info.y)


while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in data.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        x, y = get_state_coordinates(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x, y)
        state_turtle.write(answer_state,
                           align="center",
                           font=("Arial", 8, "normal"))

states_to_learn = [
    state for state in data.state if state not in guessed_states
]

learn_df = pd.DataFrame(states_to_learn, columns=["state"])
learn_df.to_csv("states_to_learn.csv", index=False)

turtle.mainloop()
