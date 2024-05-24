import pygame as pygame

class GameUI:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        pygame.display.set_caption('Yinch')
        self._bg = pygame.image.load('../images/game/plateau_yinch.png').convert_alpha()

    def get_screen(self):
        return self._screen

game_ui = GameUI()

game_ui.get_screen()