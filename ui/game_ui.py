import pygame as pygame
from main import *


class GameUI:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))
        self._main = Game()

    def get_screen(self):
        return self._screen

    def board(self):
        pygame.display.set_caption('Yinch')
        board_img = pygame.image.load('images/game/plateau_yinch.png').convert_alpha()
        board = pygame.transform.scale(board_img, (int(self._screen_width * 0.5), int(self._screen_height * 0.9)))

        return board

    def window(self):
        run = True
        while run:
            self._screen.fill((255, 255, 255))


            self.get_screen().blit(self.board(), (0, 0))
            self.afficher_plateau()

            # get mouse position
            pos = pygame.mouse.get_pos()
            #click = pygame.mouse.get_pressed()

            #print(pos, click)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

    def afficher_plateau(self):
        pawn_ring_1 = pygame.image.load('images/game/pawn_and_ring_1.png').convert_alpha()
        pawn_ring_2 = pygame.image.load('images/game/pawn_and_ring_2.png').convert_alpha()
        pawn_1 = pygame.image.load('images/game/pawn_player_1.png').convert_alpha()
        pawn_2 = pygame.image.load('images/game/pawn_player_2.png').convert_alpha()
        ring_1 = pygame.image.load('images/game/ring_player_1.png').convert_alpha()
        ring_2 = pygame.image.load('images/game/ring_player_2.png').convert_alpha()
        sizex, sizey = 80, 80
        pawn_ring_1 = pygame.transform.scale(pawn_ring_1, (sizex, sizey))
        pawn_ring_2 = pygame.transform.scale(pawn_ring_2, (sizex, sizey))
        ring_1 = pygame.transform.scale(ring_1, (sizex, sizey))
        ring_2 = pygame.transform.scale(ring_2, (sizex, sizey))

        sizex, sizey = 90, 90
        pawn_1 = pygame.transform.scale(pawn_1, (sizex, sizey))
        pawn_2 = pygame.transform.scale(pawn_2, (sizex, sizey))

        for i in range(len(self._main.get_board()[0])):
            for j in range(len(self._main.get_board())):
                pygame.draw.rect(self._screen, (255, 0, 0), (27 + j * 54, 15 + i * 33, 54, 33), 2)
        for i in range(len(self._main.get_board()[0])):
            for j in range(len(self._main.get_board())):
                if self._main.get_board()[j][i] == 2:
                    self._screen.blit(ring_1, (10 + j * 54, i * 33))
                elif self._main.get_board()[j][i] == 3:
                    self._screen.blit(ring_2, (10 + j * 54, i * 33))
                elif self._main.get_board()[j][i] == 4:
                    self._screen.blit(pawn_1, (10 + j * 54, i * 33))
                elif self._main.get_board()[j][i] == 5:
                    self._screen.blit(pawn_2, (j * 54, (-5) + i * 33))
                elif self._main.get_board()[j][i] == 6:
                    self._screen.blit(pawn_ring_1, (10 + j * 54, i * 33))
                elif self._main.get_board()[j][i] == 7:
                    self._screen.blit(pawn_ring_2, (10 + j * 54, i * 33))



game_ui = GameUI()
#game_ui.get_screen()
#game_ui.window()
