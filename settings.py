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
