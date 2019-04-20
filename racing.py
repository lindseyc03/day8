from random import *
from turtle import *
speed(5)
'''
write(0)
forward(100)
write(5)
'''
penup()
goto(-140,140)
for step in range(15):
    write(step, align = "center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    
bob = Turtle()
bob.color('pink')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 100)
bob.pendown()


sally = Turtle()
sally.color('yellow')
sally.shape('turtle')

sally.penup()
sally.goto(-160, 70)
sally.pendown()

mary = Turtle()
mary.color('deep pink')
mary.shape('turtle')

mary.penup()
mary.goto(-160, 40)
mary.pendown()

peter = Turtle()
peter.color('deep sky blue')
peter.shape('turtle')

peter.penup()
peter.goto(-160, 10)
peter.pendown()

turns = 0 
while turns < 100:
    bob.forward(randint(1,5))
    sally.forward(randint(1,5))
    mary.forward(randint(1,5))
    peter.forward(randint(1,5))
    turns += 1
    
for twirl in range(10):
    bob.left(36)
    sally.left(36)
    mary.right(36)
    peter.right(36)
