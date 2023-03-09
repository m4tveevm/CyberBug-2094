import pygame, random

from data import constants as const
from data.components import tools


class Game_screen():
    def __init__(self):
        self.curent_state = const.CURENT_STATE
        self.quit, self.next = False, False
        self.screen_init()
        self.crush_time = random.randint(100, 40000) * random.randint(1000, 10000)
        self.start_ticks = pygame.time.get_ticks()

    def screen_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(const.SCREEN_SIZE)
        pygame.display.set_icon(tools.load_image(const.GAME_ICON_LOCATION))
        pygame.display.set_caption(const.GAME_NAME)

    def update(self):
        pass

    def music_off(self):
        pass

    def status(self):
        if self.quit:
            return True

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def is_error(self):
        if (pygame.time.get_ticks() - self.start_ticks) / 1000 > len(
                const.THE_BEST_GAME_EVER) + self.crush_time:
            return True

    def is_next(self):
        if self.next:
            return True

    def runing(self):
        while True:
            if self.is_error():
                const.CURENT_STATE = const.STATUS[const.STATUS.index('bug')]
                break
            if self.is_next():
                break
            if self.quit:
                const.CURENT_STATE = False
                break
            for event in pygame.event.get():
                if self.quit:
                    break
                self.get_event(event)
                self.update()
