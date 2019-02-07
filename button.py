import pygame.font


class Button:
    def __init__(self, screen, stats):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set button size & props
        self.width, self.height = 200, 50
        self.button_color = (115, 76, 221)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build rect button object & align center of screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = self.rect.center[1] + 5

        # Create button text
        self.prep_msg(stats)

    def prep_text(self, stats):
        if not stats.game_active and not stats.game_paused and not stats.game_ended:
            self.msg = "Play"
        elif stats.game_paused and not stats.game_ended:
            self.msg = "Continue"
        elif stats.game_ended:
            self.msg = "Try again"

    def prep_msg(self, stats):
        """Transform msg in a rectangle & align text center"""
        self.prep_text(stats)

        self.msg_image = self.font.render(
            self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, stats):
        # Draw empty button & output the message
        self.prep_msg(stats)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

