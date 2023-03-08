import pygame

from data import constants as const
from data.components import tools


class Game_screen():
    def __init__(self):
        self.current_time = 0.0
        self.display = pygame.display.get_surface()
        # self.caption = caption
        self.keys = pygame.key.get_pressed()
        self.states = None
        self.state = None
        self.running = False
        self.clock = pygame.time.Clock()
        self.fps = 60

    def setup_states(self, states, default_state):
        """
        Setup states for the game
        :param states: (dictionary): Dictionary of states
        :param default_state: (state): Base state
        """
        self.states = states
        self.state = states[default_state](self.current_time, None)

    def flip_state(self):
        props = self.state.cleanup()
        self.state = self.states[self.state.next](self.current_time, props)

    def update(self):
        """
        Updates the current state
        """

        self.current_time = pygame.time.get_ticks()
        if self.state.quit:
            self.running = False
        elif self.state.done:
            self.flip_state()
        self.state.update(self.display, self.current_time)

    def event_loop(self):
        """
        Event processing loop
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.state.get_event(event)

    def main(self):
        """
        Main loop of the game
        """
        self.running = True
        while self.running:
            self.event_loop()
            self.update()
            pygame.display.update()
            self.clock.tick(self.fps)

    def screen_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(const.SCREEN_SIZE)
        pygame.display.set_icon(tools.load_image(const.GAME_ICON_LOCATION))
        pygame.display.set_caption('CyberBug 2084™')
