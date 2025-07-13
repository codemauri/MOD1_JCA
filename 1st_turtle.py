import turtle
import random
import tur
def triangle(size):
  turtle.color("green")
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
    
    
def square(size):
  turtle.color("red")
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)
    
def polygon(sides, len):
  if ( sides < 3):
    print("ERROR: sides mus be > 3")
    return
  colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink", "cyan"]
  # random_color = random.choice(colors)
  # turtle.color(random_color)
  turtle.color("purple")
  turn = 360/sides
  # turtle.forward(100)
  for _ in range(sides):
    turtle.forward(len)
    turtle.left(turn)
    
def spiral(lenlongest, angle):
  for i in range(5, lenlongest, 5):
    # i *= 0.9 + 5
    turtle.forward(i)  # linearly increasing side
    turtle.left(angle)
    
def move(len):
  back(-1*len)
    
    
    
    
    
def draw_circle_of_polygons(num_polygons, sides, length):
    angle_between = 360 / num_polygons
    for _ in range(num_polygons):
        polygon(sides, length)
        turtle.left(angle_between)
        # sides -= 1
        
        
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
  
def down(len):
  turtle.penup()
  # Move down by 20 units (you can adjust this)
  turtle.right(90)
  turtle.forward(len)
  turtle.left(90)
  turtle.pendown()

  
def forward(len):
  turtle.penup()
  turtle.forward(len)
  turtle.pendown()
  
  

# triangle(100) 
# back(75)
# triangle(50)
# back(50)
# triangle(25)

# down(150)

# forward(125)

# square(100)
# back(75)
# square(50)
# back(50)
# square(25)

# for i in range(3): 
  # # down(150)
  # back(45)
  # polygon(6, 20)

  
# Setup
# turtle.speed("fastest")  # Speed up drawing
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Draw a circle of polygons
# draw_circle_of_polygons(num_polygons=36, sides=6, length=50)  # 36 hexagons


# turtle.penup()
# turtle.goto(0, -200)
# turtle.pendown()

# for n in range(3, 10):
  # move(50)
  # polygon(n, 100/n)
  # back(50)
  # turtle.right(360/7)

# spiral(75, 45)
# move(150)
# spiral(100,90)

# turtle.done()
