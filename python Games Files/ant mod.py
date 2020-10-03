'''Modifications are :
    1. ant does not go across the borders of the screen
    2. ant color is changed
    3. ant leaves trail on the way by going through
'''
from random import *
from turtle import *
from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)


def wrap(value):
    "Wrap value around -200 and 200."
    if value > -200 and value < 200:
        return value 

def draw():
    "Move ant and draw screen."
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)
    
    #clear()
    goto(ant.x, ant.y)
    dot(4, 'red')

    if running:
        ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()
