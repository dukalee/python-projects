#!usr/bin/python3

# * head.direction이라는 attribute 사용보다는 안좋기는 하지만 아이들이 더 쉽게 이해하도록 global variable 사용.

import turtle
import time
import random

wn = turtle.Screen()
wn.title("SNAKE!")
wn.bgcolor("steel blue")
wn.setup(width = 600, height = 600)
wn.tracer(0) # 매뉴얼로 업데이트하도록 설정

# [2] Snake 객체
head = turtle.Turtle()
head.speed(0) # 속도를 가장 빠르게
head.shape("square")
head.color("limegreen")
head.up()
direction = "stop"

# [3] Snake의 움직임
def move():
    if direction == "up":
        y = head.ycor()   # 현재 snake의 y 좌표를 저장
        head.sety(y + 20) # 20 위로 움직임
    if direction == "down":
        y = head.ycor()   # 현재 snake의 y 좌표를 저장
        head.sety(y - 20) # 20 아래로 움직임
    if direction == "right":
        x = head.xcor()   # 현재 snake의 x 좌표를 저장
        head.setx(x + 20) # 20 위로 움직임
    if direction == "left":
        x = head.xcor()   # 현재 snake의 x 좌표를 저장
        head.setx(x - 20) # 20 위로 움직임

# [4] Snake의 방향 바꾸기
def up():
    global direction # 
    if direction != "down": 
        direction = "up"
def down():
    global direction
    if direction != "up":
        direction = "down"
def right():
    global direction
    if direction != "left":
        direction = "right"
def left():
    global direction
    if direction != "right":
        direction = "left"

wn.listen() # 컴퓨터 (turtle)이 keypress에 반응하도록 함.
wn.onkey(up, "Up")
wn.onkey(down, 'Down')
wn.onkey(left, "Left")
wn.onkey(right, 'Right')

# [5] food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('red')
food.up()
x = random.randint(-290, 290)
y = random.randint(-290, 290)
food.goto(x, y)

# [9] score
score = 0 
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.up()
pen.goto(0, 250)

# [6] 늘어나게 바꾸기
tails = [] 

# main loop 
while True:

    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        score += 10
    
    # [5] 늘어나게 바꾸기
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("white")
        new_tail.up()
        tails.append(new_tail)

    # [8] 몸통 충돌
    #for i in range(1, len(tails) - 1):
    for tail in tails:
        if tail.distance(head) < 15:
            time.sleep(1)
            head.goto(0, 0)
            direction = "stop"


    # 맨 뒤에서부터 loop, 끝에 있는 것들을 하나씩 앞으로 당겨와야 함. 
    if len(tails) > 0: 
        for index in range(len(tails) - 1, 0, -1): 
            x = tails[index-1].xcor()
            y = tails[index-1].ycor()
            tails[index].goto(x, y)
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)
        # 맨 처음꺼는 head의 자리로
    
    # [7] 벽 충돌
    if (head.xcor() > 290 or head.xcor() < -290 
    or head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        direction = "stop"
        
    if direction == "stop":
        score = 0 
        for tail in tails:
            tail.hideturtle()
        tails = []

    pen.clear()
    pen.write(f"Score: {score}", align = 'center', font = ("Courier", 20))

    move()
    wn.update()
    time.sleep(0.1) # 0.1초마다 업데이트 
