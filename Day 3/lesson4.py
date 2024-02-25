from turtle import *
import turtle 

speed(60)

width(4)
color("grey")
penup()
goto(-400,0)
pendown()         #square
forward(200)
begin_fill()
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()




left(90)
forward(80)      
color("brown")
begin_fill()
left(90)
forward(60)       #door
right(90)
forward(40)
right(90)
forward(60)
end_fill()

left(90)
color("grey")
forward(80)
left(90)
forward(200)
color("orange")     #roof
begin_fill()
left(45)
forward(140)
left(90)
forward(140)
end_fill()

penup()
goto(-330,175)
pendown()

color("cyan")
right(45)
begin_fill()
forward(40)    #window 1 (1)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(-270, 175)
pendown()

right(90)
begin_fill()
forward(40)
right(90)           #window 2 (1)
forward(40)
right(90)
forward(40)
right(90)
forward(40)                 #house 1--------------------------
end_fill()


penup()
goto(-100,0)
pendown()
width(30)
color("brown")
forward(80)                   #tree 1---------
width(10)
color("green")
begin_fill()
penup()
goto(-62,120)
pendown()
circle(40)
end_fill()


penup()
goto(0,0)
pendown()
width(5)

color("orange")
begin_fill()
forward(200)
right(90)               #square 2
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

right(180)
forward(80)
left(90)
color("brown")
begin_fill()
forward(60)           #door 2
right(90)
forward(40)
right(90)
forward(60)
end_fill()

left(90)
color("orange")
forward(80)            #roof 2
left(90)
forward(200)
color("blue")
begin_fill()
left(45)
forward(140)
left(90)
forward(140)
end_fill()

penup()
goto(70,170)
pendown()

color("cyan")
begin_fill()
right(45)
forward(40)
left(90)               
forward(40)             #window 1 (2)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(130,170)
pendown()

begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)                #window 2 (2)
forward(40)
right(90)
forward(40)                       #house 2----------------------
end_fill()



penup()
goto(270,0)
pendown()
width(30)
color("brown")
forward(80)                   #tree 2---------
width(10)
color("green")
begin_fill()
penup()
goto(310,120)
pendown()
circle(40)
end_fill()

penup()
goto(-100,-350)
pendown()

width(5)

color("red")
begin_fill()
forward(200)
right(90)               #square 3
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

right(180)
forward(80)
left(90)
color("brown")
begin_fill()
forward(60)           #door 3
right(90)
forward(40)
right(90)
forward(60)
end_fill()

left(90)
color("red")
forward(80)            #roof 3
left(90)
forward(200)
color("green")
begin_fill()
left(45)
forward(140)
left(90)
forward(140)
end_fill()

penup()
goto(-30,-170)
pendown()

color("cyan")
begin_fill()
right(45)
forward(40)
left(90)               
forward(40)             #window 1 (3)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(30,-170)
pendown()

begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)                #window 2 (3)
forward(40)
right(90)
forward(40)                       #house 3----------------------
end_fill()




penup()
goto(240,-340)
pendown()
width(30)
color("brown")
forward(80)                   #tree 3---------
width(10)
color("green")
begin_fill()
penup()
goto(280,-220)
pendown()
circle(40)
end_fill()





penup()
goto(-240,-340)
pendown()
width(30)
color("brown")
forward(80)                   #tree 3---------
width(10)
color("green")
begin_fill()
penup()
goto(-200,-220)
pendown()
circle(40)
end_fill()






exitonclick()