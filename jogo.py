# imports

import pygame

# inicio da engine

pygame.init()

# recursos

tela = pygame.display.set_mode((600, 600))
relogio = pygame.time.Clock()

xises = []
bolinhas = []
posicao_selecao = (0, 0)

#configuracoes

pygame.display.set_caption('Jogo da Velha')

# desenhaveis

velha = pygame.image.load("velha.png").convert_alpha()
xis = pygame.image.load("xis.png").convert_alpha()
bolinha = pygame.image.load("bolinha.png").convert_alpha()

# colidiveis

campo = pygame.Surface((200, 200))
campos = [
    (campo, (0, 0)),   (campo, (200, 0)),   (campo, (400, 0)),
    (campo, (0, 200)), (campo, (200, 200)), (campo, (400, 200)),
    (campo, (0, 400)), (campo, (200, 400)), (campo, (400, 400)),
]

# funcoes

def tique():
    relogio.tick(60)

def atualiza():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for campo in campos:
                if campo[0].get_rect(topleft=campo[1]).collidepoint(pygame.mouse.get_pos()):
                    if not bolinhas.__contains__(campo[1]):
                        if xises.__contains__(campo[1]):
                            xises.remove(campo[1])
                        bolinhas.append(campo[1])
                    else:
                        bolinhas.remove(campo[1])
                        xises.append(campo[1])

def desenha():
    tela.fill((0,0,0))
    tela.blit(velha, (0, 0))

    for posicao in bolinhas:
        tela.blit(bolinha, posicao)

    for posicao in xises:
        tela.blit(xis, posicao)

def exibe():
    pygame.display.update()

# loop do jogo

while True:
    tique()
    atualiza()
    desenha()
    exibe()