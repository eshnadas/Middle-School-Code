import pygame
class Food:
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y
        self.screen=screen
        self.rect = pygame.Rect(self.x,self.y,10,10)
        self.apple = pygame.image.load("apple.png")
    def draw(self):
        self.screen.blit(self.apple,(self.x,self.y))
        self.rect = pygame.Rect(self.x,self.y,10,10)