# Imports librarys
import pygame
import tkinter as tk

# Imports self.librarys
import ssss as ss_
import animations as an_
import player as pl_


# Pygame setup
pygame.init()

# Screen
root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Jogo")

# Spritesheet import

player_sheet = pygame.image.load("assets/sprites/personagem/sheets/DinoSprites - vita.png").convert_alpha()
sprite_sheet = ss_.SpriteSheet(player_sheet)

BG = "#aaaaaa"
BLACK = "#000000"

# Create animation object
an_.animation.create_animation_list(player_sheet)

# Framerate
clock = pygame.time.Clock()
FPS = 60

# Player
player = pl_.player(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), sprite_sheet)

# Game Loop
running = True
while running:

    # Update background
    screen.fill(BG)

    # Clock
    dt = clock.tick(FPS) / 1000

    # Update animation
    current_time = pygame.time.get_ticks()
    an_.animation.update_animation(current_time)

    # Show frame image
    screen.blit(an_.animation.animation_list[an_.animation.action][an_.animation.frame], (player.player_pos,player.player_pos))

    # Player movement
    keys = pygame.key.get_pressed()
    player.movement(keys,dt)


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.update()
