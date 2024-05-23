# Imports
import pygame

# Pygame setup
pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cogumelos X Fungos")

# Framerate
clock = pygame.time.Clock()
FPS = 30

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Square(pygame.sprite.Sprite):
    def __init__(self,col,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

square = Square("crimson", 500,300)

# Create sprite group for squares
squares = pygame.sprite.Group()
squares.add(square)


# Main game loop
running = True
while running:
    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clock
    dt = clock.tick(FPS) / 1000
    # Update background
    screen.fill('black')
    # Update sprite group
    squares.update()
    # Draw sprite group
    squares.draw(screen)


    pygame.draw.rect(screen,(100,200,80),(100,300,60,20))
    pygame.draw.circle(screen, "red", player_pos, 40)

    # Character Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.update()



# Quit
pygame.quit()