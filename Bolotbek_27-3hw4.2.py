

from Bolotbek_27-3hw4.2 import *

person = Hero("Бетмен","стрельба")
dragon = Hero_super("Дракон","летать")
dragon.prints()

class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class Hero_super(Hero):
    def __init__(self, name, abyliti):
        Hero.__init__(self, name, abyliti)

    def __str__(self):
        return f'name is: {self.name}\n' \
               f'abyliti is: = {self.abyliti}'

    def prints(self):
        print(f'name is {self.name} it is super_hero')


# first = Hero_super("Супермен", "летать")
# first.prints()

import turtle

screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("blue")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while (True):
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()
turtle.done()