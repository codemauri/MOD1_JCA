import turtle


turtle.shape("turtle")
turtle.speed(2)
turtle.color("green")
turtle.goto(0,0)
turtle.pensize(5)

def square(color,length):
  turtle.color(color)
  for i in range(4):
    turtle.forward(length)
    turtle.left(90)
    
def rectangle(width,heigth):
  turtle.color("red")
  for i in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(heigth)
    turtle.left(90)
    
    
def triangle(len_side):
  turtle.color("green")
  for i in range(3):
    turtle.forward(len_side)
    turtle.left(120)    



def separate(len):
  #turtle.goto(0,0)
  turtle.penup()  
  turtle.backward(len)
  turtle.pendown()

def interesting1(times):
  for i in range(times):
    square("green",50)
    turtle.left(360/times)
    
def interesting2(times):
  for i in range(times):
    rectangle(50,25)
    turtle.left(360/times)   
    
def house(len):
  square("red",len)
  x = turtle.xcor()
  y = turtle.ycor()
  turtle.penup()
  turtle.goto(x,len)
  turtle.pendown()
  triangle(len)
  turtle.penup()
  #turtle.goto(x,y)
  
def octagon(len):
  turtle.color("purple")
  turn = 360/8
  for _ in range(8):
    turtle.forward(len)
    turtle.left(turn)  
    
def stop(len):
  octagon(len)
  x = turtle.xcor()
  y = turtle.ycor()
  turtle.forward((3*len)/8)
  turtle.right(90)
  rectangle(2*len,len/5)
  turtle.left(90)
  #turtle.forward(50)
  #turtle.goto(x,y)
  
  
  



# square("green",90)
# separate(100)
# square("blue",90)

# rectangle(100,50)
# interesting2(36)
# separate(120)
# interesting1(36)
# house(90)
# turtle.goto(0.0)
# separate(100)
# house(45)
# separate(50)
# house(25)
# turtle.ycor
# square("red",90)
# print(type(turtle.ycor()))
# octagon(50)
stop(50)
separate(120)
stop(25)
separate(60)
stop(15)
# stop(30)
# separate(100)
# stop(40)
turtle.Screen().exitonclick()
