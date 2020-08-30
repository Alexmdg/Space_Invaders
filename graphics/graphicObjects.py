import os
from pygame import image

class ImageLoader:
    def __init__(self):
        self.city_background = image.load(os.path.join('graphics\images\\', '2834.jpg')).convert_alpha()
        self.menu_background = image.load(os.path.join('graphics\images\\', '247.jpg')).convert_alpha()
        self.base_player = image.load(os.path.join('graphics\images\\', 'soldier.png')).convert_alpha()
        self.power_up = image.load(os.path.join('graphics\images\\', 'powerup.png')).convert_alpha()
        self.ink_stain = image.load(os.path.join('graphics\images\\', 'stain.png')).convert_alpha()
        self.alien_laser = image.load(os.path.join('graphics\images\\', 'alien_laser.png')).convert_alpha()
        self.space_octo = image.load(os.path.join('graphics\images\\', 'ennemy.png')).convert_alpha()
        self.space_ghost = image.load(os.path.join('graphics\images\\', 'enemy2.png')).convert_alpha()
        self.space_blob = image.load(os.path.join('graphics\images\\', 'enemy3.png')).convert_alpha()
        self.arrow = image.load(os.path.join('graphics\images\\', 'spear.png')).convert_alpha()
        self.wood = image.load(os.path.join('graphics\images\\', 'wood.png')).convert_alpha()
        self.bullet = image.load(os.path.join('graphics\images\\', 'bullet.png')).convert_alpha()
        self.meteor = image.load(os.path.join('graphics\images\\', 'meteor.png')).convert_alpha()
        self.fireball = image.load(os.path.join('graphics\images\\', 'fireball.png')).convert_alpha()
        self.dead_bg = image.load(os.path.join('graphics\images\\', '2245.jpg')).convert_alpha()
        self.win_bg = image.load(os.path.join('graphics\images\\', 'win.jpg')).convert_alpha()


