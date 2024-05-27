import pygame as pygame
from main import *


class Menu:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        pygame.display.set_caption('Yinch')
        self._bg = pygame.image.load('images/menu/bg.jpg').convert_alpha()
        self._main = Game()

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
                self.display_solo()[0].draw()
                self.display_solo()[1].draw()
            local_button.draw()
            if rules_button.draw():
                self.display_rules()
            setting_button.draw()
            local_button.draw()
            logo_button.draw()


            if on_sound_button.draw():
                pygame.mixer.music.set_volume(0)
                off_sound_button.draw()
                pygame.display.update(on_sound_button)

            if off_sound_button.draw():
                pygame.mixer.music.set_volume(1)
                on_sound_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

    def display_solo(self):
        self._main.set_game_mode(0)

        normal_img = pygame.image.load('images/menu/button_classic.png').convert_alpha()
        blitz_img = pygame.image.load('images/menu/button_blitz.png').convert_alpha()

        normal_btn = Button(288, -10, normal_img, 0.32)
        blitz_btn = Button(288, 110, blitz_img, 0.32)

        return normal_btn, blitz_btn

    def display_local(self):
        self._main.set_game_mode(1)



    def display_rules(self):
        white = (255, 255, 255)
        gray = (91, 91, 91)
        blue = (0, 0, 128)

        display_surface = pygame.display.set_mode((self._screen_width, self._screen_height))

        pygame.display.set_caption('Yinch Rules')

        pygame.font.init()
        font_title = pygame.font.SysFont('freesansbold.ttf', 50)
        font_text = pygame.font.Font('freesansbold.ttf', 20)

        title = font_title.render('Yinsh - Règles', True, white)
        text_0 = font_text.render("Le but du jeu est d'aligner 5 pions afin de retirer 3 anneaux (en mode normal) ou 1 anneau (en mode blitz, rapide).", True, white)
        text_1 = font_text.render("En début de partie, chaques joueurs pose ses 5 anneaux sur le plateau a tour de rôle. Les pions se placent ensuite", True, white)
        text_2 = font_text.render("dans 1 anneaux et cet anneau se déplace sur les lignes à partir de sa position initiale.", True, white)

        title_rect = title.get_rect()
        title_rect.center = (self._screen_width // 2, 35)

        # infinite loop
        while True:

            display_surface.fill(gray)

            display_surface.blit(title, title_rect)
            display_surface.blit(text_0, (100, 100))
            display_surface.blit(text_1, (100, 130))
            display_surface.blit(text_2, (100, 160))

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
