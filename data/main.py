from data import constants as const
from data.states import main_menu, level, actual_gameplay

states = {
    const.MAIN_MENU: main_menu.MainMenuState,
    const.LEVEL: level.LevelState,
    const.BUG: actual_gameplay.Bug_screen
}


def main():
    while const.CURENT_STATE:
        states.get(const.CURENT_STATE)()
