import sys
import pygame as pygame

from main import *
from ui.buttons import *


class GameUI:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))
        self._main = Game()
        self._leave_img = pygame.image.load('images/leave.png').convert_alpha()

    def get_screen(self):
        return self._screen

    def board(self):
        pygame.display.set_caption('Yinch')
        board_img = pygame.image.load('images/game/plateau_yinch.png').convert_alpha()
        board = pygame.transform.scale(board_img, (int(self._screen_width * 0.5), int(self._screen_height * 0.9)))

        return board

    def window(self):
        leave_btn = Button(1200, 0, self._leave_img, 0.03)

        self._screen.fill((255, 255, 255))
        self._screen.blit(self.board(), (-20, -10))
        self.afficher_plateau()

        run = True
        while run:
            pos = pygame.mouse.get_pos()


            # get mouse position
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    isintable = ((pos[0] // (530 // len(self._main.get_board())) * 0.525),
                                 (pos[1] // (558 // len(self._main.get_board()) * 1.12)))
                    self._main.game_loop(int(isintable[1]), int(isintable[0]))
                    self._screen.fill((255, 255, 255))
                    self.get_screen().blit(self.board(), (-20, -10))
                    print(int(isintable[1]), int(isintable[0]))
                    self.afficher_plateau()

            if leave_btn.draw():
                sys.exit("Game leave")
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

        for j in range(len(self._main.get_board())):
            for i in range(len(self._main.get_board()[0])):
                if self._main.get_board()[j][i] == 1:
                    pygame.draw.rect(self._screen, (0, 0, 0), (i * 54, j * 33, 54, 33), 0)
                else :
                    pygame.draw.rect(self._screen, (255, 0, 0), (i * 54, j * 33, 54, 33), 1)


        for i in range(len(self._main.get_board()[0])):
            for j in range(len(self._main.get_board())):
                board_ui = self._main.get_board()[j][i]
                match board_ui:
                    case 2:
                        self._screen.blit(ring_1, ((-15) + i * 54, (-15) + j * 33))
                    case 3:
                        self._screen.blit(ring_2, ((-15) + i * 54, (-15) + j * 33))
                    case 4:
                        self._screen.blit(pawn_1, ((-15) + i * 54,(-15) + j * 33))
                    case 5:
                        self._screen.blit(pawn_2, ((-20) + i * 54, (-15) + j * 33))
                    case 6:
                        self._screen.blit(pawn_ring_1, ((-15) +i * 54,(-15) + j * 33))
                    case 7:
                        self._screen.blit(pawn_ring_2, ((-15) +i * 54,(-15) + j * 33))


game_ui = GameUI()
#game_ui.get_screen()
#game_ui.window()
