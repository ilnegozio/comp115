import turtle

def draw_sunbeams(t, num_beams):
    angle = 360 / num_beams
    for _ in range(num_beams):
        pen.penup()
        pen.forward(125)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.backward(145)
        pen.right(angle)
        pen.pendown()

window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)

radius = 100

# Draw a sun
pen.up()
pen.goto(0, -radius)
pen.down()
pen.circle(radius)
pen.up()
pen.goto(0, 0)

# Draw sun beams
draw_sunbeams(pen, 16)

pen.shape('blank')

window.exitonclick()


