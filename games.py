import turtle
import random
import time

game = turtle.Screen()
game.title("Highway Racer")
game.bgcolor("black")
game.setup(800, 650)
game.tracer(0)

points = 0

board = turtle.Turtle()
board.hideturtle()
board.penup()
board.color("white")
board.goto(-370, 280)

car = turtle.Turtle()
car.shape("square")
car.shapesize(stretch_wid=2, stretch_len=1)
car.color("deepskyblue")
car.penup()
car.goto(0, -270)

road = turtle.Turtle()
road.hideturtle()
road.color("white")
road.penup()

for mark in range(-320, 340, 50):
    road.goto(0, mark)
    road.write("||", align="center",
               font=("Arial", 16, "bold"))

traffic = []

lanes = [-240, -120, 0, 120, 240]
vehicle_colors = ["red", "orange", "yellow", "magenta", "lime"]

for i in range(6):
    vehicle = turtle.Turtle()
    vehicle.shape("square")
    vehicle.shapesize(2, 1)
    vehicle.penup()
    vehicle.color(random.choice(vehicle_colors))
    vehicle.goto(
        random.choice(lanes),
        random.randint(150, 800)
    )
    traffic.append(vehicle)

def go_left():
    if car.xcor() > -240:
        car.setx(car.xcor() - 120)

def go_right():
    if car.xcor() < 240:
        car.setx(car.xcor() + 120)

game.listen()
game.onkeypress(go_left, "Left")
game.onkeypress(go_right, "Right")

playing = True

while playing:

    game.update()

    board.clear()
    board.write(
        f"Points: {points}",
        font=("Verdana", 16, "bold")
    )

    for vehicle in traffic:

        vehicle.sety(vehicle.ycor() - 3)

        if vehicle.ycor() < -340:
            vehicle.goto(
                random.choice(lanes),
                random.randint(400, 800)
            )
            points += 1

        if car.distance(vehicle) < 40:
            playing = False

    time.sleep(0.02)

finish = turtle.Turtle()
finish.hideturtle()
finish.color("white")

finish.write(
    f"GAME OVER\nScore: {points}",
    align="center",
    font=("Arial", 24, "bold")
)

game.mainloop()