# This is a Quiz type Game in which you have eto guess the number of states, of the USA. If you Guessed a state
# score will be added to user score.

from turtle import Turtle, Screen
import pandas

# reading the data from CSV file using Pandas Library
read_state_name = pandas.read_csv("50_states.csv")

sc = Screen()
sc.title("US States Game")
image = "blank_states_img.gif"
sc.bgpic(image)

tim = Turtle()
tim.penup()
guessed_states = []
user_score = 0

while len(guessed_states) < 50:
    user_answer = sc.textinput(title=f"Guessed States--{user_score}/50", prompt="Guess the State of US").title()
    all_states = read_state_name.state.to_list()
    selected_state = read_state_name[read_state_name["state"] == user_answer]

    if user_answer in all_states:
        user_score += 1
        selected_state_x = int(selected_state["x"])
        selected_state_y = int(selected_state["y"])
        guessed_states.append(user_answer)
        tim.goto(selected_state_x, selected_state_y)
        tim.color("red")
        tim.write(user_answer, align="center", font=("Arial", 12, "normal"))
    # to close the program before guessing all the state I have used the below condition.
    if user_answer == None:
        break

sc.mainloop()

# I hope this project will help to a lot of beginners to get motivation and to work hard in their lives.
# Looking forward to your Positive Comments, and Suggestions.