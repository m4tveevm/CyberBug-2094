import os

from data import constants as const
# from data import setup
from data.states import main_menu


def main():
    main_menu.MainMenuState(0).main()
