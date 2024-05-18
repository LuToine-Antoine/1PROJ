import pygame as pygame

class UImenue:
    def __init__(self, height=500, width=800):
        self._screen_height = height
        self._screen_width = width

        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption('Yinch')

        # Load button images
        self._solo_img = pygame.image.load('images/menu/button_solo.png').convert_alpha()
        self._local_img = pygame.image.load('images/menu/button_local.png').convert_alpha()
        self._rules_img = pygame.image.load('images/menu/button_rules.png').convert_alpha()
        self._setting_img = pygame.image.load('images/menu/button_settings.png').convert_alpha()

        # Garde la fenêtre ouverte
        run = True
        while run:

            self._screen.fill((202, 228, 241))
            testButton.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

    def get_screen(self):
        return self._screen

    def get_solo_img(self):
        return self._solo_img


class Button:
    def __init__(self, x, y, image):
        self._menu = UImenue()
        self._image = image
        self.rect = self._image.pygame.get_rect()
        self.rect.pygame.topleft = (x, y)

    def draw(self):
        self._menu.get_screen().blit(self._image, (self.rect.x, self.rect.y))


menu = UImenue()

testButton = Button(100, 200, menu.get_solo_img())
