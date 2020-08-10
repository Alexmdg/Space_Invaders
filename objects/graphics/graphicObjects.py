import os
from pygame import image

class ImageLoader:
    def __init__(self):
        self.city_background = image.load(os.path.join('objects\graphics\images\\', '2834.jpg')).convert_alpha()
        self.menu_background = image.load(os.path.join('objects\graphics\images\\', '247.jpg')).convert_alpha()
        self.base_player = image.load(os.path.join('objects\graphics\images\\', 'soldier.png')).convert_alpha()
        self.power_up = image.load(os.path.join('objects\graphics\images\\', 'powerup.png')).convert_alpha()
        self.ink_stain = image.load(os.path.join('objects\graphics\images\\', 'stain.png')).convert_alpha()
        self.space_octo = image.load(os.path.join('objects\graphics\images\\', 'ennemy.png')).convert_alpha()
        self.space_ghost = image.load(os.path.join('objects\graphics\images\\', 'enemy2.png')).convert_alpha()
        self.space_blob = image.load(os.path.join('objects\graphics\images\\', 'enemy3.png')).convert_alpha()
        self.arrow = image.load(os.path.join('objects\graphics\images\\', 'spear.png')).convert_alpha()
        self.dead_bg = image.load(os.path.join('objects\graphics\images\\', '2245.jpg')).convert_alpha()
        self.win_bg = image.load(os.path.join('objects\graphics\images\\', 'win.jpg')).convert_alpha()


