import pygame
from config import *


class Game_rodas:
    def fase1_1(self):

        SCREEN = screen

        while True:
            SCREEN.fill(SCREEN_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()

            pygame.display.flip()
        pygame.quit()


    def fase1_2(self):

        SCREEN = screen

        while True:
            SCREEN.fill(SCREEN_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()

            pygame.display.flip()
        pygame.quit()
