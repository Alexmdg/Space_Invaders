from pygame import USEREVENT
from pygame.event import Event

menuEvents = USEREVENT + 1

class TransEventsContinue:
    def __init__(self, action='StartGame', sender='OutroWin', context=''):
        self.event = Event(menuEvents, {'action': action,
                                        'sender': sender,
                                        'context': context})