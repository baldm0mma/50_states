import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image_path = "./blank_states_img.gif"
screen.addshape(image_path)

turtle.shape(image_path)

data_path = "./50_states.csv"
state_data = pd.read_csv(data_path)
state_list = list(map(lambda state: state.title(), state_data["state"].to_list()))

correctly_guessed_state_count = 0

while len(state_list):
    current_guess = turtle.textinput(
        title=f"{correctly_guessed_state_count}/50 states guessed correctly",
        prompt="Guess another State's name:",
    ).title()

    if current_guess in state_list:
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        state = state_data[state_data["state"] == current_guess]
        label.goto(x=float(state["x"]), y=float(state["y"]))
        label.write(current_guess)
        # Remove correctly guessed state from list
        state_list.remove(current_guess)
        # Increment `correctly_guessed_state_count`
        correctly_guessed_state_count += 1

screen.exitonclick()
