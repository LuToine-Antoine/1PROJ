import sys
import pygame as pygame

from main import *
from ui.game_ui import *
from ui.buttons import *


class MenuUi:
    def __init__(self, width=1280, height=720):
        """
        Initialize the MenuUi class
        """
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        self._bg = pygame.image.load('images/menu/bg.jpg').convert_alpha()

        self._leave_img = pygame.image.load('images/leave.png').convert_alpha()
        self._leave_btn = ButtonUi(1200, 0, self._leave_img, 0.03)

        self._back_img = pygame.image.load('images/back.png').convert_alpha()
        self._back_btn = ButtonUi(510, 420, self._back_img, 0.32)

        super(GameUI)
        self._board_ui = GameUI()

    def music_menu(self):
        """
        Play the menu music.
        :return:
        """
        pygame.mixer.init()
        pygame.mixer.music.load('musics/menu_music.ogg', "ogg")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(loops=-1, start=0.0)

    def window(self):
        """
        Display the main menu of the game.
        :return:
        """

        pygame.display.set_caption('Yinch menu - LuToine')

        # Create the logo image and modify his size
        logo_img = pygame.image.load('images/menu/logo_yinch.png').convert_alpha()
        logo = pygame.transform.scale(logo_img, (int(self._screen_width * 0.15), int(self._screen_height * 0.265)))

        # Load pictures from file
        solo_img = pygame.image.load('images/menu/button_solo.png').convert_alpha()
        multiplayer_img = pygame.image.load('images/menu/button_multiplayer.png').convert_alpha()
        rules_img = pygame.image.load('images/menu/button_rules.png').convert_alpha()

        # Create button instances
        solo_button = ButtonUi(510, 205, solo_img, 0.32)
        multiplayer_button = ButtonUi(510, 335, multiplayer_img, 0.32)
        rules_button = ButtonUi(510, 500, rules_img, 0.32)

        while True:

            self._screen.blit(self._bg, (0, 0))

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if solo_button.draw():
                self.display_solo()

            if multiplayer_button.draw():
                self.display_multi()

            if rules_button.draw():
                self.display_rules()

            self._screen.blit(logo, (540, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()

    def display_solo(self):
        """
        Display the solo menu.
        :return:
        """
        self._board_ui.get_game().set_game_mode(0)
        pygame.display.set_caption('Yinch Solo mode')

        normal_img = pygame.image.load('images/menu/button_classic.png').convert_alpha()
        blitz_img = pygame.image.load('images/menu/button_blitz.png').convert_alpha()

        normal_btn = ButtonUi(510, 100, normal_img, 0.32)
        blitz_btn = ButtonUi(510, 300, blitz_img, 0.32)

        while True:

            self._screen.blit(self._bg, (0, 0))

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if self._back_btn.draw():
                self.window()

            if normal_btn.draw():
                self._board_ui.get_game().set_blitz_mode(1)
                pygame.mixer.music.pause()
                self._board_ui.window()

            if blitz_btn.draw():
                self._board_ui.get_game().set_blitz_mode(0)
                pygame.mixer.music.pause()
                self._board_ui.window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()

    def display_multi(self):
        """
        Display the multiplayer menu.
        :return:
        """

        pygame.display.set_caption('Yinch Multiplayer mode')

        local_img = pygame.image.load('images/menu/multi_menu/button_local.png').convert_alpha()
        local_button = ButtonUi(510, 100, local_img, 0.32)

        while True:

            self._screen.blit(self._bg, (0, 0))

            if local_button.draw():
                self.display_local()

            if self._back_btn.draw():
                self.window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()

    def display_local(self):
        """
        Display the local menu.
        """
        self._board_ui.get_game().set_game_mode(1)

        pygame.display.set_caption('Yinch Local Mode')

        normal_img = pygame.image.load('images/menu/button_classic.png').convert_alpha()
        blitz_img = pygame.image.load('images/menu/button_blitz.png').convert_alpha()

        normal_btn = ButtonUi(510, 190, normal_img, 0.32)
        blitz_btn = ButtonUi(510, 290, blitz_img, 0.32)

        while True:

            self._screen.blit(self._bg, (0, 0))

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if self._back_btn.draw():
                self.window()

            if normal_btn.draw():
                self._board_ui.get_game().set_blitz_mode(1)
                pygame.mixer.music.pause()
                self._board_ui.window()

            if blitz_btn.draw():
                self._board_ui.get_game().set_blitz_mode(0)
                pygame.mixer.music.pause()
                self._board_ui.window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()

    def display_rules(self):
        """
        Display the game rules.
        """
        black = (0, 0, 0)
        sakura = (214, 173, 166)
        scale = 0.2

        pygame.display.set_caption('Yinch Rules')

        pygame.font.init()
        font_title = pygame.font.SysFont('freesansbold.ttf', 50)
        font_text = pygame.font.Font('freesansbold.ttf', 20)

        # Text bloc
        title = font_title.render('Yinsh - Règles', True, black)
        text_0 = font_text.render("Le but du jeu est d'aligner 5 pions afin de retirer 3 anneaux (en mode normal) ou 1 anneau (en mode blitz, rapide).", True, black)
        text_1 = font_text.render("En début de partie, chaque joueur pose ses 5 anneaux sur le plateau à tour de rôle. Les pions se placent ensuite", True, black)
        text_2 = font_text.render("dans 1 anneaux et cet anneau se déplace sur les lignes à partir de sa position initiale.", True, black)

        # Bloc ring 1
        img_ring_1 = pygame.image.load('images/game/ring_player_1.png').convert_alpha()
        img_ring_1 = pygame.transform.scale(img_ring_1,
                                            (int(self._screen_width * scale), int((self._screen_height + 500) * scale)))
        text_ring_1 = font_text.render("Anneau joueur 1", True, black)

        # Bloc ring 2
        img_ring_2 = pygame.image.load('images/game/ring_player_2.png').convert_alpha()
        img_ring_2 = pygame.transform.scale(img_ring_2,
                                            (int(self._screen_width * scale), int((self._screen_height + 500) * scale)))
        text_ring_2 = font_text.render("Anneau joueur 2", True, black)

        # Bloc pawn 1
        img_pawn_1 = pygame.image.load('images/game/pawn_player_1.png').convert_alpha()
        img_pawn_1 = pygame.transform.scale(img_pawn_1,
                                            (int(self._screen_width * scale), int((self._screen_height + 350) * scale)))
        text_pawn_1 = font_text.render("Pion joueur 1", True, black)

        # Bloc pawn 2
        img_pawn_2 = pygame.image.load('images/game/pawn_player_2.png').convert_alpha()
        img_pawn_2 = pygame.transform.scale(img_pawn_2,
                                            (int(self._screen_width * scale), int((self._screen_height + 350) * scale)))
        text_pawn_2 = font_text.render("Pion joueur 1", True, black)

        # Placement du titre
        title_rect = title.get_rect()
        title_rect.center = (self._screen_width // 2, 35)

        # Buttons
        back_button_rules = ButtonUi(500, 420, self._back_img, 0.32)

        # infinite loop
        while True:

            self._screen.fill(sakura)

            if back_button_rules.draw():
                self.window()

            if self._leave_btn.draw():
                sys.exit("Game leave")

            self._screen.blit(title, title_rect)
            self._screen.blit(text_0, (100, 100))
            self._screen.blit(text_1, (100, 130))
            self._screen.blit(text_2, (100, 160))

            self._screen.blit(img_ring_1, (200, 170))
            self._screen.blit(text_ring_1, (250, 370))
            self._screen.blit(img_ring_2, (400, 170))
            self._screen.blit(text_ring_2, (450, 370))

            self._screen.blit(img_pawn_1, (700, 170))
            self._screen.blit(text_pawn_1, (780, 370))
            self._screen.blit(img_pawn_2, (900, 170))
            self._screen.blit(text_pawn_2, (970, 370))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()


menu = MenuUi()
menu.music_menu()
menu.window()
