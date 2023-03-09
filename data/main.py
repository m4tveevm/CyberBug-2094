import os

from data import constants as const
# from data import setup
from data.states import main_menu


def main():
    # states = {
    #     const.MAIN_MENU: main_menu.MainMenuState,
    #     const.LEVEL: level.LevelState,
    #     const.GAME_OVER: game_over.GameOverState
    # }
    main_menu.MainMenuState(0)

    # while True:
    #     for event in main_menu.pygame.event.get():
    #         if event:
    #             print(event)
    #             main_menu.MainMenuState.get_event(event)
    #             if main_menu.MainMenuState.get_event(event).quit:
    #                 os.close(0)
    #                 break