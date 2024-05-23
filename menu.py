import pygame as pygame

width = 1280
height = 720
screen_height = height
screen_width = width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Yinch')
bg = pygame.image.load('images/menu/bg.jpg').convert_alpha()


class Button:
    def __init__(self, x, y, image, scale):
        self._width = image.get_width()
        self._height = image.get_height()
        self._image = pygame.transform.scale(image, (int(self._width*scale), int(self._height*scale)))
        self.rect = self._image.get_rect()
        self.rect.topleft = (x, y)
        self._clicked = False

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

        screen.blit(self._image, (self.rect.x, self.rect.y))

        return action


def music_menu():
    pygame.mixer.init()
    pygame.mixer.music.load('musics/menu_music.ogg', "ogg")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(loops=-1, start=0.0)


def window():

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

        screen.blit(bg, (0, 0))

        # if solo_button.draw():
        solo_button.draw()
        local_button.draw()
        rules_button.draw()
        setting_button.draw()
        sound_button()
        logo_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


def sound_button():

    on_sound_img = pygame.image.load('images/menu/sound_on.png').convert_alpha()
    off_sound_img = pygame.image.load('images/menu/sound_off.png').convert_alpha()

    on_sound_button = Button(1200, 650, on_sound_img, 0.1)
    off_sound_button = Button(1200, 650, off_sound_img, 0.1)

    on_sound_button.draw()
    off_sound_button.draw()


music_menu()
window()
