import turtle
import random

screen=turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("white")
screen.screensize(500,500)
screen.register_shape("turtle.gif")


turtle_instance=turtle.Turtle()
turtle_instance.shape("turtle.gif")
turtle_instance.speed(0)

#Scoreboard
score=0
pen=turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0,250)
######

#Time
game_time=20
time=turtle.Turtle()
time.penup()
time.color("black")
time.hideturtle()
time.goto(-280,250)
time.write(f"Time: {game_time}",align="center",font=("Courier New",32,"normal"))

pen.write(f"Score: {score}",align="center",font=("Courier New",32,"normal"))


def remaining_time():
    global game_time
    game_time -=1
    time.clear()
    time.write(f"Time: {game_time}",align="center",font=("Courier New",32,"normal"))
    if game_time>=0:
        screen.ontimer(remaining_time, 1000)
    else:
        game_over()

def clicked(x,y):
    global score
    score +=1
    pen.clear()
    pen.write(f"Score: {score}",align="center",font=("Courier New",32,"normal"))
    turtle_instance.hideturtle()
    screen.ontimer(reappear_turtle, 500)

remaining_time()
turtle_instance.onclick(clicked)

#random move turtle
def move_turtle():
   turtle_instance.penup()
   r = random.randint(-300, 300)
   turtle_instance.goto(r, r)
   screen.ontimer(move_turtle, 400)

move_turtle()

def reappear_turtle():
    turtle_instance.showturtle()

def game_over():
    pen.clear()
    pen.goto(0,0)
    pen.write(f"Game Over! Your Score: {score}", align="center", font=("Courier New", 32, "normal"))
    turtle_instance.hideturtle()

screen.mainloop()