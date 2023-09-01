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

# 2.1 -Tela inicial
width, height = 640, 480                            # tamanho da janela do jogo
screen=pygame.display.set_mode((width, height))     # incializa a janela

# 2.2 - Posição do Jogador
playerpos = [100,100]

# 2.3 - lista de inimigos [pos_x, pos_y], temporizadores para a criação
badguys=[]                                          
badtimer_itv=100                                   
badtimer_cnt=0
# 2.4 - lista de flechas [angulo, pos_x, pos_y]
arrows=[]

# 2.5 - vida do jogador
vida=194

# 2.6 - contador de flechas [flechas_no_alvo, total_de_flechas]
acc=[0,0]

# 2.7 - booleanos indicando tecla pressionada
keys = [False, False, False, False]  
                               # @2    
# 3 - Carrega imagens
player = pygame.image.load("resources/images/dude.png")             # jogador
grass = pygame.image.load("resources/images/grass.png")             # grama
castle = pygame.image.load("resources/images/castle.png")           # castelo
badguyimg = pygame.image.load("resources/images/badguy.png")       # @3
arrow = pygame.image.load("resources/images/bullet.png")            # @3
healthbar = pygame.image.load("resources/images/healthbar.png")     # barra de vida (vermelha)
health = pygame.image.load("resources/images/health.png")           # vida (verde)

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
    
    #6.3 - Desenha jogador
    screen.blit(player, playerpos)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pl_x, pl_y = playerpos[0]+26, playerpos[1]+32
    delta_x, delta_y = mouse_x - pl_x, mouse_y-pl_y
    angle = math.atan2(delta_y, delta_x)
    angle = 360-angle*180/math.pi                                
    playerrot = pygame.transform.rotate(player, angle)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width//2, playerpos[1]-playerrot.get_rect().height//2)
    screen.blit(playerrot, playerpos1)
    
    # 6.4 - Desenha flechas: flecha = [angulo, pos_x, pos_y]
    # movimenta cada flecha (atualiza a posição)
    for bullet in arrows:
        bullet[1]+= int(math.cos(bullet[0])*10)
        bullet[2]+= int(math.sin(bullet[0])*10)

    #remove flechas fora da janela
    arrows = [b for b in arrows if b[1]>-64 and b[1]<640 and b[2]>-64 and b[2]<480]
    
    # rotaciona e desenha
    for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*180/math.pi)
            screen.blit(arrow1, (projectile[1], projectile[2]))
            
    # 6.5 - Desenha malvadões - cnt é o contador e itv o intervalo entre geração
    badtimer_cnt += 1
    if badtimer_cnt >= badtimer_itv:
        badguys.append([640, random.randint(50,430)])       # posição do x constante, y é randômica
        badtimer_cnt = 0
        badtimer_itv = max(30, badtimer_itv-5)              # diminui o intervalo até chegar no 30

    for badguy in badguys:                      # movimenta e desenha
        badguy[0]-= 2
        screen.blit(badguyimg, badguy)
    
    # 7.1 Detecta se fomos atingidos e remove vilões que chegaram no castelo
    #n_hit = len([b for b in badguys if b[0]<=64 and b[0]>0])
    n_hit = 0
    for b in badguys:
        if b[0]<=64 and b[0]>0:
            n_hit = n_hit+1
    vida -= n_hit*5
    
    # 7.2 - Para cada vilão cria um retângulo circunscrito (ao redor)
    for badguy in badguys:

        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]

        # para cada flecha cria um retângulo também
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]

            # 7.2.1 - testa se tem sobreposição entre os retângulos
            # testa se tem sobreposição entre os retângulos
            # se tiver seta a coordenada 'x' para um número inválido
            # e os itens serão removidos na próxima iteração
            if badrect.colliderect(bullrect):
                badguy[0] = -200        # move o vilão para fora da tela e ele será eliminado
                bullet[1] = -200
            #7.2.1 - testa se tem sobreposição entre os retângulos    
            acc[0]+=1
    
    # 7.3 remove os que estiverem na esquerda da tela
    badguys = [b for b in badguys if b[0]>64]
        
    # 7.4 Desenha precisão
    font = pygame.font.Font(None, 24)
    res = (acc[0], acc[1], 100*acc[0]/max(1,acc[1]))
    survivedtext = font.render("acertos: %d, disparos: %d, precisão: %.2f%%"%res, True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)
    
    # 7.5 - Desenha barra de vida (vermelha) e sobrepõe a vida (verde)
    screen.blit(healthbar, (5,5))
    for health1 in range(vida):
        screen.blit(health, (health1+8,8))
           
    
    
    # 8 - atualiza a tela
    pygame.display.flip()

    # 9 - Responde a eventos
    for event in pygame.event.get():

        # 9.1 Detecta se o botão 'X' foi pressionado
        if event.type==pygame.QUIT:
            go_on = False

        # 9.2 Detecta tecla pressionada
            if 0:
            if event.type == pygame.KEYDOWN:  
        
            # 9.2.1 Detecta tecla ESC
            if event.key==pygame.K_ESCAPE:
                go_on = False
                
            # 9.2.2 espaço atira (cria nova flecha na posição e orientação do jogador)

            if 0:
                pass
            elif event.key==pygame.K_SPACE:
                position=pygame.mouse.get_pos()
                pos_x, pos_y = playerpos1[0]+32, playerpos1[1]+32
                ang = math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26))
                arrows.append([ang, pos_x, pos_y])  
                                              # 9.2
            # 9.2.3 espaço atira (cria nova flecha na posição e orientação do jogador)
            acc[1]+=1
            
            # 9.2.4 teclas 'w', 'a', 's' e 'd' movimentam o jogador (acionam flag correspondente)
            if event.key==pygame.K_w:
                keys[0]=True
            elif event.key==pygame.K_a:
                keys[1]=True
            elif event.key==pygame.K_s:
                keys[2]=True
            elif event.key==pygame.K_d:
                keys[3]=True
                
        #9.3
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
    
# Passo 9 -  Sua vez
# escolha uma destas funcionalidades (ou invente uma)
# e adicione ao jogo:

# Lançar várias flechas ao mesmo tempo
# Tecla que aciona bomba que mata todos os inimgos ativos
# Adicionar música/efeito sonoro
# Fim de jogo (vitória/derrota)
# Tipo diferente de inimigo (talvez com vida)
# Opção a sua escolha