# imports

import pygame
from pygame.locals import *

# inicio da engine

pygame.init()

# recursos

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da Velha')

relogio = pygame.time.Clock()

# desenhaveis

velha=[
{'posicao': (0, 200), 'superficie': pygame.Surface((600, 10))},
{'posicao': (0, 400), 'superficie': pygame.Surface((600, 10))},
{'posicao': (200, 0), 'superficie': pygame.Surface((10, 600))},
{'posicao': (400, 0), 'superficie': pygame.Surface((10, 600))},
]

xis = []
bolinha = []

# funcoes

def tique():
    relogio.tick(60)

def atualiza():

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

def desenha():

    tela.fill((0,0,0))

    for linha in velha:
        linha.get('superficie').fill((255,255,255))
        tela.blit(linha.get('superficie'), linha.get('posicao'))

def exibe():
    pygame.display.update()

# loop do jogo

while True:

    tique()
    atualiza()
    desenha()
    exibe()