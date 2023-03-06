import pygame


class Pygame_screen():
    def __init__(self, width, height):
        self.width, self.height = 1080, 720
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        self.running = True
        pygame.display.set_caption('CyberBug 2084')
        self.start()

    def event_loop(self):
        """
        Special loop, that is checking if program is still alive.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start(self):
        pygame.init()
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()


if __name__ == '__main__':
    x, y = 1280, 720
    Pygame_screen()
