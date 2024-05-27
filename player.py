#Imports
import pygame
import spritesheet as ss

class player():
    def __init__(self, player_pos, player_sprite):
        self.player_pos = player_pos
        self.player_sprite = player_sprite
        self.player_hp = 100
        self.player_walkspeed = 300

    def walk_animation(self):
        return