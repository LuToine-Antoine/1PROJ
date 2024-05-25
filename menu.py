import pygame as pygame


class Menu:
    def __init__(self, width=1280, height=720):
        self._screen_height = height
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

        pygame.display.set_caption('Yinch')
        self._bg = pygame.image.load('images/menu/bg.jpg').convert_alpha()

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

            solo_button.draw()
            local_button.draw()
            if rules_button.draw():
                Rules().display_rules()
            setting_button.draw()
            local_button.draw()
            logo_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

    def sound_button(self):

        on_sound_img = pygame.image.load('images/menu/sound_on.png').convert_alpha()
        off_sound_img = pygame.image.load('images/menu/sound_off.png').convert_alpha()

        on_sound_button = Button(1200, 650, on_sound_img, 0.1)
        off_sound_button = Button(1200, 650, off_sound_img, 0.1)

        on_sound_button.draw()
        off_sound_button.draw()

        if on_sound_button.draw():
            pygame.mixer.music.set_volume(0)
            off_sound_button.draw()

        # if off_sound_button.draw():
        #     pygame.mixer.music.set_volume(1)
        #     on_sound_button.draw()


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


class Rules:

    def __init__(self, width=1280, height=720):
        self._width = width
        self._height = height

    def display_rules(self):
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)

        # create the display surface object
        # of specific dimension..e(X, Y).
        display_surface = pygame.display.set_mode((self._width, self._height))

        # set the pygame window name
        pygame.display.set_caption('Yinch Rules')

        # create a font object.
        # 1st parameter is the font file
        # which is present in pygame.
        # 2nd parameter is size of the font
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 32)

        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('test', True, green, blue)

        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (self._width // 2, self._height // 2)

        # infinite loop
        while True:

            display_surface.fill(white)

            display_surface.blit(text, textRect)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    quit()

                pygame.display.update()


class SoloMode:
    def __init__(self):
        pass

menu = Menu()
menu.music_menu()
menu.window()
