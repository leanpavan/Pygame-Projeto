import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim

surface = pygame.display.set_mode((100,100))
FPS = 120
frames = FPS / 12
strips = [
    SpriteStripAnim('assets/sprites/personagem/personagem1.png', (0,0,24,24), 8, 1, True, frames),
    SpriteStripAnim('assets/sprites/personagem/personagem2.png', (0,0,24,24), 7, 1, True, frames),
    SpriteStripAnim('assets/sprites/personagem/personagem3.png', (0,0,24,24), 4, 1, True, frames)
]
black = Color('black')
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = strips[n].next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()
            elif e.key == K_RETURN:
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter()
    surface.fill(black)
    surface.blit(image, (0,0))
    pygame.display.flip()
    image = strips[n].next()
    clock.tick(FPS)