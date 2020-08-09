from pygame import USEREVENT
from pygame.event import Event

menuEvents = USEREVENT + 1

class MenuEventsStartGame:
    def __init__(self):
        self.event = Event(menuEvents, {'sender': 'mainMenu',
                                        'action': 'start_g',})

class MenuEventsQuitGame:
    def __init__(self):
        self.event = Event(menuEvents, {'sender': 'pauseMenu',
                                        'action': 'Quit'})
