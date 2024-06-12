import pgzrun
import sys

TITLE = "Primal Chase"
WIDTH = 400
HEIGHT = 300

# Variáveis para o texto e o botão
texto = "Clique em 'START' para iniciar"
botao_jogar = Actor("start", center=(WIDTH/2, HEIGHT/2 + 50))
creditos = "creditos"

def draw():
    screen.clear()
    screen.draw.text(texto, center=(WIDTH/2, HEIGHT/3), color="white")
    botao_jogar.draw()
    screen.draw.text(creditos, center=(WIDTH/2, HEIGHT/1.1), color="white")

def on_mouse_down(pos):
    # Verifique se o clique do mouse está dentro dos limites do botão
    if botao_jogar.collidepoint(pos):
        iniciar_jogo()

def iniciar_jogo():
    print("O jogo está começando!")


pgzrun.go()
