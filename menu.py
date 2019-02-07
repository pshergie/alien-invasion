import pygame.font
from button import Button


class Menu:
    def __init__(self, screen, stats):
        """Init a menu"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set parameters
        self.width = 600
        self.height = 400
        self.bg_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(stats)

        if stats.game_ended:
            self.prep_msg

        # Create Play button
        self.play_button = Button(screen, stats)

    def prep_text(self, stats):
        if not stats.game_active and not stats.game_paused and not stats.game_ended:
            self.msg = "Alien Invasion"
        elif stats.game_paused and not stats.game_ended:
            self.msg = "Paused"
        elif stats.game_ended:
            self.msg = "Game over"

    def prep_msg(self, stats):
        """Transform msg in a rectangle & align text center"""
        self.prep_text(stats)

        self.msg_image = self.font.render(
            self.msg, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.y = self.rect.center[1] - (100 if stats.game_ended else 60)

        if stats.game_ended:
            self.prep_score_msg(stats)

    def prep_score_msg(self, stats):
        self.score_msg = "Your score: {}".format(stats.score)
        self.score_msg_image = self.font.render(
            self.score_msg, True, self.text_color, self.bg_color)
        self.score_msg_image_rect = self.msg_image.get_rect()
        self.score_msg_image_rect.center = self.rect.center
        self.score_msg_image_rect.x = self.rect.center[0] - 110 - (5 * len(str(stats.score)))
        self.score_msg_image_rect.y = self.rect.center[1] - 60

    def draw_menu(self, stats):
        self.prep_msg(stats)
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        if stats.game_ended:
            self.screen.blit(self.score_msg_image, self.score_msg_image_rect)

        self.play_button.draw_button(stats)
