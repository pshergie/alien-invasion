class Settings():
    """Class that stores all game settings"""

    def __init__(self):
        """Initilase static game settings"""
        # screen parameters
        self.screen_width = 1200
        self.screen_height = 690
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet parameters
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Game tempo factor
        self.speedup_scale = 1.1

        # Aliens cost increase factor
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1 means right; -1 means left
        self.fleet_direction = 1

        # Points amount for an alien
        self.alien_points = 50

    def increase_speed(self):
        """Increase game speed settings & alien cost"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
