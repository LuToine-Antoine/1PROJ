import pygame as pygame
from main import *
from ui.game_ui import *


class Menu:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        pygame.display.set_caption('Yinch')
        self._bg = pygame.image.load('images/menu/bg.jpg').convert_alpha()
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

        on_sound_img = pygame.image.load('images/menu/sound_on.png').convert_alpha()
        off_sound_img = pygame.image.load('images/menu/sound_off.png').convert_alpha()

        on_sound_button = Button(1200, 650, on_sound_img, 0.1)
        off_sound_button = Button(1200, 650, off_sound_img, 0.1)

        run = True
        while run:

            self.get_screen().blit(self._bg, (0, 0))

            if solo_button.draw():
                self.display_solo()
            local_button.draw()
            if rules_button.draw():
                self.display_rules()
            setting_button.draw()
            local_button.draw()
            logo_button.draw()

            # if on_sound_button.draw():
            #     pygame.mixer.music.set_volume(0)
            #     off_sound_button.draw()
            #     pygame.display.update(on_sound_button)

            # if off_sound_button.draw():
            #     pygame.mixer.music.set_volume(1)
            #     on_sound_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

    def display_solo(self):
        self._main.set_game_mode(0)

        display_surface = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption('Yinch Solo mode')

        normal_img = pygame.image.load('images/menu/button_classic.png').convert_alpha()
        blitz_img = pygame.image.load('images/menu/button_blitz.png').convert_alpha()

        normal_btn = Button(288, -10, normal_img, 0.32)
        blitz_btn = Button(288, 110, blitz_img, 0.32)

        while True:

            self.get_screen().blit(self._bg, (0, 0))

            if normal_btn.draw():
                self._main.set_game_mode(0)
                self._board_ui.window()
            if blitz_btn.draw():
                self._main.set_game_mode(1)
                self._board_ui.window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

    def display_local(self):
        self._main.set_game_mode(1)

        display_surface = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption('Yinch Solo mode')

        normal_img = pygame.image.load('images/menu/button_classic.png').convert_alpha()
        blitz_img = pygame.image.load('images/menu/button_blitz.png').convert_alpha()

        normal_btn = Button(288, -10, normal_img, 0.32)
        blitz_btn = Button(288, 110, blitz_img, 0.32)

        while True:

            self.get_screen().blit(self._bg, (0, 0))

            if normal_btn.draw():
                self._main.set_game_mode(0)
                self._board_ui.window()
            if blitz_btn.draw():
                self._main.set_game_mode(1)
                self._board_ui.window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

    def display_rules(self):
        white = (0, 0, 0)
        gray = (91, 91, 91)

        display_surface = pygame.display.set_mode((self._screen_width, self._screen_height))
        scale = 0.2

        pygame.display.set_caption('Yinch Rules')

        pygame.font.init()
        font_title = pygame.font.SysFont('freesansbold.ttf', 50)
        font_text = pygame.font.Font('freesansbold.ttf', 20)

        title = font_title.render(
            'Yinsh - Règles', True, white)
        text_0 = font_text.render("Le but du jeu est d'aligner 5 pions afin de retirer 3 anneaux (en mode normal) ou 1 anneau (en mode blitz, rapide).", True, white)
        text_1 = font_text.render("En début de partie, chaques joueurs pose ses 5 anneaux sur le plateau a tour de rôle. Les pions se placent ensuite", True, white)
        text_2 = font_text.render("dans 1 anneaux et cet anneau se déplace sur les lignes à partir de sa position initiale.", True, white)

        img_ring_1 = pygame.image.load('images/game/ring_player_1.png').convert_alpha()
        img_ring_2 = pygame.image.load('images/game/ring_player_2.png').convert_alpha()

        img_ring_1 = pygame.transform.scale(img_ring_1,
                                            (int(self._screen_width * scale), int((self._screen_height + 500) * scale)))

        text_ring_1 = font_text.render("Anneau joueur 1", True, white)

        img_ring_2 = pygame.transform.scale(img_ring_2,
                                            (int(self._screen_width * scale), int((self._screen_height + 500) * scale)))

        text_ring_2 = font_text.render("Anneau joueur 2", True, white)

        img_pawn_1 = pygame.image.load('images/game/pawn_player_1.png').convert_alpha()
        img_pawn_2 = pygame.image.load('images/game/pawn_player_2.png').convert_alpha()

        img_pawn_1 = pygame.transform.scale(img_pawn_1,
                                            (int(self._screen_width * scale), int((self._screen_height + 350) * scale)))

        text_pawn_1 = font_text.render("Pion joueur 1", True, white)

        img_pawn_2 = pygame.transform.scale(img_pawn_2,
                                            (int(self._screen_width * scale), int((self._screen_height + 350) * scale)))

        text_pawn_2 = font_text.render("Pion joueur 1", True, white)

        title_rect = title.get_rect()
        title_rect.center = (self._screen_width // 2, 35)

        # infinite loop
        while True:

            # display_surface.fill(gray)
            self.get_screen().blit(self._bg, (0, 0))

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
                    quit()
                pygame.display.update()


class Button:
    def __init__(self, x, y, image, scale):
        self._width = image.get_width()
        self._height = image.get_height()
        self._image = pygame.transform.scale(image, (int(self._width*scale), int(self._height*scale)))
        self.rect = self._image.get_rect()
        self.rect.topleft = (x, y)
        self._clicked = False

        self._menu = Menu()

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouse hover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self._clicked:
                self._clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 1:
            self._clicked = False

        self._menu.get_screen().blit(self._image, (self.rect.x, self.rect.y))

        return action


menu = Menu()
menu.music_menu()
menu.window()
