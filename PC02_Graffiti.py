#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Sophia Huseby
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

turtle.speed(0)

#this section of code contains the fill and shape for the black top hat
turtle.up()
turtle.left(90)
turtle.forward(175)
turtle.down()
turtle.begin_fill()
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

#this section of code contains the yellow ribbon on the hat
turtle.up()
turtle.color(218, 173, 41)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.down()
turtle.begin_fill()
turtle.forward(42)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(123)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(80)
turtle.end_fill()


#this section of code contains the pig nose
turtle.pencolor(180, 56, 108)
turtle.fillcolor(235, 121, 169)
turtle.pensize(3)
turtle.up()
turtle.goto(17, 64)
turtle.down()
turtle.begin_fill()
turtle.circle(19)
turtle.end_fill()


#this section of code contains the pig nostrils
turtle.up()
turtle.color(180, 56, 108)
turtle.pensize(7)
turtle.goto(24, 86)
turtle.down()
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.up()
turtle.forward(14)
turtle.down()
turtle.right(90)
turtle.forward(5)
turtle.hideturtle()


#this section of code contains the pig tail
turtle.up()
turtle.pensize(5)
turtle.goto(-215, -210)
turtle.down()
turtle.left(45)
turtle.forward(50)
turtle.up()
turtle.forward(13)
turtle.down()
turtle.circle(15)
turtle.forward(50)



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
