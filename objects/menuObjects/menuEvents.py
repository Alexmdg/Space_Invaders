from pygame import USEREVENT
from pygame.event import Event

menuEvents = USEREVENT + 1

class MainMenuEvents:
    def __init__(self, render, scene):
        self.event = Event(menuEvents, {'render': render, 'scene': scene})
