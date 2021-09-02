class Settings:
    """"A class to store settings"""
    
    def __init__(self):
        """"Initialize the game's settings."""
        #Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        