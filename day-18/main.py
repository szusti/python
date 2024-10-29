from turtle import Turtle, Screen

timm = Turtle()



timm.shape("turtle")



screen = Screen()
for i in range (4):
    timm.forward(100)
    timm.left(90)


screen.exitonclick()