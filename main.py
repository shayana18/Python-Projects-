from turtle import Screen
from Snake import Snake
from Foodd import Food
import time
from Scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Shykizzy No Kizzy Snake Game")
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

scoreboard.score()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    #collision with food
    if snake.head.distance(food) < 15:
        scoreboard.points += 1
        food.refresh()
        snake.extend()
        scoreboard.score()

    #Detect collision with wall

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()


    #detect collision with tail

    for segment in snake.seg_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()





screen.exitonclick()
