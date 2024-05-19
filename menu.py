import pygame as pygame

height = 500
width = 800

screen_height = height
screen_width = width

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Yinch')

# Load button images
solo_img = pygame.image.load('images/menu/button_solo.png').convert_alpha()
local_img = pygame.image.load('images/menu/button_local.png').convert_alpha()
rules_img = pygame.image.load('images/menu/button_rules.png').convert_alpha()
setting_img = pygame.image.load('images/menu/button_settings.png').convert_alpha()


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


# Create buttons
solo_button = Button(100, 200, solo_img, 0.5)
local_button = Button(200, 210, local_img, 0.5)
rules_button = Button(200, 220, rules_img, 0.5)
setting_button = Button(220, 230, setting_img, 0.5)


# Garde la fenêtre ouverte
run = True
while run:

    screen.fill((202, 228, 241))

    # appelle une fonction du jeu, ici le mode solo if solo_button.draw():
    solo_button.draw()
    local_button.draw()
    rules_button.draw()
    setting_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
