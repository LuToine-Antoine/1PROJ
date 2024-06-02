import sys
import pygame as pygame

from main import *
from ui.buttons import *


class GameUI:
    def __init__(self, width=1280, height=720):
        """
        Initialize the game UI.
        :param width:
        :param height:
        """

        # Initialize the window.
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        self._main = Game()
        self._possibles = RingsMoves(0, 0, self._main.get_board())

        # Initialize images that will be often use.
        self._leave_img = pygame.image.load('images/leave.png').convert_alpha()
        self.show_possible_moves = []
        self._back_img = pygame.image.load('images/back.png').convert_alpha()
        self._back_btn = ButtonUi(570, 300, self._back_img, 0.32)
        self._back_btn_game = ButtonUi(775, 500, self._back_img, 0.32)
        self._leave_btn = ButtonUi(1200, 0, self._leave_img, 0.03)
        self._blue_taiko = pygame.image.load('images/game/ring_player_1.png').convert_alpha()
        self._blue_taiko = pygame.transform.scale(
            self._blue_taiko, (int(self._screen_width * 0.09), int(self._screen_height * 0.16)))
        self._red_taiko = pygame.image.load('images/game/ring_player_2.png').convert_alpha()
        self._red_taiko = pygame.transform.scale(
            self._red_taiko, (int(self._screen_width * 0.09), int(self._screen_height * 0.16)))
        self._taiko_under = pygame.image.load('images/game/menu/taiko_under.png').convert_alpha()
        self._taiko_under = pygame.transform.scale(
            self._taiko_under, (int(self._screen_width * 0.09), int(self._screen_height * 0.16)))

    def get_screen(self):
        """
        Returns the screen.
        :return: screen
        """
        return self._screen

    def get_game(self):
        """
        Returns the game class.
        :return: Game()
        """
        return self._main

    def board_ui(self):
        """
        Initialize the board images.
        :return: board img
        """
        pygame.display.set_caption('Yinch')
        board_img = pygame.image.load('images/game/plateau_yinch.png').convert_alpha()
        board = pygame.transform.scale(board_img, (int(self._screen_width * 0.5), int(self._screen_height * 0.9)))

        return board

    def window(self):
        """
        Display the main window.
        """
        # Create colors var
        black = (0, 0, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)

        # Build the screen and display the board
        self._screen.fill((255, 255, 255))
        self._screen.blit(self.board_ui(), (-20, -10))
        self.display_board()

        # Initialize fonts
        pygame.font.init()
        font_title = pygame.font.SysFont('freesansbold.ttf', 50)
        font_action = pygame.font.SysFont('freesansbold.ttf', 30)

        selected_player_img = pygame.image.load('images/game/menu/sakura_logo.png').convert_alpha()
        selected_player = pygame.transform.scale(
            selected_player_img, (int(self._screen_width * 0.04), int(self._screen_height * 0.06)))

        text_tips = font_action.render(
            'Astuce : Cliquez droit sur votre anneau pour voir vos déplacements possibles.', True, black)
        text_player_1 = font_title.render('Joueur 1', True, blue)
        text_player_2 = font_title.render('Joueur 2', True, red)

        # Display loop.
        run = True
        while run:

            text_ring_number_1 = font_title.render(f'Anneau(x) retiré(s) {self._main.get_player_1_ring()}', True, blue)
            text_ring_number_2 = font_title.render(f'Anneau(x) retiré(s)  {self._main.get_player_2_ring()}', True, red)

            text_pawn_reaming = font_action.render(
                f'Pions restants {self._main.get_pawn().get_pawn_stock()}', True, black)
            self.get_screen().blit(text_pawn_reaming, (840, 100))

            if self._main.get_blitz_mode() == 1:
                self.get_screen().blit(self._taiko_under, (840, 240))
                self.get_screen().blit(self._taiko_under, (840, 540))

            if self._main.get_blitz_mode() == 0:
                # Player 1 rings remains
                self.get_screen().blit(self._taiko_under, (750, 240))
                self.get_screen().blit(self._taiko_under, (855, 240))
                self.get_screen().blit(self._taiko_under, (960, 240))
                match self._main.get_player_1_ring():
                    case 1:
                        self.get_screen().blit(self._blue_taiko, (750, 240))
                    case 2:
                        self.get_screen().blit(self._blue_taiko, (750, 240))
                        self.get_screen().blit(self._blue_taiko, (855, 240))
                    case 3:
                        self.get_screen().blit(self._blue_taiko, (750, 240))
                        self.get_screen().blit(self._blue_taiko, (855, 240))
                        self.get_screen().blit(self._blue_taiko, (960, 240))

                # Player 2 rings remain
                self.get_screen().blit(self._taiko_under, (750, 440))
                self.get_screen().blit(self._taiko_under, (855, 440))
                self.get_screen().blit(self._taiko_under, (960, 440))
                match self._main.get_player_2_ring():
                    case 1:
                        self.get_screen().blit(self._red_taiko, (750, 440))
                    case 2:
                        self.get_screen().blit(self._red_taiko, (750, 440))
                        self.get_screen().blit(self._red_taiko, (855, 440))
                    case 3:
                        self.get_screen().blit(self._red_taiko, (750, 440))
                        self.get_screen().blit(self._red_taiko, (855, 440))
                        self.get_screen().blit(self._red_taiko, (960, 440))

            pos = pygame.mouse.get_pos()

            if self._main.win():
                self.win_menu()

            if self._leave_btn.draw():
                sys.exit("Game leave")
            pygame.display.update()

            self.get_screen().blit(text_player_1, (840, 150))
            self.get_screen().blit(text_player_2, (840, 350))

            self.get_screen().blit(text_ring_number_1, (760, 200))
            self.get_screen().blit(text_ring_number_2, (760, 400))

            # Get mouse position
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self._main.get_game_mode() == 0:
                        if self._main.get_player() == 1:
                            click_coords = ((pos[0] // (532 // len(self._main.get_board())) * 0.540),
                                            (pos[1] // (558 // len(self._main.get_board()) * 1.15)))
                        else:
                            click_coords = self._main.ia_moves()
                    if self._main.get_game_mode() == 1:
                        click_coords = ((pos[0] // (532 // len(self._main.get_board())) * 0.540),
                                        (pos[1] // (558 // len(self._main.get_board()) * 1.15)))
                    self._main.game_loop(int(click_coords[1]), int(click_coords[0]))
                    self._screen.fill((255, 255, 255))
                    self.get_screen().blit(self.board_ui(), (-20, -10))
                    self.display_board()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    see_moves = ((pos[0] // (532 // len(self._main.get_board())) * 0.540),
                                 (pos[1] // (558 // len(self._main.get_board()) * 1.15)))
                    if self._main.get_board()[int(see_moves[1])][int(see_moves[0])] in (2, 3, 6, 7):
                        self._screen.fill((255, 255, 255))
                        self.get_screen().blit(self.board_ui(), (-20, -10))
                        self.view_possible_moves(int(see_moves[1]), int(see_moves[0]))
                        self.display_board()

            text_turn = font_title.render(f'Tour {self._main.get_turn()}', True, black)
            self.get_screen().blit(text_turn, (860, 30))

            texts = {
                (0, 1): font_action.render('Placez vos premiers anneaux', True, blue),
                (1, 1): font_action.render("Déplacez l'anneau", True, blue),
                (2, 1): font_action.render('Placez un pion dans un anneau', True, blue),
                (0, 2): font_action.render('Placez vos premiers anneaux', True, red),
                (1, 2): font_action.render("Déplacez l'anneau", True, red),
                (2, 2): font_action.render('Placez un pion dans un anneau', True, red),
            }

            click_count = self._main.get_click_count()
            player = self._main.get_player()

            if self._main.get_turn() < 10:
                if click_count == 0:
                    action_key = (0, player)
                else:
                    action_key = (1, player)
            else:
                if click_count == 0:
                    action_key = (2, player)
                else:
                    action_key = (1, player)

            text = texts[action_key]
            self.get_screen().blit(text, (760, 70))

            self.get_screen().blit(text_tips, (450, 650))

            if self._main.get_player() == 1:
                self.get_screen().blit(selected_player, (780, 145))
            if self._main.get_player() == 2:
                self.get_screen().blit(selected_player, (780, 345))

    def display_board(self):
        """
        Display the board.
        """
        # Initialize the pictures that will be used
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
                board_ui = self._main.get_board()[j][i]
                match board_ui:
                    case 2:
                        self._screen.blit(ring_1, ((-15) + i * 54, (-15) + j * 33))
                    case 3:
                        self._screen.blit(ring_2, ((-15) + i * 54, (-15) + j * 33))
                    case 4:
                        self._screen.blit(pawn_1, ((-15) + i * 54, (-15) + j * 33))
                    case 5:
                        self._screen.blit(pawn_2, ((-20) + i * 54, (-15) + j * 33))
                    case 6:
                        self._screen.blit(pawn_ring_1, ((-15) + i * 54, (-15) + j * 33))
                    case 7:
                        self._screen.blit(pawn_ring_2, ((-15) + i * 54, (-15) + j * 33))

    def view_possible_moves(self, x, y):
        """
        Display the possible cases where you could place your ring.
        :param x:
        :param y:
        :return:
        """
        self.show_possible_moves.clear()
        possible = pygame.image.load('images/game/case_possible.png').convert_alpha()
        possible = pygame.transform.scale(possible, (70, 70))
        self.show_possible_moves = list(self._possibles.get_possible_moves(x, y))

        for i in range(len(self._main.get_board()[0])):
            for j in range(len(self._main.get_board())):
                for x in range(len(self.show_possible_moves)):
                    if (j, i) in self.show_possible_moves[x]:
                        self._screen.blit(possible, ((-10) + i * 54, (-10) + j * 33))

    def win_menu(self):
        """
        Display the win menu.
        """
        black = (0, 0, 0)
        sakura = (214, 173, 166)

        pygame.font.init()
        font_title = pygame.font.SysFont('freesansbold.ttf', 50)

        if self._main.get_player() == 1:
            winner = 2
        else:
            winner = 1

        if self._main.win() == 3:
            pygame.display.set_caption(f'Yinch - Egalité ! !')
            text_winner = font_title.render(f'Bien joué égalité !', True, black)
        else:
            pygame.display.set_caption(f'Yinch - {winner} Win !')
            text_winner = font_title.render(f'Bien joué Joueur {winner}', True, black)

        cat_img = pygame.image.load('images/cat_win.png').convert_alpha()
        cat_img = pygame.transform.scale(cat_img, (int(self._screen_width * 0.3), int(self._screen_height * 0.5)))

        restart_img = pygame.image.load('images/button_restart.png').convert_alpha()
        restart_btn = ButtonUi(510, 540, restart_img, 0.32)

        self.win_music()

        while True:

            self._screen.fill(sakura)

            self._screen.blit(text_winner, (470, 70))
            self._screen.blit(cat_img, (440, 150))

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if restart_btn.draw():
                self.restart()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()

    def win_music(self):
        """
        Plays the win music
        """
        pygame.mixer.init()
        pygame.mixer.music.load('musics/win_sound.ogg', "ogg")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(loops=-1, start=0.0)

    def restart(self):
        """
        Restarts the game.
        """
        pygame.mixer.music.set_volume(0)
        self._main.reset_board()
        self._main.reset_player_rings()
        self._main.reset_turn()
        self._main.get_pawn().reset_pawn()
        self.window()
