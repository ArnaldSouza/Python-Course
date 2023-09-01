#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 07:28:17 2021

@author: fip
"""

#https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

# 1 - Importando Modulos
import pygame
import math
import random

# ############################################################################
# CLASSES
# ############################################################################
pygame.init()
pygame.font.init()

class Game():
    def __init__(self):
        # 2 - Inicialização

        self.width, self.height = 640, 480                      # tamanho da janela do jogo
        self.screen=pygame.display.set_mode((640, 480))    # incializa a janela
        self.mv_keys = [False, False, False, False]             # botões pressionados
        self.life = 194
        self.arrows=[]                                           # lista de flechas
        self.badguys=[]                                          # lista de inimigos
        self.acc=[0,0]                                           # contador de flechas (acertos e disparos)

        self.badtimer_itv=100                                    # temporizadores de geração de inimigos
        self.badtimer_cnt=0         

    def update_arrows(self, img):
        for arr in self.arrows:
            arr[1]+= int(math.cos(arr[0])*10)
            arr[2]+= int(math.sin(arr[0])*10)

        self.arrows = [b for b in self.arrows if is_pos_valid(b[1], b[2])]

        for arr in self.arrows:
            rotated = pygame.transform.rotate(img, 360-arr[0]*180/math.pi)
            self.screen.blit(rotated, (arr[1], arr[2]))

    def update_badguys_and_check_collisions(self, res):

        # 6.5 - Desenha malvadões - cnt é o contador e itv o intervalo entre geração
        self.badtimer_cnt += 1
        if self.badtimer_cnt >= self.badtimer_itv:
            self.badguys.append([640, random.randint(50,430)])       # posição do x constante, y é randômica
            self.badtimer_cnt = 0
            self.badtimer_itv = max(30, self.badtimer_itv-5)              # diminui o intervalo até chegar no 30

        # 7.1 Detecta se fomos atingidos e remove vilões que chegaram no castelo
        n_hit = len([b for b in self.badguys if b[0]<=64 and b[0]>0])
        self.life -= n_hit*random.randint(2, 7)
        self.badguys = [b for b in self.badguys if b[0]>64]
        
        #7.2 Move vilões e detecta colisões
        for badguy in self.badguys:

            self.screen.blit(res.badguyimg, badguy)
            
            # move (decrementa posição x) e cria retângulo para detectar colisões
            badguy[0]-= 2
            badrect=pygame.Rect(res.badguyimg.get_rect())
            badrect.top=badguy[1]
            badrect.left=badguy[0]
    
            #7.2.1 - detecta colisões com cada flecha
            for bullet in self.arrows:
                bullrect=pygame.Rect(res.arrow.get_rect())
                bullrect.left=bullet[1]
                bullrect.top=bullet[2]
                if badrect.colliderect(bullrect):
                    self.acc[0]+=1
                    badguy[0] = -200        # move o vilão para fora da tela e ele será eliminado
                    bullet[2] = -200

class Player():
    def __init__(self, player_image):
        self.pos = [100,100]
        self.img = player_image

    def move(self, keys):
        if keys[0]:
            self.pos[1]-=5
        elif keys[2]:
            self.pos[1]+=5
        if keys[1]:
            self.pos[0]-=5
        elif keys[3]:
            self.pos[0]+=5

    def draw(self, screen, res):
        mouse_pos = pygame.mouse.get_pos()
        angle = math.atan2(mouse_pos[1]-(self.pos[1]+32),mouse_pos[0]-(self.pos[0]+26))
        angle = 360-angle*180/math.pi                                
        playerrot = pygame.transform.rotate(res.player, angle)
        playerpos1 = (self.pos[0]-playerrot.get_rect().width//2, self.pos[1]-playerrot.get_rect().height//2)
        screen.blit(playerrot, playerpos1) 


class Resource():
    def __init__(self):
        
        # 3 - Carrega imagens
        self.player = pygame.image.load("resources/images/dude.png")             # jogador
        self.grass = pygame.image.load("resources/images/grass.png")             # grama
        self.castle = pygame.image.load("resources/images/castle.png")           # castelo
        self.arrow = pygame.image.load("resources/images/bullet.png")            # flecha
        self.healthbar = pygame.image.load("resources/images/healthbar.png")     # barra de vida (vermelha)
        self.health = pygame.image.load("resources/images/health.png")           # vida (verde)
        self.badguyimg = pygame.image.load("resources/images/badguy.png")       # vilão

# ############################################################################
# FUNÇÕES AVULSAS
# ############################################################################
def is_pos_valid(x_pos, y_pos):
    return x_pos>-64 and x_pos<640 and y_pos>-64 and y_pos<480

def draw_background(screen, res):
    # 5 - Limpa a tela a cada iteração
    screen.fill(0)
    
    # 6 - Desenha elementos na tela
    # 6.1 - Desenha grama
    for x in range(640//res.grass.get_width()+1):
        for y in range(480//res.grass.get_height()+1):
            screen.blit(res.grass,(x*100,y*100))

    # 6.2 - Desenha castelos
    screen.blit(res.castle,(0,30))
    screen.blit(res.castle,(0,135))
    screen.blit(res.castle,(0,240))
    screen.blit(res.castle,(0,345 ))    

def draw_upper_bar(game, res):
        # 7.3 Desenha precisão
        font = pygame.font.Font(None, 24)
        data = (game.acc[0], game.acc[1], 100*game.acc[0]/max(1,game.acc[1]))
        survivedtext = font.render("acertos: %d, disparos: %d, precisão: %.2f%%"%data, True, (0,0,0))
        textRect = survivedtext.get_rect()
        textRect.topright=[635,5]
        game.screen.blit(survivedtext, textRect)
    
       # 7.4 - Desenha barra de vida (vermelha) e sobrepõe a vida (verde)
        game.screen.blit(res.healthbar, (5,5))
        for health1 in range(game.life):
            game.screen.blit(res.health, (health1+8,8))


def on_event(event, game, player):
    must_quit = False
    # 9.1 Detecta se o botão 'X' foi pressionado
    if event.type==pygame.QUIT:
        must_quit = True

    # 9.2 detecta se uma tecla foi pressionada
    if event.type == pygame.KEYDOWN:
    
        # 9.2.1 teclas 'w', 'a', 's' e 'd' movimentam o jogador (acionam flag correspondente)
        if event.key==pygame.K_w:
            game.mv_keys[0]=True
        elif event.key==pygame.K_a:
            game.mv_keys[1]=True
        elif event.key==pygame.K_s:
            game.mv_keys[2]=True
        elif event.key==pygame.K_d:
            game.mv_keys[3]=True

        # 9.2.2 tecla ESC sai do jogo
        elif event.key==pygame.K_ESCAPE:
            must_quit = True
            
        # 9.2.3 espaço atira (cria nova flecha na posição e orientação do jogador)
        elif event.key==pygame.K_SPACE:
            position=pygame.mouse.get_pos()
            game.acc[1]+=1
            pos_x, pos_y = player.pos[0]+32, player.pos[1]+20
            ang = math.atan2(position[1]-pos_y,position[0]-pos_x)
            game.arrows.append([ang, pos_x, pos_y])

    # 9.3 se a techa for levantada zera a flag
    if event.type == pygame.KEYUP:
        if event.key==pygame.K_w:
            game.mv_keys[0]=False
        elif event.key==pygame.K_a:
            game.mv_keys[1]=False
        elif event.key==pygame.K_s:
            game.mv_keys[2]=False
        elif event.key==pygame.K_d:
            game.mv_keys[3]=False
    return must_quit


if __name__ == "__main__":

    game = Game()
    res = Resource()
    player = Player(res.player)

    go_on = True
    while go_on:
        draw_background(game.screen, res)
        player.draw(game.screen, res)

        game.update_arrows(res.arrow)

        game.update_badguys_and_check_collisions(res)

        draw_upper_bar(game, res)

        # 8 - atualiza a tela
        pygame.display.flip()
        
        # 9 - Responde a eventos
        for event in pygame.event.get():
            must_quit = on_event(event, game, player)
            if must_quit:
                pygame.quit() 
                go_on = False
    
        player.move(game.mv_keys)    


