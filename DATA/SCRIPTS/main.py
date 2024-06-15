# imports
import pygame, sys

# imports self library
from DATA.SCRIPTS.settings  import *
from DATA.SCRIPTS.level     import Level
import DATA.SCRIPTS.GUI     as gui_

class Game:
    def __init__(self):

        # Game_state
        self.game_state = {
            'QUIT': False,
            'MENU': True,
            'Game': False
        }

        #General setup
        pygame.init()
        pygame.display.set_caption('ds2D')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.level_obj = Level()

    def run(self):
        while True:
            if self.game_state['Game']:
                self.level_obj.run()

            if self.game_state['MENU']:
                gui_.main_menu(self.game_state)

            if self.game_state['QUIT']:
                self.quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

            pygame.display.update()
            self.clock.tick(FPS)

    def quit(self):
        print("\n!!! Game ended !!!")
        pygame.quit()
        sys.exit()

print("main.py loaded!")
