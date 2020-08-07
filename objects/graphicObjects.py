import pygame, os

class GraphicObjects:
    def __init__(self):
        self.base_player = pygame.image.load(os.path.join('images\\', 'soldier.png')).convert_alpha()
        self.ink_stain = pygame.image.load(os.path.join('images\\', 'stain.png')).convert_alpha()
        self.space_octo = pygame.image.load(os.path.join('images\\', 'ennemy.png')).convert_alpha()
        self.arrow = pygame.image.load(os.path.join('images\\', 'spear.png')).convert_alpha()