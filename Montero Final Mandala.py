import turtle

window = turtle.Screen()
window.bgcolor('white')
turtle.title("Mandala Tattoo by Matthew Montero - BSCS 1A")


t = turtle.Turtle()
t.speed(0)
penSize = 10
t.pensize(penSize)
outrad = 300

t.up()
t.goto(0,-(outrad))
t.down()
t.circle(outrad)


t.up()
t.pensize(5)
t.goto(0,0)
t.down()
for j in range(20):
	t.begin_fill()  
	t.right(360/20)
	t.color('black')
	for i in range(4):
		t.forward(210)
		t.left(90)
	t.end_fill()


t.up()
t.goto(0,-220)
t.down()
t.color("black")
t.fillcolor("white")
t.begin_fill()
t.circle(220)
t.end_fill()

t.up()
t.pensize(5)
t.goto(0,-200)
t.down()
t.color("black")
t.fillcolor("white")
t.begin_fill()
t.circle(200)
t.end_fill()
t.color('black')

t.up()
t.goto(0,0)
t.down()
for j in range(10):
	t.begin_fill()  
	t.right(360/10)
	t.color('black')
	for i in range(8):
		t.forward(75)
		t.left(360/8)
	t.end_fill()

t.color('black')
t.fillcolor('white')
t.up()
t.goto(0,-150)
t.down()
t.begin_fill()
t.circle(150)
t.end_fill()

t.up()
t.goto(-70, -34)
t.down()
t.pensize(3)
for times in range(36):
    t.forward(200)
    t.left(120)
    t.forward(100)
    t.right(120)
    t.left(170)
    t.left(20)
    t.forward(15)

t.color('black')
t.fillcolor('black')
t.up()
t.goto(1,-18)
t.down()
t.begin_fill()
t.circle(20)
t.end_fill()


t.hideturtle()
turtle.exitonclick()