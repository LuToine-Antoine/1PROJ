import pygame as pygame


class Button:
    def __init__(self, x, y, image, scale):
        self._width = image.get_width()
        self._height = image.get_height()
        self._image = pygame.transform.scale(image, (int(self._width*scale), int(self._height*scale)))
        self.rect = self._image.get_rect()
        self.rect.topleft = (x, y)
        self._clicked = False

        self._screen = pygame.display.set_mode((1280, 720))

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

        self._screen.blit(self._image, (self.rect.x, self.rect.y))

        return action
