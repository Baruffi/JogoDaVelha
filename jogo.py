# imports

import pygame

# inicio da engine

pygame.init()

# listas

xises = []
bolinhas = []
turnos = []

linhas = [
    ((0, 0), (0, 200), (0, 400)),
    ((200, 0), (200, 200), (200, 400)),
    ((400, 0), (400, 200), (400, 400)),
    ((0, 0), (200, 0), (400, 0)),
    ((0, 200), (200, 200), (400, 200)),
    ((0, 400), (200, 400), (400, 400)),
    ((0, 0), (200, 200), (400, 400)),
    ((400, 0), (200, 200), (0, 400)),
]

#configuracoes

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da Velha')

# desenhaveis

velha = pygame.image.load("velha.png").convert_alpha()
xis = pygame.image.load("xis.png").convert_alpha()
bolinha = pygame.image.load("bolinha.png").convert_alpha()

xis_transparente = xis.copy()
xis_transparente.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)

bolinha_transparente = bolinha.copy()
bolinha_transparente.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)

# colidiveis

campo = pygame.Surface((200, 200))

campos = [
    (campo, (0, 0)),   (campo, (200, 0)),   (campo, (400, 0)),
    (campo, (0, 200)), (campo, (200, 200)), (campo, (400, 200)),
    (campo, (0, 400)), (campo, (200, 400)), (campo, (400, 400)),
]

# funcoes

def jogador_venceu():
    for linha in linhas:
        for celula in linha:
            value = True
            if not xises.__contains__(celula):
                value = False
                break
    return value

def computador_venceu():
    for linha in linhas:
        for celula in linha:
            value = True
            if not bolinhas.__contains__(celula):
                value = False
                break
    return value

def empatou():
    if turnos.__len__() == 9:
        return True

def reinicia():
    xises.clear()
    bolinhas.clear()
    turnos.clear()

def atualiza():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for campo in campos:
                if campo[0].get_rect(topleft=campo[1]).collidepoint(pygame.mouse.get_pos()):
                    if not xises.__contains__(campo[1]) and not bolinhas.__contains__(campo[1]):

                        if turnos.__len__() % 2 == 0:
                            xises.append(campo[1])
                        else:
                            bolinhas.append(campo[1])

                        turnos.append((xises, bolinhas))
    
    if jogador_venceu():
        print('Vitoria para o jogador!')
        reinicia()

    if computador_venceu():
        print('Vitoria para o computador!')
        reinicia()

    if empatou():
        print('Empate!')
        reinicia()

def desenha():
    tela.fill((0,0,0))

    tela.blit(velha, (0, 0))

    for campo in campos:
        if campo[0].get_rect(topleft=campo[1]).collidepoint(pygame.mouse.get_pos()):
            if turnos.__len__() % 2 == 0:
                tela.blit(xis_transparente, campo[1])
            else:
                tela.blit(bolinha_transparente, campo[1])

    for posicao in xises:
        tela.blit(xis, posicao)

    for posicao in bolinhas:
        tela.blit(bolinha, posicao)

def exibe():
    pygame.display.update()

# loop do jogo

while True:
    atualiza()
    desenha()
    exibe()