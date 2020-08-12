from pygame import USEREVENT
from pygame.event import Event



start_stage_Events = USEREVENT + 1
close_stage_Events = USEREVENT + 2
set_and_get_Events = USEREVENT + 3
start_menu_Events = USEREVENT + 4
close_menu_Events = USEREVENT + 5
quit_game_Events = USEREVENT + 6


class StartStageEvent:
    def __init__(self, sender= 'MainMenu', render='StageRender', scene='StageScene', level=1):
        self.event = Event(start_stage_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class CloseStageEvents:
    def __init__(self, sender= 'MainMenu', render='StageRender', scene='StageScene', level=1):
        self.event = Event(close_stage_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class StartMenuEvent:
    def __init__(self, sender= 'LoseOutro', render='MenuRender', scene='MainMenu', level=1):
        self.event = Event(start_menu_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class CloseMenuEvents:
    def __init__(self, sender= 'MainMenu', render='MenuRender', scene='MainMenu', level=1):
        self.event = Event(close_menu_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class QuitGameEvents:
    def __init__(self, sender= 'MainMenu', render='StageRender', scene='StageScene', level=1):
        self.event = Event(quit_game_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class GetSetEvents:
    def __init__(self, sender='MainMenu',
                type='get', hero='', level=1,
                context=''):
        self.event = Event(set_and_get_Events,
                           {'sender': sender,
                            'type': type,
                            'hero': hero,
                            'level': level,
                            'context': context})

