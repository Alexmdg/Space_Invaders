from pygame import Surface, Rect, draw, font
import pygame.event
import pygame.transform
import settings

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.INFO)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)

class Pannel:
    def __init__(self, size):
        self.size = size
        self.image = Surface(size, flags=pygame.SRCALPHA)
        self.rect = self.image.get_rect()

    def set_border_Color(self, color):
        draw.line(self.image, color, (0, 0), (self.size[0], 0), 3)
        draw.line(self.image, color, (0, 0), (0, self.size[1]), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (self.size[0], 0), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (0, self.size[1]), 3)


class Button(Pannel):
    def __init__(self, name, size, msg, font_size, event, font_color=settings.GREY):
        super().__init__(size)
        self.size = size
        self.font_size=font_size
        self.fpnt_color = font_color
        self.image.fill(settings.PURPLE)
        self.name = name
        self.text = TextLabel(size, msg, font_size, font_color)
        self.image.blit(self.text.label, self.text.rect)
        self.event = event

    def click_down(self):
        self.text.change_settings(font_size=self.text.font_size)
        self.image.blit(self.text.label, self.text.rect)
        rect_logger.success(f'button {self.name} has been clicked down')

    def click_up(self):
        self.text.change_settings(font_size=self.text.font_size, font_color=settings.GREY)
        self.image.blit(self.text.label, self.text.rect)
        self.is_clicked = True
        for event in self.event:
            pygame.event.post(event.event)
            if event.event.sender == 'HeroMenuBack' or event.event.sender == 'HeroMenuNext':
                self.event.remove(event)
        rect_logger.success(f'button {self.name} has been clicked up')

    def change_txt(self, msg):
        self.text = TextLabel(self.size, msg, self.font_size, self.font_color)
        self.image.blit(self.text.label, self.text.rect)


class TextLabel:
    def __init__(self, size, msg, font_size=24, color=settings.GREY):
        self.font_size = font_size
        self.msg = msg
        self.font = font.SysFont(None, self.font_size)
        self.label = self.font.render(msg, True, color)
        self.rect = self.label.get_rect()
        self.rect.center = (size[0] / 2, size[1] / 2)

    def change_settings(self, font_size=24, font_color=settings.YELLOW):
        self.font = font.SysFont(None, font_size)
        self.label = self.font.render(self.msg, True, font_color)


class ItemBox(Pannel):
    def __init__(self, name, side='Vertical'):
        self.name = name
        self.side = side
        self.items = []


    def createPannel(self, centerx=settings.SCREEN_SIZE[0]/2, centery=settings.SCREEN_SIZE[1]/2, space_between=0, transparent=False,
                     bg_color=settings.Purple(0), bttn_color=settings.Purple(0)):

        if self.side == 'Vertical':
            self.space_between = (space_between * settings.SCREEN_SIZE[1]) / 100
            sizeX = 0
            sizeY = self.space_between * (len(self.items) - 1)
            for item in self.items:
                sizeX = max(sizeX, item.size[0])
                sizeY += item.size[1]

            super().__init__((sizeX, sizeY))
            self.image.fill(settings.PURPLE)
            self.rect.centerx = centerx
            self.rect.centery = centery

            pos = 0
            if transparent is True:
                self.image.fill(settings.Purple(0))
            for item in self.items:
                item.rect.x = 0
                item.rect.y = pos
                pos += item.size[1] + self.space_between
                self.image.blit(item.image, item.rect)
        elif self.side == 'Horizontal':
            self.space_between = (space_between * settings.SCREEN_SIZE[0]) / 100
            sizeY = 0
            sizeX = self.space_between * (len(self.items) - 1)
            for item in self.items:
                sizeY = max(sizeY, item.size[1])
                sizeX += item.size[0]

            super().__init__((sizeX, sizeY))
            self.image.fill(settings.PURPLE)
            self.rect.centerx = centerx
            self.rect.centery = centery

            pos = 0

            if transparent is True:
                self.image.convert_alpha()
                self.image.fill(bg_color)
            for item in self.items:
                item.rect.y = 0
                item.rect.x = pos
                pos += item.size[0] + self.space_between
                if transparent is True:
                    if type(item) == Button:
                        item.image.convert_alpha()
                        item.image.fill(bttn_color)
                        item.image.blit(item.text.label, item.text.rect)
                self.image.blit(item.image, item.rect)

    def update(self):
        for item in self.items:
            display_logger.debug(f'{item}')
            self.image.blit(item.image, item.rect)


class Menu(Pannel):
    def __init__(self, ratiox=0.618, ratioy=0.618):
        super().__init__(settings.SCREEN_SIZE)
        self.menu_body = Pannel((settings.SCREEN_SIZE[0] * ratiox, settings.SCREEN_SIZE[1] * ratioy))
        self.item_boxes = [ItemBox('mainBox')]
        self.targetbox = None

        self.is_running = True
        self.pos = 0
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.image.blit(self.background, (0, 0))

        self.menu_body.rect.centerx = self.size[0] / 2
        self.menu_body.rect.centery = self.size[1] / 2
        self.menu_body.image.fill(settings.PURPLE)

        self.clock = pygame.time.Clock()
        self.count = 3
        self.time = 0
        self.image.blit(self.menu_body.image, self.menu_body.rect)

    def add_button(self, itemBox_name, name, label, event=None,
                   xratio=0.618, yratio=0.161,
                   font_size=48):
        def search_itemBox_name(box_list, box_name):
            for box in box_list:
                if box.name == box_name:
                    box.items.append(button)
                elif type(box) == ItemBox:
                    search_itemBox_name(box.items, box_name)
        button = Button(name,
                        (xratio * self.menu_body.size[0],
                         yratio * self.menu_body.size[1]),
                        label,
                        font_size,
                        event)
        search_itemBox_name(self.item_boxes, itemBox_name)

    def search_itembox(self, target, ib=None):
        ib = self.item_boxes[0] if ib is None else ib
        for item in ib.items:
            rect_logger.debug(f'{item}, {type(item)}')
            if type(item) == ItemBox:
                if item.name == target:
                    rect_logger.success(f'Box found : {item.name} - {type(item)} - {item.items}')
                    self.targetbox = item
                else:
                    rect_logger.debug(f'Searching in {item.name}')
                    self.search_itembox(target, item)

    def search_button(self, target, ib=None):
        ib = self.item_boxes[0] if ib is None else ib
        for item in ib.items:
            if type(item) == Button:
                if item.name == target:
                    self.target_button = item
            elif type(item) == ItemBox:
                self.search_button(target, item)

    def create_pannels(self):
        def search_itemBox(itembox):
            boxes = 0
            for box in itembox.items:
                if type(box) == ItemBox:
                    try:
                        rect_logger.debug(settings.Fore.GREEN +
                            f'Box : {box.name} in Itembox : {itembox.name} init: Box_size = {box.size}: OK')
                    except:
                        boxes += 1
                        rect_logger.debug(f"Box : '{box.name}' in Itembox : '{itembox.name}' : searching ItemBoxes")
                        search_itemBox(box)
                        try:
                            box.createPannel(transparent=True)
                        except:
                            rect_logger.exception("Couldn't create pannel")
            if boxes == 0:
                itembox.createPannel(transparent=True)
            else:
                search_itemBox(itembox)
            return boxes

        try:
            for box in self.item_boxes:
                boxes = search_itemBox(box)
                while boxes > 0:
                    boxes = 0
                    search_itemBox(box)
                    rect_logger.debug(f'Boxes without pannels : {boxes}')
        except:
            rect_logger.exception("Couldn't create pannels")

    def update(self):
        for box in self.item_boxes:
            box.update()
            self.menu_body.image.blit(box.image, box.rect)
        self.image.blit(self.background, (0, 0))
        self.image.blit(self.menu_body.image, self.menu_body.rect)

    def click_down(self, button):
        button.click_down()

    def click_up(self, button):
        button.click_up()
        event_logger.debug('button clicked')
        self.is_running = False








