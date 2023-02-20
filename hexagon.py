import turtle

colors = ["red", "orange", "yellow",
          "green", "blue", "purple"]
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
for i in range(360):
    t.pencolor(colors[i%6])
    t.width((i//100+1))
    t.forward(i)
    t.left(59)