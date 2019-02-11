import sys
import pygame
import random
from time import sleep
from bullet import Bullet
from alien_bullet import AlienBullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets):
    """Create a bullet if no limit"""
    # Create new bullet & include it in group bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def alien_fire_bullet(ai_settings, screen, alien, alien_bullets):
    """Create an alien bullet"""
    new_alien_bullet = AlienBullet(ai_settings, screen, alien)
    alien_bullets.add(new_alien_bullet)


def check_final_score(stats):
    if stats.score >= stats.high_score:
        score_file = open('score.txt', 'w')
        score_file.write(str(stats.score))
        score_file.close()


def check_keydown_events(event, ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Handle key down"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RETURN:
        if not stats.game_active and not stats.game_paused:
            start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif stats.game_paused:
            resume_game(stats)
    elif event.key == pygame.K_SPACE:
        if stats.game_active and not stats.game_paused:
            fire_bullet(ai_settings, screen, ship, bullets)
        elif stats.game_paused and not stats.game_active:
            resume_game(stats)
        elif not stats.game_active and not stats.game_paused:
            start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
    elif event.key == pygame.K_q:
        check_final_score(stats)
        sys.exit()
    elif stats.game_active and event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
        pause_game(stats)


def check_keyup_events(event, ship):
    """Handle key up"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(
        ai_settings, screen, stats, sb, menu, ship, aliens, bullets):
    # Handle keyboard & mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check_final_score(stats)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if stats.game_paused:
                resume_game(stats)
            else:
                check_play_button(
                    ai_settings, screen, stats, sb, menu,
                    ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                event, ai_settings, stats, sb, screen, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Reset game settings
    ai_settings.initialize_dynamic_settings()

    # Hide mouse cursor
    pygame.mouse.set_visible(False)

    # Reset game statistics
    stats.reset_stats()
    stats.game_active = True

    # Empty score & level images
    sb.prep_images()

    # Empty aliens & bullets lists
    aliens.empty()
    bullets.empty()

    # Create new fleet & set the ship to bottom center
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def pause_game(stats):
    stats.game_active = False
    stats.game_paused = True

    # Show mouse cursor
    pygame.mouse.set_visible(True)


def resume_game(stats):
    stats.game_active = True
    stats.game_paused = False

    # Hide mouse cursor
    pygame.mouse.set_visible(False)


def end_game(stats):
    stats.game_active = False
    stats.game_ended = True

    # Show mouse cursor
    pygame.mouse.set_visible(True)


def check_play_button(
        ai_settings, screen, stats, sb, menu,
        ship, aliens, bullets, mouse_x, mouse_y):
    """Start new game on Play button press"""
    button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_screen(
        ai_settings, screen, stats, sb, ship, aliens,
        bullets, alien_bullets, menu, fps_counter, fps):
    # Re-render screen
    screen.fill(ai_settings.bg_color)

    # Show scoreboard
    sb.show_score()

    # Show fps counter
    fps_counter.show_fps()
    fps_counter.prep_counter(fps)

    # All bullets draws before
    # screen & alien images
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Show Play button if game is inactive
    if stats.game_paused and not stats.game_active:
        menu.draw_menu(stats)
    elif not stats.game_paused and not stats.game_active:
        menu.draw_menu(stats)

    # Show last rendered screen
    pygame.display.flip()


def update_bullets(
        ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    """Update bullets position & remove old bullets"""
    # Update bullets position
    bullets.update()
    alien_bullets.update()

    # Delete out of screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Delete out of screen alien bullets
    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= screen.get_rect().bottom:
            alien_bullets.remove(alien_bullet)

    check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)

    check_alien_bullet_ship_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)


def check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    """Handle collision between bullet & aliens"""
    # Remove bullets & aliens which have collisions
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)

    if len(aliens) == 0:
        start_new_level(
            ai_settings, screen, stats, sb, ship,
            aliens, bullets, alien_bullets)


def check_alien_bullet_ship_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    """Handle collision between bullet & aliens"""
    # Remove bullets & aliens which have collisions

    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(
            ai_settings, stats, sb, screen,
            ship, aliens, bullets, alien_bullets)


def start_new_level(
        ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    # Destroy existing bullets, speedup the game, create a new fleet
    # and increase level count
    bullets.empty()
    alien_bullets.empty()
    ai_settings.increase_speed()

    # Increase level
    stats.level += 1
    sb.prep_level()

    create_fleet(ai_settings, screen, ship, aliens)


def ship_hit(
        ai_settings, stats, sb, screen,
        ship, aliens, bullets, alien_bullets):
    """Handle collision between ship and alien/alien_bullet"""
    if stats.ships_left > 0:
        # Reduce ships_left
        stats.ships_left -= 1

        # Update game info
        sb.prep_ships()

        # Empty aliens & bullets list
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # Create a new fleet & place the ship at the center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)

    else:
        end_game(stats)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create aliens fleet"""
    # Create an alien and calculate row count
    # Interval between aliens equals alien width

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create alien fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """Calculate aliens count per row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and put it into row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Return possible row count"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(
        ai_settings, stats, sb, screen, ship,
        aliens, bullets, alien_bullets, ticks):
    """Check if fleet is at the edge, then update aliens positions"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Check collision "alien-ship"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(
            ai_settings, stats, sb, screen, ship,
            aliens, bullets, alien_bullets)

    # Check aliens which reached bottom edge
    check_aliens_bottom(
        ai_settings, stats, sb, screen, ship, aliens, bullets, alien_bullets)

    if ticks % ai_settings.tick_factor == 0:
        rand_id = random.randint(0, len(aliens))
        for idx, alien in enumerate(aliens.sprites()):
            if idx == rand_id:
                alien_fire_bullet(ai_settings, screen, alien, alien_bullets)


def check_aliens_bottom(
        ai_settings, stats, sb, screen, ship, aliens, bullets, alien_bullets):
    """Check if aliens reach bottom edge"""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Did the same as for ship collision
            ship_hit(
                ai_settings, stats, sb, screen, ship,
                aliens, bullets, alien_bullets)
            break


def check_fleet_edges(ai_settings, aliens):
    """React to the alien edge touch"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the fleet and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def check_high_score(stats, sb):
    """Check if new record appears"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
