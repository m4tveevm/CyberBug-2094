import os
import pygame

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('resources', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_music(name):
    fullname = os.path.join('resources/', name)
    if not os.path.isfile(fullname):
        print(f"Файл с медиа '{fullname}' не найден")
    else:
        return pygame.mixer.Sound(fullname)
