from objects.levelsObjects import *


logger = createLogger(__name__)
logger.setLevel(logging.DEBUG)


class LevelsRender:
    objects = {}
    def __init__(self):
        self.objects['player'] = Player()
        self.objects['enemies'] = OctoArmy(5, 12)
        self.objects['shots'] = Arrows()
        self.running = True

    def showObjects(self):
        for entity in self.objects:
            self.objects[entity].show(self.objects['player'].rect)

    def handleEvent(self, event):
        self.objects['shots'].fireShot(self.objects['player'].rect, event)

class MenuRender:
    pass

class GameInfosRender:
    pass




