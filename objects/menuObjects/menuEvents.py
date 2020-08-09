from pygame import USEREVENT
from pygame.event import Event

menuEvents = USEREVENT + 1

class MainMenuEvents:
    def __init__(self, button, action, render, scene):
        self.event = Event(menuEvents, {'sender': 'mainMenu',
                                        'button': button,
                                        'action': action,
                                        'render': render,
                                        'scene': scene})

class PauseMenuEvents:
    def __init__(self, button, action, render, scene):
        self.event = Event(menuEvents, {'sender': 'pauseMenu',
                                        'button': button,
                                        'action': action,
                                        'render': render,
                                        'scene': scene})
