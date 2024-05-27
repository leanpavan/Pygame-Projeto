# Imports
import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        return image

# used in main.py ↓ 
class Square(pygame.sprite.Sprite):
    def __init__(self,col,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


# loader image ↓
sprite_sheet_image = lambda: pygame.image.load("assets/sprites/personagem/sheets/DinoSprites - vita.png").convert_alpha()

# define as image in pygame ↓
sprite_sheet = lambda: SpriteSheet(sprite_sheet_image())
