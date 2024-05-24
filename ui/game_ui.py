import pygame as pygame
from pygame.transform import scale


class GameUI:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        pygame.display.set_caption('Yinch')
        self._bg = pygame.image.load('../images/game/plateau_yinch.png').convert_alpha()
        self._image = pygame.transform.scale(image, (int(self._width * scale), int(self._height * scale)))

    def get_screen(self):
        return self._screen

    def window(self):
        run = True
        while run:

            self.get_screen().blit(self._bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

game_ui = GameUI()

game_ui.get_screen()
game_ui.window()