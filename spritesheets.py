# Imports
import pygame
import spritesheet

# Pygame setup
pygame.init()

# Screen
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Spritesheets")

# Spritesheet
sprite_sheet_image = pygame.image.load("assets/sprites/personagem/personagem_spritesheet.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


frame_0 = sprite_sheet.get_image(0, 32,32, 3)
frame_1 = sprite_sheet.get_image(1, 32,32, 3)

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
