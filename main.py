import turtle
import pandas
import time

# Screen settings
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_correct = 0

# 50_states.csv processing
data = pandas.read_csv("50_states.csv")
states = data["state"]
states = states.to_list()
x_values = data["x"].to_list()
y_values = data["y"].to_list()
coordinates = []
for i in range(len(x_values)):
    coordinates.append((x_values[i], y_values[i]))


# A function to write over the country that the user entered
def write_in_screen(state, position):
    new_write = turtle.Turtle()
    new_write.penup()
    new_write.hideturtle()
    new_write.setposition(position)
    new_write.write(arg=state, align="center")


# Start game
correct_answered = []
while states_correct < 50:
    user_answer = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?")
    user_answer = user_answer.title()
    if user_answer in states and user_answer not in correct_answered:
        states_correct += 1
        correct_answered.append(user_answer)
        index = states.index(user_answer)
        write_in_screen(states[index], coordinates[index])
        time.sleep(1)
    elif user_answer == "Exit":
        not_answered = [state for state in states if state not in correct_answered]
        data_report = {
            "Not answered": not_answered
        }
        data_report = pandas.DataFrame.from_dict(data_report)
        data_report.to_csv("user_report.csv")
        break
