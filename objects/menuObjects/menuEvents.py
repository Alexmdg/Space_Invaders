from pygame import USEREVENT
from pygame.event import Event

menuEvents = USEREVENT + 1

class MenuEventsStartGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'start_g'})

class MenuEventsQuitGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'Quit'})

class MenuEventsResumeGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'ResumeGame'})
