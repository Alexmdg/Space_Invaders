from pygame import USEREVENT
from pygame.event import Event

menuEvents = USEREVENT + 1

class MenuEventsStartGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'StartGame'})

class MenuEventsMainMenu:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'MainMenu'})

class MenuEventsQuitGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'Quit'})

class MenuEventsResumeGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'ResumeGame'})

class MenuEventsRestartLevel:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'RestartLevel'})

class MenuEventsContinueGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'ContinueGame'})

class MenuEventsNextLevel:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'NextLevel'})


class MenuEventsHeroMenu:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'HeroMenu'})
