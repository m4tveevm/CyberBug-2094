import pygame

from data import constants as const
from data.components import tools
from data.states.game_screen import Game_Screen


class LevelState(Game_Screen):
    def __init__(self):
        super().__init__()
        self.sprites = pygame.sprite.AbstractGroup()
        self.quit, self.next = False, False
        self.time = pygame.time.get_ticks()

        # hidden params of colors
        self.color_red = False
        self.end_time = False
        self.color_yellow = False
        self.color_purple = False
        self.list_of_sprites = []
        self.start()

    def status(self):
        super().status()

    def start(self):
        self.init_layers()
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

    def layer_settings(self, sprite, img, sprites_list, x_y=(0, 0)):
        sprite.image = tools.load_image(img)
        sprite.w, sprite.h = const.SCREEN_SIZE
        sprite.x, sprite.y = x_y
        sprite.rect = ((sprite.x, sprite.y),
                       (sprite.w, sprite.h))
        sprite.add(sprites_list)

    def init_layers(self):
        self.game_btn_red()
        self.game_btn_yellow()
        self.game_btn_purple()

    def game_btn_red(self):
        self.red_sprite_group = pygame.sprite.AbstractGroup()
        color_red_sprite = pygame.sprite.Sprite()
        self.layer_settings(color_red_sprite, "task_one_1.png", sprites_list=self.red_sprite_group)

    def game_btn_yellow(self):
        color_yellow_sprite = pygame.sprite.Sprite()
        self.yellow_sprite_group = pygame.sprite.AbstractGroup()
        self.layer_settings(color_yellow_sprite, "task_one_2.png", sprites_list=self.yellow_sprite_group)

    def game_btn_purple(self):
        color_purple_sprite = pygame.sprite.Sprite()
        self.purple_sprite_group = pygame.sprite.AbstractGroup()
        self.layer_settings(color_purple_sprite, "task_one_3.png", sprites_list=self.purple_sprite_group)

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
                self.color_purple = True

    def result(self):
        font = pygame.font.Font(None, 50)
        text = font.render(
            f"Поздравляем вы прошли за {self.end_time}сек! Рекорд: {tools.best_time()}", True, 'red')
        text_x = const.SCREEN_CENTER - text.get_width() // 2
        text_y = const.SCREEN_SIZE[1] * 0.1 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y))
        pygame.draw.rect(self.screen, (255, 0, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20),
                         5)

    def update(self):
        super().update()
        self.screen.blit(
            pygame.transform.scale(tools.load_image("task_one.png"), const.SCREEN_SIZE), (0, 0))
        if self.color_red:
            self.red_sprite_group.draw(self.screen)
        if self.color_yellow:
            self.yellow_sprite_group.draw(self.screen)
        if self.color_purple:
            self.purple_sprite_group.draw(self.screen)
        if self.color_purple and self.color_red and self.color_yellow:
            if not self.end_time:
                self.end_time = (self.time - pygame.time.get_ticks()) / 1000 * (-1)
                tools.add_time_db(self.end_time)
            self.result()

        self.sprites.draw(self.screen)
        pygame.display.flip()
