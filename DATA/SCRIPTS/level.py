# imports
import pygame
from random import choice

# imports self library
import DATA.SCRIPTS.settings    as sett_
from DATA.SCRIPTS.tile          import Tile
from DATA.SCRIPTS.player        import Player
from DATA.SCRIPTS.support       import *

class Level:
    def __init__(self):

        #get the display surface
        self.screen = pygame.display.get_surface()
        self.display = self.display = pygame.Surface((self.screen.get_width()/4, self.screen.get_height()/4)).convert()

        #Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

        self.player_obj = Player((self.display.get_width()/2,self.display.get_height()/2), [self.visible_sprites], self.obstacle_sprites)

    def create_map(self):
        # layouts = {
        #     'boundary': import_csv_layout('DATA\ds2d_sprites\CSV\pain._void.csv'),
        #     'grass': import_csv_layout('DATA/graphics/map/map_Grass.csv'),
        #     'object': import_csv_layout('DATA/graphics/map/map_Objects.csv')
        # }
        # graphics = {
        #     'grass': import_folder('DATA/graphics/grass'),
        #     'objects': import_folder('DATA/graphics/objects')
        # }

        # for style,layout in layouts.items():
        #     for row_index, row in enumerate(layout):
        #         for col_index, col in enumerate(row):
        #             if col != '-1':
        #                 x = col_index * sett_.TILEZISE
        #                 y = row_index * sett_.TILEZISE
        #                 if style == 'boundary':
        #                     Tile((x,y), [self.obstacle_sprites], 'invisible')
        #                 if style == 'grass':
        #                     random_grass_image = choice(graphics['grass'])
        #                     Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'grass', random_grass_image)
        #                 if style == 'object':
        #                     surf = graphics['objects'][int(col)]
        #                     Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
        ...

    def run(self):
        #self.display.fill('#0d0d0d')
        #update and draw the game
        self.visible_sprites.custom_draw(self.player_obj)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__(self)
        self.screen = pygame.display.get_surface()
        self.display = self.display = pygame.Surface((self.screen.get_width()/4, self.screen.get_height()/4)).convert()
        self.half_width = self.display.get_size()[0] // 2
        self.half_height = self.display.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surface = pygame.image.load('DATA\ds2d_sprites\ground_pain.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0,0))

    def custom_draw(self, player):

        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display.blit(self.floor_surface, floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_position)

        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))

print("level.py loaded!")
