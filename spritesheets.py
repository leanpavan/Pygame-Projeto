# Imports
import pygame

# Pygame setup
pygame.init()

# Screen
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Spritesheets")

# Spritesheet import
'''  
    sprite_sheet e sprite_sheet_image apenas funcionam depois da
    definição do "pygame.display" e "pygame.init()"  
'''
import spritesheet

BG = "#aaaaaa"
BLACK = "#000000"


frame_0 = spritesheet.sprite_sheet.get_image(0, 32,32, 3)
frame_1 = spritesheet.sprite_sheet.get_image(1, 32,32, 3)

# Framerate
clock = pygame.time.Clock()
FPS = 30

# Game Loop
running = True
while running:

    # Update background
    screen.fill(BG)

    # Show frame image
    screen.blit(frame_0, (0,0))
    screen.blit(frame_1, (100,0))


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
