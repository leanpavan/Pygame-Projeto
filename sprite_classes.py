# Imports
import pygame

class Square(pygame.sprite.Sprite):
    def __init__(self,col,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)