import pygame

from data import constants as const
from data.components import tools


class Game_screen():
    def __init__(self):
        self.curent_state = const.CURENT_STATE
        self.quit = False
        self.screen_init()

    def screen_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(const.SCREEN_SIZE)
        pygame.display.set_icon(tools.load_image(const.GAME_ICON_LOCATION))
        pygame.display.set_caption('CyberBug 2084™')

    def runing(self):
        while True:
            if self.quit:
                break
            for event in pygame.event.get():
                self.curent_state.get_event(event)
                self.curent_state.update()