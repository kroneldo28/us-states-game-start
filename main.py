import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()

correct_guesses = []
# We loop until we have all the states found
while len(correct_guesses) < 50:
    user_answer = screen.textinput(prompt="Guess a State", title=f"{len(correct_guesses)}/50 correct guesses").title()
    if user_answer == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_dataframe = pandas.DataFrame(missing_states)
        new_dataframe.to_csv("missing_states.csv")
        break
    if user_answer in states:
        print(user_answer)
        turtle.penup()
        state_dataframe = states_data[states_data.state == user_answer]
        x_cor = float(state_dataframe.x)
        y_cor = float(state_dataframe.y)
        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.goto(x_cor, y_cor)
        state_text.write(f"{user_answer}")
        correct_guesses.append(user_answer)

# MY SOLUTION
# # Let's save the missing states to a csv
# list_of_states = states_data.state.to_list()
# for state in correct_guesses:
#     if state in list_of_states:
#         list_of_states.remove(state)
#
# missing_states = pandas.Series(data=list_of_states)
# print(missing_states)
#
# missing_states.to_csv("missing_states.csv")


