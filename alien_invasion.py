import pygame

from settings import Settings
from ship import Ship
# from background import Background
import game_functions as gf


def run_game():
    # Init the game and create window object
    pygame.init()
    ai_settings = Settings()
    # background = Background("images/bg.jpg", (0, 0))

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    # Create the ship
    ship = Ship(ai_settings, screen)

    # Start main game loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
