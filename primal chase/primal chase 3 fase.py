# Escreva o seu código aqui :-)
import pgzrun
import pygame.mixer

pygame.mixer.init()

TITLE = "Primal Chase 3"
WIDTH = 400
HEIGHT = 300

music1 = pygame.mixer.Sound("finale.mp3")
music2 = pygame.mixer.Sound("andando.mp3")
music1.play(-1)  # -1 indica que a música vai tocar em loop
music2.play(-1)  # -1 indica que a música vai tocar em loop

crocodile = Actor("raptor", (400, 180))
crocodile_speed = 10
crocodile_spawn_time = 10
crocodile_timer = 0
crocodile_touch_edge = False

mlk_images = ["mlk1", "mlk2", "mlk3", "mlk4"]

mlk = Actor(mlk_images[0], (50, 170))

animation_time = 0.1
current_time = 0
current_frame = 0

background = Actor("background 3")
background_x = 0
background_speed = 3

def is_out_of_bounds(actor):
    return actor.left > WIDTH or actor.right < 100 or actor.top > HEIGHT or actor.bottom < 100

def draw():
    screen.clear()

    background.x = background_x
    background.y = HEIGHT / 2
    background.draw()

    background.x = background_x + background.width
    background.y = HEIGHT / 2
    background.draw()

    mlk.draw()

    crocodile.draw()

def update(dt):
    global current_time, current_frame, background_x, crocodile_timer, crocodile_touch_edge

    background_x -= background_speed
    if background_x <= -background.width:
        background_x = 0

    current_time += dt
    if current_time >= animation_time:
        current_time = 0
        current_frame = (current_frame + 1) % len(mlk_images)
        mlk.image = mlk_images[current_frame]

    move_crocodile()

    crocodile_timer += dt
    if crocodile_timer >= crocodile_spawn_time:
        spawn_crocodile()
        crocodile_timer = 0

    if is_out_of_bounds(crocodile) and not crocodile_touch_edge:
        crocodile_touch_edge = True
        pgzrun.quit()  # Encerre o jogo corretamente


def move_crocodile():
    global crocodile_touch_edge
    crocodile.x -= crocodile_speed

    if crocodile.right < 0 and not crocodile_touch_edge:
        crocodile_touch_edge = True

    if crocodile_touch_edge and crocodile.right < 0:
        crocodile.x = WIDTH + 50

def spawn_crocodile():
    crocodile.x = WIDTH + 50

def on_key_down(key):
    if key == keys.SPACE:
        crocodile.x = WIDTH + 60  # Defina a posição do crocodilo fora da tela


pgzrun.go()
