class GameStats:
    """Trace statistics for the game"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # The game launches at active state
        self.game_active = True

    def reset_stats(self):
        """Initialize in process statistics"""
        self.ships_left = self.ai_settings.ship_limit
