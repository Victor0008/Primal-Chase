import pgzrun

TITLE = "Primal Chase creditos"
WIDTH = 400
HEIGHT = 300

def draw():
    # Limpa a tela
    screen.clear()

    # Obtém as dimensões da tela
    largura = screen.width
    altura = screen.height


    texto_creditos = "Creditos"
    texto_equipe = "2M2 Larissa, Gustavo, Juan, Victor"
    cor_texto = "white"
    tamanho_texto = 20


    largura_texto_creditos = len(texto_creditos) * tamanho_texto * 0.1
    largura_texto_equipe = len(texto_equipe) * tamanho_texto * 0.3
    altura_texto = tamanho_texto

    # Calcula as coordenadas x e y para posicionar o texto no meio da tela
    x_creditos = (largura - largura_texto_creditos) / 2
    y_creditos = altura * 0.3

    x_equipe = (largura - largura_texto_equipe) / 1
    y_equipe = altura * 0.7

    # Desenha o texto no centro da tela
    screen.draw.text(texto_creditos, midtop=(x_creditos, y_creditos), fontsize=tamanho_texto, color=cor_texto)
    screen.draw.text(texto_equipe, midtop=(x_equipe, y_equipe), fontsize=tamanho_texto, color=cor_texto)

pgzrun.go()
