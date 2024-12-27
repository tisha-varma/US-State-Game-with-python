import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Quiz")

# ADD IMAGE TO THE SCREEN
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# TODO : Refer this while making india quiz
# IF YOU WANT TO FIND COORDINATES WHEREVER THE MOUSE CLICKS/ COORDINATES OFF STATE
# def get_mouse_on_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_on_click_coor)
# turtle.mainloop()   # => it helps not to exit on click !

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)

score = 0
correct_guess = []

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Correct", prompt="What's another state name").title()

    # if answer_state == 'Exit':
    #     remaining_state = []
    #     for state in all_states:
    #         if state not in correct_guess:
    #             remaining_state.append(state)
    #
    #     remaining_state_dict = {
    #         'States Left': remaining_state
    #     }
    #     new_data = pandas.DataFrame(remaining_state_dict)
    #     new_data.to_csv("states_to_learn.csv")
    #     break
    #

    if answer_state == "Exit":

        remaining_states = [state for state in all_states if state not in correct_guess]
        # for state in all_states:
        #     if state not in correct_guess:
        #         remaining_states.append(state)
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state not in correct_guess:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            row = data[data.state == answer_state]
            row_x = float(row.x)
            row_y = float(row.y)
            t.goto(row_x, row_y)
            t.write(answer_state)
            # or t.write(row.state.item())
            score += 1
            correct_guess.append(answer_state)


screen.exitonclick()

