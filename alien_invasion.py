import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from menu import Menu
from scoreboard import Scoreboard
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

    # Create an instance for game statistics storage & scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Create menu
    menu = Menu(screen, stats)

    # Create the ship, bullets group & aliens group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create aliens fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    game_process = True

    # Start main game loop
    while game_process:
        gf.check_events(
            ai_settings, screen, stats, sb, menu, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens, bullets, menu)


run_game()
