from pygame import USEREVENT
from pygame.event import Event



start_stage_Events = USEREVENT + 1
start_menu_Events = USEREVENT + 2
close_render_Events = USEREVENT + 3
set_and_get_Events = USEREVENT + 4
quit_game_Events = USEREVENT + 5
power_up_Events = USEREVENT + 6


class StartStageEvents:
    def __init__(self, sender= 'MainMenu', render='StageRender', scene='StageScene', level=1):
        self.event = Event(start_stage_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class StartMenuEvents:
    def __init__(self, sender= 'LoseOutro', render='MenuRender', scene='MainMenu', level=1):
        self.event = Event(start_menu_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class CloseRenderEvents:
    def __init__(self, sender= 'MainMenu', render='StageRender', scene='StageScene', level=1):
        self.event = Event(close_render_Events,
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


class QuitGameEvents:
    def __init__(self, sender= 'MainMenu', render='StageRender', scene='StageScene', level=1):
        self.event = Event(quit_game_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'level': level})


class PowerUpEvents:
    def __init__(self, sender=1, action='+'):
        self.event = Event(power_up_Events,
                           {'sender': sender,
                            'action': action})

