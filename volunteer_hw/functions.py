from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def draw_circle():
    turtle.circle(100)


def draw_rectangle():
    for _ in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

def draw_square():
   for _ in range(4):
        turtle.forward(200)
        turtle.left(90)


def rhombus():
   for i in range(2):
        turtle.forward(200)
        turtle.left(50)
        turtle.forward(200)
        turtle.left(130)

def hello():
    turtle.write("hello", font=("Arial", 24, "normal"))

def python():
    turtle.write("python", font=("Arial", 24, "normal"))


def eight_angle():
    for _ in range(8):
        turtle.forward(100)
        turtle.left(45)

def ten_angle():
    for _ in range(10):
        turtle.forward(100)
        turtle.left(36)
def tree():
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)

    for x in range(1,5):
        turtle.right(90)
        side = (100 - x * 20)
        turtle.forward(side)
        for _ in range(4):
            turtle.left(120)
            turtle.forward(2 * side)
        turtle.right(30)

def screen_off():
    screen.exitonclick()
