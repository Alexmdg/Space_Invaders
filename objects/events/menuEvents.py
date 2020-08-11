from pygame import USEREVENT
from pygame.event import Event



start_stage_Events = USEREVENT + 1
close_stage_Events = USEREVENT + 2
set_and_get_Events = USEREVENT + 3
start_menu_Events = USEREVENT + 4

class StartStageEvent:
    def __init__(self, render='StageRender', scene='StageScene', stage=1):
        self.event = Event(start_stage_Events,
                           {'render': render,
                            'scene': scene,
                            'stage': stage})

class CloseStageEvents:
    def __init__(self, render='StageRender', scene='StageScene', stage=1):
        self.event = Event(start_stage_Events,
                           {'render': render,
                            'scene': scene,
                            'stage': stage})

class MenuEventsNewGame:
    def __init__(self):
        self.event = Event(menuEvents, {'action': 'StartGame',
                                        'context': 'restart',
                                        'sender': 'PauseMenu'})

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
