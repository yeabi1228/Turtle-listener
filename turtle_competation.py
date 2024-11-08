from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)
user_guess = screen.textinput(title="THE TURTLE RACE",prompt="which turtle do you think win?enter the color")
colors = ["red","orange","yellow","blue","green","purple"]

is_race_on1 = True
num1 = 0
all_turtle = []
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(230, 100 - num1)
    num1+= 50
    all_turtle.append(tim)
while is_race_on1:
    for turtle in all_turtle:
        if turtle.xcor() <-233:
            is_race_on1 = False
            if user_guess == turtle.pencolor():

                print(f"you win, and the {turtle.pencolor()} turtle is the winner")
            else:

                print(f"you loses ,and the {turtle.pencolor()} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.backward(random_distance)




screen.exitonclick()
