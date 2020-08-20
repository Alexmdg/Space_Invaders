from pygame import USEREVENT
from pygame.event import Event



start_stage_Events = USEREVENT + 1
start_menu_Events = USEREVENT + 2
close_render_Events = USEREVENT + 3
set_and_get_Events = USEREVENT + 4
quit_game_Events = USEREVENT + 5
power_up_Events = USEREVENT + 6


class StartStageEvents:
    def __init__(self, sender= 'MainMenuScene', render='StageRender', scene='StageScene', context=None):
        self.event = Event(start_stage_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'context': context})


class StartMenuEvents:
    def __init__(self, sender= 'LoseOutro', render='MenuRender', scene='MainMenuScene', context=None):
        self.event = Event(start_menu_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'context': context})


class CloseRenderEvents:
    def __init__(self, sender= 'MainMenuScene', render='StageRender', scene='StageScene', context=None):
        self.event = Event(close_render_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'context': context})


class GetSetEvents:
    def __init__(self, sender='MainMenuScene', action='get', hero='', level=1, context=None):
        self.event = Event(set_and_get_Events,
                           {'sender': sender,
                            'action': action,
                            'hero': hero,
                            'level': level,
                            'context': context})


class QuitGameEvents:
    def __init__(self, sender= 'MainMenuScene', render='StageRender', scene='StageScene', context=None):
        self.event = Event(quit_game_Events,
                           {'sender': sender,
                            'render': render,
                            'scene': scene,
                            'context': context})


class PowerUpEvents:
    def __init__(self, sender=1, action='+'):
        self.event = Event(power_up_Events,
                           {'sender': sender,
                            'action': action})

