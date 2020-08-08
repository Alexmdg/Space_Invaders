import pygame

menuEvents = pygame.USEREVENT + 1

class MainMenuEvents:
    def __init__(self, render, scene):
        pygame.event.Event(menuEvents, {'render': render, 'scene': scene})
