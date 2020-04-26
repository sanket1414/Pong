#pong game for beginners
import turtle
import time

wn=turtle.Screen()
wn.title("Pong by Sanket")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a=turtle.Turtle() #turtle=module name, Turtle=class name
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b=turtle.Turtle() #turtle=module name, Turtle=class name
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball=turtle.Turtle() #turtle=module name, Turtle=class name
ball.speed(0.5)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))
#Functions
def paddle_a_up():
	if paddle_a.ycor() < 230:
		y = paddle_a.ycor() # ycor is from turtle module it returns the y co-ordinates and we r assigning that value to tthe variable b
		y += 20
		paddle_a.sety(y)


def paddle_a_down():
	if paddle_a.ycor() > -230:
		y = paddle_a.ycor() # ycor is from turtle module it returns the y co-ordinates and we r assigning that value to tthe variable b
		y -= 20
		paddle_a.sety(y)


def paddle_b_up():
	if paddle_b.ycor() < 230:
		y = paddle_b.ycor() # ycor is from turtle module it returns the y co-ordinates and we r assigning that value to tthe variable b
		y += 20
		paddle_b.sety(y)


def paddle_b_down():
	if paddle_b.ycor() > -230:
		y = paddle_b.ycor() # ycor is from turtle module it returns the y co-ordinates and we r assigning that value to tthe variable b
		y -= 20
		paddle_b.sety(y)

#Keyboard binding

wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # when user press w call the func paddle_a_up
wn.onkeypress(paddle_a_down, "s") # when user press s call the func paddle_a_down
wn.onkeypress(paddle_b_up, "Up") # when user press up arrow call the func paddle_b_up
wn.onkeypress(paddle_b_down, "Down") # when user press down arrow call the func paddle_b_down



#Main game loop
while True:
	time.sleep(1 / 60)
	wn.update() 

	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1	
		score_a += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1	
		score_b += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

		

	#paddle nd ball collision
	if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.setx(320)
		ball.dx *= -1

	if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.setx(-320)
		ball.dx *= -1	