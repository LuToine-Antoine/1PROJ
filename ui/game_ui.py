import pygame as pygame
from pygame.transform import scale


class GameUI:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

    def get_screen(self):
        return self._screen

    def board(self):
        pygame.display.set_caption('Yinch')
        board_img = pygame.image.load('../images/game/plateau_yinch.png').convert_alpha()
        board = pygame.transform.scale(board_img, (int(self._screen_width * 0.6), int(self._screen_height * 1)))
        return board

    def window(self):
        run = True
        while run:

            self.get_screen().blit(self.board(), (0, 0))

            # get mouse position
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            print(click)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()


game_ui = GameUI()
game_ui.get_screen()
game_ui.window()
