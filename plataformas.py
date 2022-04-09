import pygame

def plat_m(self):
    self.c = pygame.image.load("img/plat.png")
    self.c = pygame.transform.scale(self.c, (100,50))
    return self.c
