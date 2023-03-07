import pygame

from data import constants as const
from data.components import tools
from data.states.game_screen import Game_screen


class MainMenuState(Game_screen):
    def __init__(self, start_time):
        super().__init__()
        self.start_time = start_time
        self.sprites = pygame.sprite.AbstractGroup()
        self.start()

    def start(self):
        pygame.mouse.set_visible(True)
        self.screen_init()
        self.setup_title()
        self.setup_buttons()
        self.update(self.screen, 0)
        while True:
            for event in pygame.event.get():
                pygame.display.flip()
                self.get_event(event)

    def setup_title(self):
        self.title = pygame.sprite.Sprite()
        self.title.image = tools.load_image("main_title.png")
        self.title.rect = (
            ((const.SCREEN_SIZE[0] * 0.1), self.title.image.get_size()[0] * 0.1),
            self.title.image.get_size())
        self.title.add(self.sprites)

    def setup_buttons(self):
        self.menu_button_play()
        self.menu_button_quit()
        self.menu_button_settings()

    def menu_button_play(self):
        self.button_play = pygame.sprite.Sprite()
        self.button_play.image = tools.load_image("btn_play.png")

        self.button_play.w, self.button_play.h = self.button_play.image.get_size()
        self.button_play.x, self.button_play.y = const.SCREEN_CENTER - self.button_play.w // 2, 0.5 * \
                                                 const.SCREEN_SIZE[-1]

        self.button_play.rect = ((self.button_play.x, self.button_play.y),
                                 (self.button_play.w, self.button_play.h))
        self.button_play.add(self.sprites)

    def menu_button_quit(self):
        self.button_quit = pygame.sprite.Sprite()
        self.button_quit.image = tools.load_image("btn_quit.png")

        self.button_quit.w, self.button_quit.h = self.button_quit.image.get_size()
        self.button_quit.x, self.button_quit.y = const.SCREEN_CENTER - self.button_quit.w // 2, 0.8 * \
                                                 const.SCREEN_SIZE[-1]

        self.button_quit.rect = ((self.button_quit.x, self.button_quit.y),
                                 (self.button_quit.w, self.button_quit.h))
        self.button_quit.add(self.sprites)

    def menu_button_settings(self):
        self.button_settings = pygame.sprite.Sprite()
        self.button_settings.image = tools.load_image("btn_settings.png")

        self.button_settings.w, self.button_settings.h = self.button_settings.image.get_size()
        self.button_settings.x, self.button_settings.y = const.SCREEN_CENTER - self.button_settings.w // 2, 0.65 * \
                                                         const.SCREEN_SIZE[-1]

        self.button_settings.rect = ((self.button_settings.x, self.button_settings.y),
                                     (self.button_settings.w, self.button_settings.h))
        self.button_settings.add(self.sprites)

    def get_event(self, event):
        if all([self.button_play.x <= pygame.mouse.get_pos()[
            0] <= self.button_play.x + self.button_play.w,
                self.button_play.y <= pygame.mouse.get_pos()[
                    1] <= self.button_play.y + self.button_play.h]):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.mouse.set_visible(False)
                self.next = const.LEVEL
                self.done = True

        elif all([self.button_quit.x <= pygame.mouse.get_pos()[
            0] <= self.button_quit.x + self.button_quit.w,
                  self.button_quit.y <= pygame.mouse.get_pos()[
                      1] <= self.button_quit.y + self.button_quit.h]):
            if event.type == pygame.MOUSEBUTTONUP:
                self.quit = True
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def update(self, display, current_time):
        self.current_time = current_time

        # scale = pygame.transform.scale(
        #     background_img, (background_img.get_width() // 2,
        #                background_img.get_height() // 2))
        #
        # scale_rect = scale.get_rect(
        #     center=(200, 150))
        #
        # sc.blit(scale, scale_rect)

        self.screen.blit(pygame.transform.scale(tools.load_image("menu_background.png"),
                                                const.SCREEN_SIZE), (0, 0))
        self.sprites.draw(display)
