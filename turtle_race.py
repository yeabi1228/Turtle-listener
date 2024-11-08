from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
user_guess=screen.textinput(title="this the TURTLE race",prompt="which turtle is gonna win? enter the color")
colors =["red","orange","yellow","green","blue","purple"]
is_race_on = True
all_turtles = []
num=0
for i in range(6):

    timi = Turtle(shape = "turtle")
    if colors[i]==user_guess:
        timi.color(colors[i])
        timi.penup()
        timi.goto(-230, -130 )
    else:
        timi.color(colors[i])
        timi.penup()
        timi.goto(-230,-100+num)
        num+=30
    all_turtles.append(timi)
while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 233:
            is_race_on = False
            if user_guess == turtles.pencolor():
                print(f"you won , the {turtles.pencolor()} turtle is the winner")
            else:
                print(f"you loses,the {turtles.pencolor()} turtle is the winner")
        random_distance = random.randint(0,10)
        turtles.forward(random_distance)

screen.exitonclick()
