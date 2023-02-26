import pygame


class Pygame_screen():
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('CyberBug 2084')
        self.start()

    def draw(self):
        pass

    def start(self):
        pygame.init()
        self.draw()
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()


if __name__ == '__main__':
    x, y = 1280, 720
    Pygame_screen(int(x), int(y))