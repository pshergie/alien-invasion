import pygame


class Ship():
    def __init__(self, screen):
        """Initialise the ship and set it's initial position"""
        self.screen = screen

        # Load ship's image & get a rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Every ship should appear at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship in current position"""
        self.screen.blit(self.image, self.rect)
