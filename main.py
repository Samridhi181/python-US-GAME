import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States Games")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
guessed_states = []

while len(guessed_states)<50:
    answer_state= screen.textinput(f"{len(guessed_states)}/50 States Correct","What's another state's name?").title()
#to check if answer is in the stae list

    if answer_state == "Exit":
        missing_states=[state for state in all_states if state not in guessed_states]

        new_data= pandas.DataFrame(missing_states)
        new_data.to_csv("learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)












































