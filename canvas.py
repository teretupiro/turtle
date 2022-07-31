import turtle
polygon=turtle.Turtle()
polygon.shape('turtle')
polygon.penup()
polygon.goto(-100,100)
polygon.pendown()
polygon.pencolor(0.2,0.5,0.8)
polygon.speed(10)
while True:


  pen_size=10
  blue_color=0.8
  polygon_size=200

  def create_polygon(angles):

     for i in range(angles):
        polygon.forward(200)
        polygon.left(-(360/angles))
        #b = polygon.pencolor()[2] - 0.11
        #polygon.pencolor((0.2, 0.5, b))


  for i in range(2):
   create_polygon(3)
   pen_size=+2
   polygon.penup()
   polygon.goto(polygon.xcor()+5,polygon.ycor()+10)
   polygon.pendown()
