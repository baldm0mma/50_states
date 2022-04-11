import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image_path = "./blank_states_img.gif"
screen.addshape(image_path)

turtle.shape(image_path)

data_path = "./50_states.csv"
state_data = pd.read_csv(data_path)
state_list = list(map(lambda state: state.lower(), state_data["state"].to_list()))
print(state_list)

correctly_guessed_state_count = 0

current_guess = turtle.textinput(
    title=f"{correctly_guessed_state_count}/50 states guessed correctly", prompt="Guess another State's name:"
)

screen.mainloop()
