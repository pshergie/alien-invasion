class Settings():
    """Class that stores all game settings"""

    def __init__(self):
        """Initilase game settings"""
        # screen parameters
        self.screen_width = 1200
        self.screen_height = 690
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet parameters
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet_direction = 1 means right; -1 means left
        self.fleet_direction = 1
