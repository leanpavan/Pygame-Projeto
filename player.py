#Imports
import pygame
import animations as an_
import spritesheet as ss_

class player():
    def __init__(self, player_pos, player_sprite):
        self.player_pos = player_pos
        self.player_sprite = player_sprite
        self.player_hp = 100
        self.player_walkspeed = 300

    def movement(self,keys:list,dt:float):
        '''Keys: pygame.key.get_pressed()
        dt: clock game'''
        if keys[pygame.K_a]:
            self.player_pos.x -= self.player_walkspeed * dt
            an_.animation.action = 1
        elif keys[pygame.K_d]:
            self.player_pos.x += self.player_walkspeed * dt
            an_.animation.action = 1
        elif keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            if an_.animation.frame >= 4:
                an_.animation.frame = 0
            an_.animation.action = 0