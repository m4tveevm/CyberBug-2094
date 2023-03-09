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

        # hidden params of colors
        self.color_red = False
        self.color_yellow = False
        self.color_purple = False

        self.start()

    def status(self):
        super().status()

    def start(self):
        # self.setup_buttons()
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

    def game_btn_red(self):
        self.color_red_sprite = pygame.sprite.Sprite()
        self.color_red_sprite.image = tools.load_image("task_one_1.png")

        self.color_red_sprite.w, self.color_red_sprite.h = const.SCREEN_SIZE
        self.color_red_sprite.x, self.color_red_sprite.y = 0, 0

        self.color_red_sprite.rect = ((self.color_red_sprite.x, self.color_red_sprite.y),
                                      (self.color_red_sprite.w, self.color_red_sprite.h))
        self.color_red_sprite.add(self.sprites)

    def game_btn_yellow(self):
        self.color_yellow_sprite = pygame.sprite.Sprite()
        self.color_yellow_sprite.image = tools.load_image("task_one_2.png")

        self.color_yellow_sprite.w, self.color_yellow_sprite.h = const.SCREEN_SIZE
        self.color_yellow_sprite.x, self.color_yellow_sprite.y = 0, 0

        self.color_yellow_sprite.rect = (
            (self.color_yellow_sprite.x, self.color_yellow_sprite.y),
            (self.color_yellow_sprite.w, self.color_yellow_sprite.h))
        self.color_yellow_sprite.add(self.sprites)

    def game_btn_purple(self):
        self.color_purple_sprite = pygame.sprite.Sprite()
        self.color_purple_sprite.image = tools.load_image("task_one_3.png")

        self.color_purple_sprite.w, self.color_purple_sprite.h = const.SCREEN_SIZE
        self.color_purple_sprite.x, self.color_purple_sprite.y = 0, 0

        self.color_purple_sprite.rect = (
            (self.color_purple_sprite.x, self.color_purple_sprite.y),
            (self.color_purple_sprite.w, self.color_purple_sprite.h))
        self.color_purple_sprite.add(self.sprites)

    def game_btn_background(self):
        self.color_background_sprite = pygame.sprite.Sprite()
        self.color_background_sprite.image = tools.load_image("task_one_4.png")

        self.color_background_sprite.w, self.color_background_sprite.h = const.SCREEN_SIZE
        self.color_background_sprite.x, self.color_background_sprite.y = 0, 0

        self.color_background_sprite.rect = (
            (self.color_background_sprite.x, self.color_background_sprite.y),
            (self.color_background_sprite.w, self.color_background_sprite.h))
        self.color_background_sprite.add(self.sprites)

    def get_event(self, event):
        super().get_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
            if event.key == pygame.K_1:
                self.color_red = True
            if event.key == pygame.K_2:
                self.color_yellow = True
            if event.key == pygame.K_3:
                self.color_red = True

    def update(self):
        super().update()
        if self.color_yellow:
            self.game_btn_yellow()
        if self.color_purple:
            self.game_btn_purple()
        if self.color_red:
            self.game_btn_red()
            self.game_btn_background()
        self.screen.blit(
            pygame.transform.scale(tools.load_image("task_one.png"),
                                   const.SCREEN_SIZE), (0, 0))
        self.sprites.draw(self.screen)
        pygame.display.flip()
