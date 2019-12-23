# Import our functions
from turtle import *
#from shapes import *

# Name our turtle and make it fast
t= Turtle()
t.speed(50)

# Make our waves
def w():
  t.color("dark blue")
  t.begin_fill()
  t.pendown()
  t.left(70)
  t.forward(90)
  t.right(60)
  t.forward(35)
  t.right(60)
  t.forward(30)
  t.right(60)
  t.forward(30)
  t.right(60)
  t.forward(20)
  t.right(60)
  t.forward(15)
  t.right(190)
  t.forward(32)
  t.left(20)
  t.forward(30)
  t.left(39.7)
  t.end_fill()  

t.penup()
t.goto(-200,-200)
w()
w()
w()
w()
w()
t.penup()

# Make large bubbles
def lb():
  t.pendown()
  t.circle(20)
  t.penup()
  t.left(56)
  t.forward(15)
  t.pendown()
  t.circle(14,90)
  t.right(144.6)
  t.penup()

# Move up to higher bubble
def up():
  t.forward(50)

# Move down to lower bubble
def down():
  t.forward(50)
  t.right(90)
  t.forward(70)
  t.left(90)
  
# Draw lower row of dark bubbles
t.goto(-150,-80)
lb()
up()
lb()
down()
lb()
up()
lb()
down()
lb()
up()
lb()
down()
lb()

# Move to start middle row of bubbles
t.goto(-150,10)

# Draw middle row of blue mid-size bubbles
def mb():
  t.color("blue")
  t.pendown()
  t.circle(16)
  t.penup()
  t.left(56)
  t.forward(15)
  t.pendown()
  t.circle(8,90)
  t.right(144.6)
  t.penup()

mb()
up()
mb()
down()
mb()
up()
mb()
down()
mb()
up()
mb()
down()
mb()

# Move to start top row of turquoise bubbles
t.goto(-150,100)


# Draw top row of light blue tiny bubbles
def sb(x,y):
  t.color("turquoise")
  t.goto(x,y)
  t.pendown()
  t.circle(10)
  t.penup()
  t.left(56)
  t.forward(15)
  t.goto(x+1,y+10)
  t.pendown()
  t.circle(5,90)
  t.right(144.6)
  t.penup()
  return
x=-150
y=100
for i in range (1,9):
  sb(x,y)
  x = x+50
  if(y == 100):
    y = 130
  else:
    y = 100
    
t.goto(-200,-200)
