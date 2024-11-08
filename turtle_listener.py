from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)
def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.title("press 'w' to make turtle forward")
screen.title("press 's' to make turtle backward")
screen.title("press 'd' to make turtle clockwise")
screen.title("press 'a' to make turtle counter clockwise")
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=screen_clear)
screen.exitonclick()