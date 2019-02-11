import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """Init an alien ans set init position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load an alien image and set rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Every new alien should appear in left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save alien float position
        self.x = float(self.rect.x)

    def blitme(self):
        """Render alien in current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move alien left or right"""
        self.x += (
            self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        )
        self.rect.x = self.x

        # if ticks % 50 == 0:
        #     self.shoot()

    def check_edges(self):
        """Return True if the alien is at the edge"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def shoot(self):
        """Trigger alien to shoot"""
        print("Shot!")
