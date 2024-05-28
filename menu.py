import sys
import pygame as pygame

from main import *
from ui.game_ui import *
from ui.buttons import *


class Menu:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        pygame.display.set_caption('Yinch')
        self._bg = pygame.image.load('images/menu/bg.jpg').convert_alpha()

        self._leave_img = pygame.image.load('images/leave.png').convert_alpha()
        self._leave_btn = Button(1200, 0, self._leave_img, 0.03)

        self._back_img = pygame.image.load('images/back.png').convert_alpha()
        self._back_btn = Button(500, 700, self._back_img, 1)

        self._main = Game()
        self._board_ui = GameUI()

    def get_screen(self):
        return self._screen

    def music_menu(self):
        pygame.mixer.init()
        pygame.mixer.music.load('musics/menu_music.ogg', "ogg")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(loops=-1, start=0.0)

    def window(self):

        solo_img = pygame.image.load('images/menu/button_solo.png').convert_alpha()
        local_img = pygame.image.load('images/menu/button_local.png').convert_alpha()
        rules_img = pygame.image.load('images/menu/button_rules.png').convert_alpha()
        setting_img = pygame.image.load('images/menu/button_settings.png').convert_alpha()

        solo_button = Button(288, -10, solo_img, 0.32)
        local_button = Button(288, 110, local_img, 0.32)
        rules_button = Button(288, 240, rules_img, 0.32)
        setting_button = Button(288, 360, setting_img, 0.32)

        logo_img = pygame.image.load('images/menu/logo_yinch.png').convert_alpha()
        logo_button = Button(550, 0, logo_img, 0.1)

        run = True
        while run:

            self.get_screen().blit(self._bg, (0, 0))

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if solo_button.draw():
                self.display_solo()
            local_button.draw()
            if rules_button.draw():
                self.display_rules()
            setting_button.draw()
            logo_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

    def display_solo(self):
        self._main.set_game_mode(0)
        pygame.display.set_caption('Yinch Solo mode')

        normal_img = pygame.image.load('images/menu/button_classic.png').convert_alpha()
        blitz_img = pygame.image.load('images/menu/button_blitz.png').convert_alpha()

        normal_btn = Button(288, -10, normal_img, 0.32)
        blitz_btn = Button(288, 110, blitz_img, 0.32)

        while True:

            self.get_screen().blit(self._bg, (0, 0))

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if self._back_btn.draw():
                Menu()

            if normal_btn.draw():
                self._main.set_game_mode(0)
                pygame.mixer.music.pause()
                self._board_ui.window()
            if blitz_btn.draw():
                self._main.set_game_mode(1)
                pygame.mixer.music.pause()
                self._board_ui.window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()

    def display_local(self):
        self._main.set_game_mode(1)

        pygame.display.set_caption('Yinch Local Mode')

        normal_img = pygame.image.load('images/menu/button_classic.png').convert_alpha()
        blitz_img = pygame.image.load('images/menu/button_blitz.png').convert_alpha()

        normal_btn = Button(288, -10, normal_img, 0.32)
        blitz_btn = Button(288, 110, blitz_img, 0.32)

        while True:

            self.get_screen().blit(self._bg, (0, 0))

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if self._back_btn.draw():
                Menu()

            if normal_btn.draw():
                self._main.set_game_mode(0)
                pygame.mixer.music.pause()
                self._board_ui.window()
            if blitz_btn.draw():
                self._main.set_game_mode(1)
                pygame.mixer.music.pause()
                self._board_ui.window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()

    def display_rules(self):
        black = (0, 0, 0)
        sakura = (214, 173, 166)

        display_surface = pygame.display.set_mode((self._screen_width, self._screen_height))
        scale = 0.2

        pygame.display.set_caption('Yinch Rules')

        pygame.font.init()
        font_title = pygame.font.SysFont('freesansbold.ttf', 50)
        font_text = pygame.font.Font('freesansbold.ttf', 20)

        title = font_title.render(
            'Yinsh - Règles', True, black)
        text_0 = font_text.render("Le but du jeu est d'aligner 5 pions afin de retirer 3 anneaux (en mode normal) ou 1 anneau (en mode blitz, rapide).", True, black)
        text_1 = font_text.render("En début de partie, chaques joueurs pose ses 5 anneaux sur le plateau a tour de rôle. Les pions se placent ensuite", True, black)
        text_2 = font_text.render("dans 1 anneaux et cet anneau se déplace sur les lignes à partir de sa position initiale.", True, black)

        img_ring_1 = pygame.image.load('images/game/ring_player_1.png').convert_alpha()
        img_ring_2 = pygame.image.load('images/game/ring_player_2.png').convert_alpha()

        img_ring_1 = pygame.transform.scale(img_ring_1,
                                            (int(self._screen_width * scale), int((self._screen_height + 500) * scale)))

        text_ring_1 = font_text.render("Anneau joueur 1", True, black)

        img_ring_2 = pygame.transform.scale(img_ring_2,
                                            (int(self._screen_width * scale), int((self._screen_height + 500) * scale)))

        text_ring_2 = font_text.render("Anneau joueur 2", True, black)

        img_pawn_1 = pygame.image.load('images/game/pawn_player_1.png').convert_alpha()
        img_pawn_2 = pygame.image.load('images/game/pawn_player_2.png').convert_alpha()

        img_pawn_1 = pygame.transform.scale(img_pawn_1,
                                            (int(self._screen_width * scale), int((self._screen_height + 350) * scale)))

        text_pawn_1 = font_text.render("Pion joueur 1", True, black)

        img_pawn_2 = pygame.transform.scale(img_pawn_2,
                                            (int(self._screen_width * scale), int((self._screen_height + 350) * scale)))

        text_pawn_2 = font_text.render("Pion joueur 1", True, black)

        title_rect = title.get_rect()
        title_rect.center = (self._screen_width // 2, 35)

        # infinite loop
        while True:

            display_surface.fill(sakura)

            if self._leave_btn.draw():
                sys.exit("Game leave")

            if self._back_btn.draw():
                Menu()

            display_surface.blit(title, title_rect)
            display_surface.blit(text_0, (100, 100))
            display_surface.blit(text_1, (100, 130))
            display_surface.blit(text_2, (100, 160))

            display_surface.blit(img_ring_1, (200, 170))
            display_surface.blit(text_ring_1, (250, 370))
            display_surface.blit(img_ring_2, (400, 170))
            display_surface.blit(text_ring_2, (450, 370))

            display_surface.blit(img_pawn_1, (700, 170))
            display_surface.blit(text_pawn_1, (780, 370))
            display_surface.blit(img_pawn_2, (900, 170))
            display_surface.blit(text_pawn_2, (970, 370))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Game leave")
                pygame.display.update()


menu = Menu()
menu.music_menu()
menu.window()
