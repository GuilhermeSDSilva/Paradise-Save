from config import *
from player import *
from plataformas import *
from serra import *
import sys
import pygame


class Inicial:
    def tela_inicial(self):
        pygame.init()
        SCREEN = screen


        f1 = 20
        f2 = 20
        escolha = 1
        
        score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
        score_text = score_font.render('INICIO', True, "blue", SCREEN_COLOR)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (500, 50)
        
        f1_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
        f1_text = f1_font.render('Fase 1', True, "blue", SCREEN_COLOR)
        f1_text_rect = f1_text.get_rect()
        f1_text_rect.center = (500, 400)

        f2_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
        f2_text = f2_font.render('Fase 2', True, "blue", SCREEN_COLOR)
        f2_text_rect = f2_text.get_rect()
        f2_text_rect.center = (500, 500)




        
        while True:
            SCREEN.fill(SCREEN_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if escolha == 1:
                            escolha += 1
                        else:
                            escolha -= 1
                    if event.key == pygame.K_s:
                        
                        if escolha == 2:
                            escolha -= 1
                        else:
                            escolha += 1
                    if event.key == pygame.K_SPACE:
                        if escolha == 1:
                            GR.fase1()
                        else:
                            GR2.fase2()
                      
    
            screen.blit(score_text, score_text_rect)
            screen.blit(f1_text, f1_text_rect)
            screen.blit(f2_text, f2_text_rect)


            if escolha == 1:
                f1_text = f1_font.render('Fase 1', True, "green", SCREEN_COLOR)
            else:
                f1_text = f1_font.render('Fase 1', True, "blue", SCREEN_COLOR)

            if escolha == 2:
                f2_text = f2_font.render('Fase 2', True, "green", SCREEN_COLOR)
            else:
                f2_text = f2_font.render('Fase 2', True, "blue", SCREEN_COLOR)
            
            pygame.display.flip()
        pygame.quit()
        
INI = Inicial()


class Game_rodas2:
    def fase2(self):
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

        
        
        armadilha = pygame.image.load("img/armadilha.png")
        armadilha = pygame.transform.scale(armadilha, (200,90))
        armadilha_x = 400
        arm_direita= True
        
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
            plataforma = pygame.draw.rect(SCREEN, "green",(0,625,1000,20))


             #desenhar armadilha
            SCREEN.blit(armadilha, (armadilha_x, 550))
            


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
            if player_y >= 595:
                caindo = False
            else:
                caindo = True
                
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

            # movimentp da armadilha
            if arm_direita is True:
                armadilha_x += 1
            elif arm_direita is False:
                armadilha_x -= 1
            # direcao da armadilha
            if armadilha_x >= 700:
                arm_direita = False
            elif armadilha_x <= 400:
                arm_direita = True
            
            # condicão para quando perder
            if(  armadilha_x - 10 <= player_x <= armadilha_x + 190 ) and (player_y > 590):
                player_x = 10
            
            
            pygame.display.flip()
        pygame.quit()
GR2 = Game_rodas2()

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
        plataform5 = plat_m(self)
        plataform6 = plat_m(self)
        plataform7 = plat_m(self)
        

         
        
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
            SCREEN.blit(plataform2, (100, 500))
            SCREEN.blit(plataform3, (200, 400))
            SCREEN.blit(plataform4, (300, 300))
            SCREEN.blit(plataform5, (500, 300))
            SCREEN.blit(plataform6, (700, 300))
            SCREEN.blit(plataform7, (900, 300))

            #desenhar passagem
            passagem = pygame.draw.rect(SCREEN, "red", (940,266,30,50))
            
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
            caindo = coli_plat_f1(self, player_x, player_y)

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
     
            if  920<player_x<960:
                GR2.fase2()

            if player_y >= 700:
                player_x = 10
                player_y = 570
                
            pygame.display.flip()
        pygame.quit()



    
