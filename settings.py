class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (127, 255, 212)
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 2.5
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 165, 42, 42
        self.bullets_allowed = 2
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 60
        self.fleet_direction = -1            # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.ship_limit = 3
