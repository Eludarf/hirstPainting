import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(140, 49, 106), (165, 169, 38), (245, 80, 57), (215, 229, 226), (228, 116, 164), (63, 199, 220),
              (230, 237, 240), (3, 140, 45), (242, 65, 139), (2, 143, 186), (18, 165, 127), (163, 56, 52),
              (254, 231, 0), (244, 222, 55), (161, 174, 167), (229, 168, 190), (31, 193, 215), (245, 168, 151),
              (143, 212, 224), (161, 209, 183), (104, 45, 97), (0, 127, 30)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
