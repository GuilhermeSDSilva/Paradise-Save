from config import *
from player import *
from plataformas import *
import sys
import pygame

class Game_rodas:
    def fase1(self):
        pygame.init()

        # desenhar tela (dentro de config)
        SCREEN = screen
        
        # informacões do player
        player = play(self)
        player_x = 10
        player_y = 570
        direita = False
        esquerda = False
        pulo = False

        pode_pular = True
        # so vai poder pular novamente quando o player_y for igual ao ponto_inicial
        ponto_inicial = 0

        player_y_pulo = player_y

        #gravidade
        caindo = True

        # desenhar plataformas
        plataform1 = plat_m(self)
        plataform2 = plat_m(self)
        plataform3 = plat_m(self)
        plataform4 = plat_m(self)

        
        
        while True:
            SCREEN.fill(SCREEN_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        direita = True
                    if event.key == pygame.K_a:
                        esquerda = True
                    if event.key == pygame.K_w:
                        pulo = True
                        ponto_inicial = player_y
                      
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        direita = False
                    if event.key == pygame.K_a:
                        esquerda = False
    
            #desenhar player
            SCREEN.blit(player, (player_x, player_y))

            #desenhar plataformas
            SCREEN.blit(plataform1, (0, 600))
            SCREEN.blit(plataform1, (100, 500))
            SCREEN.blit(plataform1, (200, 400))
            SCREEN.blit(plataform1, (300, 300))

            # movimentacão do player
            if (direita is True):
                player_x += 1
            if (esquerda is True):
                player_x -= 1

            # fisica para cair
            if(caindo is True):
                player_y +=1
            else:
                plyaer_y = player_y

            # colisão com as plataformas
            caindo = coli_plat(self, player_x, player_y)

            # condicão para o pulo
            if(pulo is True) and (pode_pular is True):
                caindo = False
                player_y_pulo = player_y_pulo
                player_y -=1
            else:
                player_y_pulo = player_y
                
            # voltar do pulo   
            if player_y <= player_y_pulo - 120:
                pulo=False
                pode_pular = False

            if player_y == ponto_inicial:
                pode_pular = True
            

            
            
            pygame.display.flip()
        pygame.quit()
