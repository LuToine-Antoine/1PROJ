import pygame as pygame


class ButtonUi:
    def __init__(self, x, y, image, scale, screen_width=1280, screen_height=720,):
        """
        Initialize the button class.
        :param x:
        :param y:
        :param image:
        :param scale:
        :param screen_width:
        :param screen_height:
        """
        self._width = image.get_width()
        self._height = image.get_height()
        self._image = pygame.transform.scale(image, (int(self._width*scale), int(self._height*scale)))
        self.rect = self._image.get_rect()
        self.rect.topleft = (x, y)
        self._clicked = False

        self._screen = pygame.display.set_mode((screen_width, screen_height))

    def draw(self):
        """
        Draw the button on the screen and detect when an action is made (click on the button).
        """
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse hover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self._clicked:
                self._clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 1:
            self._clicked = False

        self._screen.blit(self._image, (self.rect.x, self.rect.y))

        return action
