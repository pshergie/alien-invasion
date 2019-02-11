import pygame.font


class FPSCounter:
    """Initialize fps counter"""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Font settings
        self.text_color = ai_settings.font_color
        self.font = pygame.font.SysFont(None, 30)

        # Prepare source image
        self.prep_counter(0)

    def prep_counter(self, fps):
        """Transform fps number to a graphic image"""
        fps_count = "fps: {}".format(fps)

        self.fps_counter_image = self.font.render(
            fps_count, True, self.text_color, self.ai_settings.bg_color)

        # Align best score to center top
        self.fps_counter_rect = self.fps_counter_image.get_rect()
        self.fps_counter_rect.centerx = self.screen_rect.centerx
        self.fps_counter_rect.left = 10
        self.fps_counter_rect.bottom = self.screen_rect.bottom - 10

    def show_fps(self):
        """Show current score, best score, level & ships left"""
        self.screen.blit(self.fps_counter_image, self.fps_counter_rect)
