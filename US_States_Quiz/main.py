from turtle import Turtle, Screen
from score import Score
import pandas

screen = Screen()
score = Score()
states = pandas.read_csv("50_states.csv")
map_list = states.state.to_list()


def game():
    screen.title("US State Quiz Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle = Turtle()
    turtle.shape(image)

    guessed_list = []
    score.update(len(guessed_list))

    while len(guessed_list) < 50:
        answer = screen.textinput(title="Guess the state", prompt="What state of US can you guess?").title()

        if answer == "Exit":
            missing_list = [state for state in map_list if state not in guessed_list]
            missing_data = pandas.DataFrame(missing_list)
            missing_data.to_csv("missing_states.csv")
            break

        if answer in map_list:
            guessed_list.append(answer)
            data = states[states.state == answer]
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(data.x), int(data.y))
            t.write(data.state.item(), align="Center", font=("Arial", 8, "bold"))
            score.update(len(guessed_list))

        if len(guessed_list) == 50:
            score.win()
            game_choice = screen.textinput(title="US States Game", prompt="Play again or Exit").lower()
            if game_choice == "play again":
                screen.clear()
                game()


game()

# To find the coordinate of all the states on the map
# def get_mouse_click_coordinate(x,y):
#     print(x,y)
#
# screen.onscreenclick(fun = get_mouse_click_coordinate)
