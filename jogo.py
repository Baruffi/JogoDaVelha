# imports

import pygame

# inicio da engine

pygame.init()

# recursos

tela = pygame.display.set_mode((600, 600))
relogio = pygame.time.Clock()

xises = 0
bolinhas = 0

#configuracoes

pygame.display.set_caption('Jogo da Velha')

# desenhaveis

velha = pygame.image.load("velha.png").convert_alpha()
xis = pygame.image.load("xis.png").convert_alpha()
bolinha = pygame.image.load("bolinha.png").convert_alpha()

# funcoes

def tique():
    relogio.tick(60)

def atualiza():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def desenha():
    tela.fill((0,0,0))
    tela.blit(velha, (0, 0))

    for i in range(0, bolinhas):
        tela.blit(bolinha, (0, 0))

    for i in range(0, xises):
        tela.blit(xis, (0, 0))

def exibe():
    pygame.display.update()

# loop do jogo

while True:
    tique()
    atualiza()
    desenha()
    exibe()