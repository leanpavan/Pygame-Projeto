# imports
import pygame

# imports self library
import DATA.SCRIPTS.settings    as sett_

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((sett_.TILEZISE,sett_.TILEZISE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            # do an offset
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - sett_.TILEZISE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)

print("tile.py loaded!")
