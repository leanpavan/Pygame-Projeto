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

# Create animation list
animation_list = []
animation_steps = [4, 6, 3, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldow = 150
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(spritesheet.sprite_sheet().get_image(step_counter, 24,24, 3))
        step_counter += 1
    animation_list.append(temp_img_list)

# Framerate
clock = pygame.time.Clock()
FPS = 30

# Player
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 300

# Game Loop
running = True
while running:

    # Update background
    screen.fill(BG)

    # Clock
    dt = clock.tick(FPS) / 1000

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldow:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0


    # Show frame image
    print(frame)
    screen.blit(animation_list[action][frame], (player_pos,player_pos))


    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
        action = 1
    elif keys[pygame.K_d]:
        player_pos.x += player_speed * dt
        action = 1
    elif keys[pygame.K_a] == False and keys[pygame.K_d] == False:
        if frame >= 4:
            frame = 0
        action = 0


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
