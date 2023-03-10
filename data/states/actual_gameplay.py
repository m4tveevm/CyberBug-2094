import pygame, random

from data import constants as const
from data.components import tools
from data.states.game_screen import Game_Screen


class Bug_screen(Game_Screen):
    def __init__(self):
        super().__init__()
        tools.load_music(random.choice(["error_music.mp3", "bug.mp3"])).play()
        self.start_ticks = pygame.time.get_ticks()
        self.quit = False
        self.buging()

    def buging(self):
        self.animate()
        while True:
            for event in pygame.event.get():
                self.get_event(event)
            pygame.display.flip()
            if (pygame.time.get_ticks() - self.start_ticks) > 5000:
                const.CURENT_STATE = False
                break

    def animate(self):
        self.screen.blit(pygame.transform.scale(tools.load_image("error_screen.png"),
                                                const.SCREEN_SIZE), (0, 0))
        pygame.display.flip()

    def update(self):
        super().update()
