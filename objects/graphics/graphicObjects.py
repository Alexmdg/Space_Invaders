import pygame, os

class ImageLoader:
    def __init__(self):
        self.city_background = pygame.image.load(os.path.join('objects\graphics\images\\', '2834.jpg')).convert_alpha()
        self.menu_background = pygame.image.load(os.path.join('objects\graphics\images\\', '247.jpg')).convert_alpha()
        self.base_player = pygame.image.load(os.path.join('objects\graphics\images\\', 'soldier.png')).convert_alpha()
        self.power_up = pygame.image.load(os.path.join('objects\graphics\images\\', 'powerup.png')).convert_alpha()
        self.ink_stain = pygame.image.load(os.path.join('objects\graphics\images\\', 'stain.png')).convert_alpha()
        self.space_octo = pygame.image.load(os.path.join('objects\graphics\images\\', 'ennemy.png')).convert_alpha()
        self.arrow = pygame.image.load(os.path.join('objects\graphics\images\\', 'spear.png')).convert_alpha()

