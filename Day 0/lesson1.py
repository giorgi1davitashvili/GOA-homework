from turtle import *

speed(3)

width(4)
color("purple")
#square
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#door
begin_fill()
forward(80)
color("yellow")
left(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill()

penup() 
goto(200, 200)
pendown()
color("red")

begin_fill()
right(150)
forward(200)  #roof
left(120)
forward(200)
end_fill()

penup()
goto(170, 180)
pendown()
color("green")

begin_fill()
right(60)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(70, 180)
pendown()

begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


exitonclick()