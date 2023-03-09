import pygame

from data import constants as const
from data.components import tools
from data.states.game_screen import Game_screen


class MainMenuState(Game_screen):
    def __init__(self):
        super().__init__()
        self.start_time = 0
        self.sprites = pygame.sprite.AbstractGroup()
        self.start()

    def status(self):
        super().status()
        if self.done:
            return self.next

    def start(self):
        pygame.mouse.set_visible(True)
        self.setup_title()
        self.setup_buttons()
        self.update()
        self.menu_music = tools.load_music("menu_music.mp3")
        self.menu_music.play(loops=9999999, fade_ms=100)
        self.music_playing = True
        self.runing()

    def change_misic_status(self):
        if self.music_playing:
            self.menu_music.stop()
            self.music_playing = False
        else:
            self.menu_music.play(loops=9999999, fade_ms=100)
            self.music_playing = True

    def music_off(self):
        super().music_off()
        self.menu_music.stop()
        self.music_playing = False

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

        self.menu_volume_button()

    def menu_button_play(self):
        self.button_play = pygame.sprite.Sprite()
        self.button_play.image = tools.load_image("btn_play.png")

        self.button_play.w, self.button_play.h = self.button_play.image.get_size()
        self.button_play.x, self.button_play.y = const.SCREEN_CENTER - self.button_play.w // 2, 0.5 * \
                                                 const.SCREEN_SIZE[-1]

        self.button_play.rect = ((self.button_play.x, self.button_play.y),
                                 (self.button_play.w, self.button_play.h))
        self.button_play.add(self.sprites)

    def menu_volume_button(self):
        self.button_volume = pygame.sprite.Sprite()
        self.button_volume.image = tools.load_image("btn_volume.png")
        self.button_volume.w, self.button_volume.h = self.button_play.image.get_size()
        self.button_volume.x, self.button_volume.y = const.SCREEN_SIZE[0] * 0.01, 0.7 * \
                                                     const.SCREEN_SIZE[1]
        self.button_volume.rect = ((self.button_volume.x, self.button_volume.y),
                                   (self.button_volume.w, self.button_volume.h))
        self.button_volume.add(self.sprites)

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
        super().get_event(event)
        if all([self.button_play.x <= pygame.mouse.get_pos()[
            0] <= self.button_play.x + self.button_play.w,
                self.button_play.y <= pygame.mouse.get_pos()[
                    1] <= self.button_play.y + self.button_play.h]):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONUP:
                self.done = True
        elif all([self.button_quit.x <= pygame.mouse.get_pos()[
            0] <= self.button_quit.x + self.button_quit.w,
                  self.button_quit.y <= pygame.mouse.get_pos()[
                      1] <= self.button_quit.y + self.button_quit.h]):
            if event.type == pygame.MOUSEBUTTONUP:
                self.quit = True
        elif all([self.button_volume.x <= pygame.mouse.get_pos()[
            0] <= self.button_volume.x + self.button_volume.w,
                  self.button_volume.y <= pygame.mouse.get_pos()[
                      1] <= self.button_volume.y + self.button_volume.h]):
            if event.type == pygame.MOUSEBUTTONUP:
                self.change_misic_status()

    def update(self):
        super().update()

        self.screen.blit(pygame.transform.scale(tools.load_image("menu_background.png"),
                                                const.SCREEN_SIZE), (0, 0))
        self.sprites.draw(self.screen)
        pygame.display.flip()
