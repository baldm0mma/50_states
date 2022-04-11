import turtle
import pandas as pd

# Build screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Add custom shape for background
image_path = "./blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

# Get state data
data_path = "./50_states.csv"
state_data = pd.read_csv(data_path)
# Build title-cased list of all states
state_list = list(map(lambda state: state.title(), state_data["state"].to_list()))

# Correctly-guessed state tally
correctly_guessed_state_count = 0

while len(state_list):
    # User's input
    current_guess = turtle.textinput(
        title=f"{correctly_guessed_state_count}/50 states guessed correctly",
        prompt="Guess another State's name:",
    ).title()

    # Add exit option that will build csv with all un-guessed states for later learning
    if current_guess == "Exit":
        # Generate csv with un-guessed states
        states_to_learn = pd.DataFrame({"state": state_list})
        states_to_learn.to_csv("./states_to_learn.csv")
        break

    # Add state label to screen
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
