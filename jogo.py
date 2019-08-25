import pygame
from pygame.locals import *

pygame.init()

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da Velha')

velha=[
{'pos': (0, 200), 'surface': pygame.Surface((600, 10))},
{'pos': (0, 400), 'surface': pygame.Surface((600, 10))},
{'pos': (200, 0), 'surface': pygame.Surface((10, 600))},
{'pos': (400, 0), 'surface': pygame.Surface((10, 600))},
]

xis = []
bolinha = []

def update():

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

def draw():

    tela.fill((0,0,0))

    for linha in velha:
        linha.get('surface').fill((255,255,255))
        tela.blit(linha.get('surface'), linha.get('pos'))

while True:

    update()
    draw()

    pygame.display.update()