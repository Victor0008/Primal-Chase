import pgzrun
import pygame
import random

TITLE = "Primal Chase"
WIDTH = 400
HEIGHT = 300

snake = Actor('snake')
snake.x = 420
snake.y = 250

mlk = Actor('principal')
mlk.x = 100
mlk.y = 220

bg = Actor('background')

#while game_has_not_ended():
 #   snake.draw()

def update():
    if keyboard.left:
        mlk.x -= 5
    if keyboard.right:
        mlk.x += 5

def update():
    snake.left += -1
    if snake.left > WIDTH:
        snake.right = 0

def draw():
    bg.draw()
    snake.draw()
    mlk.draw()

    pgzrun.go
