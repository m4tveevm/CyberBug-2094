import pygame, random

from data import constants as const
from data.components import tools


class Game_Screen():
    def __init__(self):
        self.music_playing = False
        self.curent_state = const.CURRENT_STATE
        self.quit, self.next = False, False
        self.screen_init()
        self.states_music = tools.load_music("menu_music.mp3")
        self.crush_time = random.randint(100, 300)
        self.start_ticks = pygame.time.get_ticks()

    def screen_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(const.SCREEN_SIZE)
        pygame.display.set_icon(tools.load_image(const.GAME_ICON_LOCATION))
        pygame.display.set_caption(const.GAME_NAME)

    def update(self):
        pass

    def change_misic_status(self):
        if self.music_playing:
            self.states_music.stop()
            self.music_playing = False
        else:
            self.states_music.play(loops=9999999, fade_ms=100)
            self.music_playing = True

    def music_off(self):
        self.states_music.stop()
        self.music_playing = False

    def status(self):
        if self.quit:
            return True

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def is_error(self):
        if (pygame.time.get_ticks() - self.start_ticks) / 300 > len(
                const.THE_BEST_GAME_EVER) + self.crush_time:
            return True

    def is_next(self):
        if self.next:
            return True

    def runing(self):
        while True:
            if self.is_error():
                const.CURRENT_STATE = const.STATUS[const.STATUS.index('bug')]
                print('Oops, game has crashed!')
                break
            if self.is_next():
                break
            if self.quit:
                const.CURRENT_STATE = False
                break
            for event in pygame.event.get():
                if self.quit:
                    break
                self.get_event(event)
            self.update()
