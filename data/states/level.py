import pygame

from data import constants as const
from data.components import tools
from data.states.game_screen import Game_screen


class LevelState(Game_screen):
    def __init__(self):
        super().__init__()
