# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:49:45 2021

@author: Arninho
"""

#https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

# 1 - Importando Modulos
import pygame
import math
import random

# 2 - Inicialização
pygame.init()
pygame.font.init()

width, height = 640, 480                            # tamanho da janela do jogo
screen=pygame.display.set_mode((width, height))     # incializa a janela
keys = [False, False, False, False]                 # botões pressionados
playerpos=[100,100]                                 # posição do jogador
healthvalue=194                                     # vida do jogador
acc=[0,0]                                           # contador de flechas (acertos e disparos)
arrows=[]                                           # lista de flechas

badtimer_itv=100                                    # temporizadores de geração de inimigos
badtimer_cnt=0         
badguys=[]                                          # lista de inimigos

# 3 - Carrega imagens
player = pygame.image.load("resources/images/dude.png")             # jogador
grass = pygame.image.load("resources/images/grass.png")             # grama
castle = pygame.image.load("resources/images/castle.png")           # castelo
arrow = pygame.image.load("resources/images/bullet.png")            # flecha
healthbar = pygame.image.load("resources/images/healthbar.png")     # barra de vida (vermelha)
health = pygame.image.load("resources/images/health.png")           # vida (verde)
badguyimg1 = pygame.image.load("resources/images/badguy.png")       # vilão
badguyimg=badguyimg1

# 4 - laço principal
go_on = True
while go_on:
    
    # 5 - Limpa a tela a cada iteração
    screen.fill(0)
    
    # 6 - Desenha elementos na tela
    # 6.1 - Desenha grama
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
            
    # 6.2 - Desenha castelos
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))    

    # 6.3 - Desenha Jogador (posição do mouse, angulo, converte para graus, rotaciona e desenha)
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    angle = 360-angle*180/math.pi                                
    playerrot = pygame.transform.rotate(player, angle)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width//2, playerpos[1]-playerrot.get_rect().height//2)
    screen.blit(playerrot, playerpos1) 

    # 6.4 - Desenha flechas: flecha = [angulo, pos_x, pos_y]
    for bullet in arrows:
        bullet[1]+= int(math.cos(bullet[0])*10)
        bullet[2]+= int(math.sin(bullet[0])*10)

    #remove flechas fora da janela, rotaciona e desenha
    arrows = [b for b in arrows if b[1]>-64 and b[1]<640 and b[2]>-64 and b[2]<480]
    for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*180/math.pi)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    
    # 6.5 - Desenha malvadões - cnt é o contador e itv o intervalo entre geração
    badtimer_cnt += 1
    if badtimer_cnt >= badtimer_itv:
        badguys.append([640, random.randint(50,430)])       # posição do x constante, y é randômica
        badtimer_cnt = 0
        badtimer_itv = max(30, badtimer_itv-5)              # diminui o intervalo até chegar no 30

    for badguy in badguys:
        screen.blit(badguyimg, badguy)


    # 7 Lógica do jogo
    # 7.1 Detecta se fomos atingidos e remove vilões que chegaram no castelo
    n_hit = len([b for b in badguys if b[0]<=64])
    healthvalue -= n_hit*random.randint(5, 20)
    badguys = [b for b in badguys if b[0]>64]
    
    #7.2 Move vilões e detecta colisões
    for badguy in badguys:

        # move (decrementa posição x) e cria retângulo para detectar colisões
        badguy[0]-= 2
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]

      #7.2.1 - detecta colisões com cada flecha
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguy[1] = -200        # move o vilão para fora da tela e ele será eliminado
                bullet[2] = -200

    # 7.3 Desenha precisão
    font = pygame.font.Font(None, 24)
    res = (acc[0], acc[1], 100*acc[0]/max(1,acc[1]))
    survivedtext = font.render("acertos: %d, disparos: %d, precisão: %.2f%%"%res, True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)

   # 7.4 - Desenha barra de vida (vermelha) e sobrepõe a vida (verde)
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))

    # 8 - atualiza a tela
    pygame.display.flip()
    
    # 9 - Responde a eventos
    for event in pygame.event.get():

        # 9.1 Detecta se o botão 'X' foi pressionado
        if event.type==pygame.QUIT:
            go_on = False

        # 9.2 detecta se uma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
        
            # 9.2.1 teclas 'w', 'a', 's' e 'd' movimentam o jogador (acionam flag correspondente)
            if event.key==pygame.K_w:
                keys[0]=True
            elif event.key==pygame.K_a:
                keys[1]=True
            elif event.key==pygame.K_s:
                keys[2]=True
            elif event.key==pygame.K_d:
                keys[3]=True

            # 9.2.2 tecla ESC sai do jogo
            elif event.key==pygame.K_ESCAPE:
                go_on = False
                
            # 9.2.3 espaço atira (cria nova flecha na posição e orientação do jogador)
            elif event.key==pygame.K_SPACE:
                position=pygame.mouse.get_pos()
                acc[1]+=1
                pos_x, pos_y = playerpos1[0]+32, playerpos1[1]+32
                ang = math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26))
                arrows.append([ang, pos_x, pos_y])

        # 9.3 se a techa for levantada zera a flag
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

    # 10 - finalmente move o jogador
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5

pygame.quit() 
