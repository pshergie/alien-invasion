import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
# from background import Background


def run_game():
    # Init the game and create window object
    pygame.init()
    ai_settings = Settings()
    # background = Background("images/bg.jpg", (0, 0))

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    # Create Play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance for game statistics storage
    stats = GameStats(ai_settings)

    # Create the ship, bullets group & aliens group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create aliens fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start main game loop
    while True:
        gf.check_events(
            ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
