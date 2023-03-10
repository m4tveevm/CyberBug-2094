import os
from datetime import date

import pygame

import requests
from bs4 import BeautifulSoup

import sqlite3

pygame.init()


def get_version():
    try:
        url = f'https://updating.space/pg_stats.html/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
            'Accept-Language': 'en-US,en;q=0.9'}
        response = requests.get(url, headers=headers)
        bs = BeautifulSoup(response.text, "html.parser")
    except:
        return 'Версия : Network Error'
    try:
        version = bs.find("p", {"class": "version"}).get_text(strip=True)
        print(version)
    except:
        return f'Версия : server error'
    return f'Версия {version} актуальна'


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


def best_time():
    con = sqlite3.connect('data/results.sqlite')
    cur = con.cursor()

    result = cur.execute(f'''
    SELECT time, date
    FROM all_results
    order by time''').fetchall()
    return f"{result[0][0]}cек ({result[0][1]})"


def add_time_db(time):
    today = date.today()
    con = sqlite3.connect('data/results.sqlite')
    cur = con.cursor()

    cur.execute(f'''
    INSERT INTO all_results (
                            time,
                            date
                        )
                        VALUES (
                            '{time}',
                            '{today}'
                        );
    ''').fetchall()
    con.commit()
