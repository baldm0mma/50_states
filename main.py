import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image_path = "./blank_states_img.gif"
screen.addshape(image_path)

turtle.shape(image_path)

current_guess = turtle.textinput(
    title="Guess the State", prompt="Guess another State's name:"
).lower()

screen.mainloop()
