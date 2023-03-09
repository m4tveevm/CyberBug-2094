import pygame

from data import constants as const
from data.components import tools
from data.states.game_screen import Game_screen


class LevelState(Game_screen):
    def __init__(self):
        super().__init__()
        self.sprites = pygame.sprite.AbstractGroup()
        self.quit, self.next = False, False
        self.time = pygame.time.get_ticks()
        self.start()

    def status(self):
        super().status()

    def start(self):
        self.setup_buttons()
        self.update()
        self.menu_music = tools.load_music("ghoul_music.mp3")
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

    def setup_buttons(self):
        self.game_btn_red()
        self.game_btn_yellow()
        self.game_btn_purple()

    def game_btn_red(self):
        self.button_red = pygame.sprite.Sprite()
        self.button_red.image = tools.load_image("red.png")

        self.button_red.w, self.button_red.h = self.button_red.image.get_size()
        self.button_red.x, self.button_red.y = const.SCREEN_CENTER - self.button_red.w // 2, 0.5 * \
                                                 const.SCREEN_SIZE[-1]

        self.button_red.rect = ((self.button_red.x, self.button_red.y),
                                 (self.button_red.w, self.button_red.h))
        self.button_red.add(self.sprites)

    def game_btn_yellow(self):
        self.button_yellow = pygame.sprite.Sprite()
        self.button_yellow.image = tools.load_image("yellow.png")

        self.button_yellow.w, self.button_yellow.h = self.button_yellow.image.get_size()
        self.button_yellow.x, self.button_yellow.y = const.SCREEN_CENTER - self.button_yellow.w // 2, 0.5 * \
                                                 const.SCREEN_SIZE[-1]

        self.button_yellow.rect = ((self.button_yellow.x, self.button_yellow.y),
                                 (self.button_yellow.w, self.button_yellow.h))
        self.button_yellow.add(self.sprites)

    def game_btn_purple(self):
        self.button_purple = pygame.sprite.Sprite()
        self.button_purple.image = tools.load_image("purple.png")

        self.button_purple.w, self.button_purple.h = [i // 100 for i in self.button_purple.image.get_size()]
        self.button_purple.x, self.button_purple.y = const.SCREEN_CENTER - self.button_purple.w // 2, 0.5 * \
                                                 const.SCREEN_SIZE[-1]

        self.button_purple.rect = ((self.button_purple.x, self.button_purple.y),
                                 (self.button_purple.w, self.button_purple.h))
        self.button_purple.add(self.sprites)

    def get_event(self, event):
        super().get_event(event)
        # if all([self.game_btn_red.x <= pygame.mouse.get_pos()[
        #     0] <= self.game_btn_red.x + self.game_btn_red.w,
        #         self.game_btn_red.y <= pygame.mouse.get_pos()[
        #             1] <= self.game_btn_red.y + self.game_btn_red.h]):
        #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        #     if event.type == pygame.MOUSEBUTTONUP:
        #         pass


    def update(self):
        super().update()

        self.screen.blit(
            pygame.transform.scale(tools.load_image("task_one.png"),
                                   const.SCREEN_SIZE), (0, 0))
        self.sprites.draw(self.screen)
        pygame.display.flip()
