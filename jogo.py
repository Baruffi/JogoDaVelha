# imports

import pygame

# inicio da engine

pygame.init()

# configuracoes

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da Velha')

font = pygame.font.Font(None, 32)

# desenhaveis

velha = pygame.image.load('velha.png').convert_alpha()
xis = pygame.image.load('xis.png').convert_alpha()
bolinha = pygame.image.load('bolinha.png').convert_alpha()

xis_transparente = xis.copy()
xis_transparente.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)

bolinha_transparente = bolinha.copy()
bolinha_transparente.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)

jogador_venceu_text = font.render('Vitoria para o primeiro jogador!', False, (0, 255, 0))
computador_venceu_text = font.render('Vitoria para o segundo jogador!', False, (255, 0, 0))
empate_text = font.render('Empate!', False, (255, 255, 0))

jogador_venceu_text_rect = jogador_venceu_text.get_rect()
jogador_venceu_text_rect.center = (600 / 2, 600 / 2)

computador_venceu_text_rect = computador_venceu_text.get_rect()
computador_venceu_text_rect.center = (600 / 2, 600 / 2)

empate_text_rect = empate_text.get_rect()
empate_text_rect.center = (600 / 2, 600 / 2)

# colidiveis

campo = pygame.Surface((200, 200))

campos = [
    (campo, (0, 0)),   (campo, (200, 0)),   (campo, (400, 0)),
    (campo, (0, 200)), (campo, (200, 200)), (campo, (400, 200)),
    (campo, (0, 400)), (campo, (200, 400)), (campo, (400, 400)),
]

# listas dinâmicas

xises = []
bolinhas = []
turnos = []

# condicoes de vitoria

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

# funcoes

def jogador_venceu():
    for linha in linhas:
        if all(xises.__contains__(linha[i]) for i in range(3)):
            return True

def computador_venceu():
    for linha in linhas:
        if all(bolinhas.__contains__(linha[i]) for i in range(3)):
            return True

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
        print('Vitoria para o primeiro jogador!')
        reinicia()

    if computador_venceu():
        print('Vitoria para o segundo jogador!')
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