import pygame
def serra_t(self,s):
    if s == 1:
       self.se = pygame.image.load("img/serra3.png")
       self.se = pygame.transform.rotate(self.se, 0)
       return self.se
    elif s == 2:
       self.se = pygame.image.load("img/serra3.png")
       self.se = pygame.transform.rotate(self.se, 45)
       return self.se
