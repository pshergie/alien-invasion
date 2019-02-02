import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # Init the game and create window object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    # Create the ship
    ship = Ship(screen)

    # Start main game loop
    while True:
        # Handle keyboard & mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Re-render screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()


run_game()
