import pygame
from pygame.locals import *
from sys import exit
from random import randint #Sorteia valores dentro de um determinado intervalo

pygame.init() #incializar todas as funcoes de pygame

#1. Definição da largura e altura da nossa tela
largura = 640
altura = 480
x = largura / 2 
y = altura / 2 

# Variável para retângulo blue
x_blue = randint(30,500)
y_blue = randint(40,360)

# Fonte da mensagem que aparecerá na tela
fonte = pygame.font.SysFont('Times New Roman', 40, True, True)

# Variável Pontos
pontos = 0

# Tela
tela = pygame.display.set_mode((largura,altura)) #objeto tela, set mode vai recebe uma tupla

# Nome
pygame.display.set_caption('lab-pygame')

# Controlando taxa de frames
relogio = pygame.time.Clock()

#2. Criação do loop principal do jogo
# a cada seg, o jogo vai ter que estar se atualizando
while True:
    relogio.tick(40)#quantos frames por segundo o nosso jogo terá
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))

    for event in pygame.event.get(): #a cada interação do loop principal,checar se algum evento ocorreu
        if event.type == QUIT:
            pygame.quit()
            exit()

        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''
                
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    
    # 3. Desenhando o nosso retângulo
    retangulo_green = pygame.draw.rect(tela,(0,255,0), (x, y,40,50)) #x,y,largura(px), altura
    retangulo_blue = pygame.draw.rect(tela, (0,0,255), (x_blue,y_blue,40,50))
    
    #4. Colisão de objetos
    if retangulo_green.colliderect(retangulo_blue):
        pontos += 1
        x_blue = randint(30,500)
        y_blue = randint(40,360)

    #Se mova sozinho
    # if y >= altura:
    #    y = 0
    #y = y + 5

    #pygame.draw.circle(tela,(255,0,0),(300,260), 40)
    #pygame.draw.line(tela, (120,50,50), (380,0), (380,600), 5)

    tela.blit(texto_formatado, (450,40)) # aparecer na tela
    pygame.display.update() #atualiza a tela do jogo