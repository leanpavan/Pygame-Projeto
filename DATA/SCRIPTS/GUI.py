# imports
import pygame, sys

# imports self library
from DATA.SCRIPTS.button    import Button
from DATA.SCRIPTS.settings  import *

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
BG = pygame.image.load("DATA/main_menu/BG.png")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("DATA/main_menu/font.ttf", size)

def main_menu(game_state:dict):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        #para mudar a cor/nome do menu
        MENU_TEXT = get_font(75).render("PROJETO GRADIENTE", True, "#eff0e4")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("DATA/main_menu/Play Rect.png"), pos=(640, 400),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("DATA/main_menu/Quit Rect.png"), pos=(640, 600),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_state['MENU'] = False
                    game_state['Game'] = True
                    return game_state
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_state['QUIT'] = True
                    return game_state

        pygame.display.update()

print("GUI.py loaded!")
