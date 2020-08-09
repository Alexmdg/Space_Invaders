from objects.menus import *


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)

class StageRender(pygame.Surface):
    def __init__(self, size, stage):
        super().__init__(size)
        self.stage = stage
        self.update()
        self.is_running = True
        self.is_paused = False

    def update(self):
        self.blit(self.stage.background, (0, 0))
        self.blit(self.stage.topbar, (0, 0))
        if self.stage.intro.is_running:
            self.stage.intro.update()
            for object in self.stage.objects:
                for elem in self.stage.objects[object]:
                    for sprite in elem.sprites():
                        self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))
            self.blit(self.stage.intro.bg.image, self.stage.intro.bg.rect)
            self.blit(self.stage.intro.title.label, self.stage.intro.title.rect)
            self.blit(self.stage.intro.counter.label, self.stage.intro.counter.rect)
        else:
            self.stage.update()
            self._collisionHandler()
            for object in self.stage.objects:
                for elem in self.stage.objects[object]:
                    elem.update()
                    for sprite in elem.sprites():
                        self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))


    def handleEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_paused = True
        self.stage.objects['shots'][0].fireShot(self.stage.objects['player'][0].sprites()[0].rect, event)

    def _collisionHandler(self):
        for enemies in self.stage.objects['enemies']:
            if pygame.sprite.spritecollideany(self.stage.objects['player'][0].sprites()[0], enemies):
                self.stage.is_death_outro_running = True
            deaths = pygame.sprite.groupcollide(self.stage.objects['shots'][0],
                                                enemies,
                                                True, True)
            power_up = pygame.sprite.spritecollideany(self.stage.objects['player'][0].sprites()[0], self.stage.objects['deads'][0])
            if power_up:
                self.stage.objects['player'][0].power_up += 1
                power_up.kill()
            for arrow in deaths:
                for dead in deaths[arrow]:
                    self.stage.objects['deads'][0].died(dead)


class MenuRender(pygame.Surface):
    def __init__(self, menu):
        super().__init__(menu.body.size)
        self.is_running = True
        self.is_paused = False
        main_logger.succes('MenuRender init : OK')
        self.menu = menu
        main_logger.succes('Load Menu Object : OK')
        self.blit(self.menu.body.image, (0, 0))
        main_logger.succes('Display main menu : OK')

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            event_logger.debug(f'click : {event.type}, {event.pos}')
            for button in self.menu.buttons.buttons:
                button_x1 = self.menu.body.rect.centerx + button.body.rect[0]
                button_y1 = self.menu.body.rect.centery - button.body.rect[1]
                hitbox = pygame.Rect((button_x1, button_y1), (button.body.rect[2], button.body.rect[3]))
                event_logger.debug(f'button rect : {hitbox}')
                event_logger.debug(f'collidepoint : {hitbox.collidepoint(event.pos)}')
                if hitbox.collidepoint(event.pos):
                    self.menu.on_click(button)


    def update(self):
        self.menu.update()
        self.blit(self.menu.body.image, (0, 0))














