class GameStats:
    """Trace statistics for the game"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # The game launches in inactive state
        self.game_active = False
        self.game_paused = False

        # Best score shouldn't reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize in process statistics"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
