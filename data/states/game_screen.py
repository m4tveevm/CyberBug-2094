import pygame

from data import constants as const
from data.components import tools


class Game_screen():
    def screen_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(const.SCREEN_SIZE)
        pygame.display.set_icon(tools.load_image(const.GAME_ICON_LOCATION))
        pygame.display.set_caption('CyberBug 2084™')