import pygame

def play(self):
    self.play = pygame.image.load("img/player.png")
    self.play = pygame.transform.scale(self.play, (30, 30))
    return self.play

def coli_plat(self,play_x,play_y):
    # colisão plataforma 1
    if(0 < play_x < 100) and ( 585 < play_y < 588):
        self.cond = False
        return self.cond
    # colisão plataforma 2
    elif(100 < play_x < 200) and ( 485 < play_y < 488):
        self.cond = False
        return self.cond
    # colisão plataforma 2
    elif(200 < play_x < 300) and ( 385 < play_y < 388):
        self.cond = False
        return self.cond
    # colisão plataforma 2
    elif(300 < play_x < 400) and ( 285 < play_y < 288):
        self.cond = False
        return self.cond

    
    else:
        self.cond = True
        return self.cond
    

