import pygame

def play(self):
    self.play = pygame.image.load("img/player.png")
    self.play = pygame.transform.scale(self.play, (40, 40))
    return self.play
