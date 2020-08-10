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
        if self.stage.is_running:
            self.stage.topbar.update()
            self.blit(self.stage.background, (0, 0))
            self.blit(self.stage.topbar.image, (0, 0))
            if self.stage.intro.is_running:
                self.stage.intro.update()
                for object in self.stage.objects:
                    for elem in self.stage.objects[object]:
                        for sprite in elem.sprites():
                            self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))
                self.blit(self.stage.intro.image, self.stage.intro.rect)
            elif self.stage.outro.is_running:
                self.stage.outro.update()
                for object in self.stage.objects:
                    for elem in self.stage.objects[object]:
                        for sprite in elem.sprites():
                            self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))
                self.blit(self.stage.outro.image, self.stage.outro.rect)
            elif self.stage.objects['player'][0].stats.kills == self.stage.level.total_unit:
                self.stage.outro.chose_ending('win')
                self.stage.outro.is_running = True
            else:
                self.stage.update()
                self._collisionHandler()
                for object in self.stage.objects:
                    for elem in self.stage.objects[object]:
                        elem.update()
                        for sprite in elem.sprites():
                            self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))
        else:
            self.is_running = False


    def handleEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_paused = True
        self.stage.objects['shots'][0].fireShot(self.stage.objects['player'][0].sprites()[0].rect, event)

    def _collisionHandler(self):
        for enemies in self.stage.objects['enemies']:
            if pygame.sprite.spritecollideany(self.stage.objects['player'][0].sprites()[0], enemies):
                self.stage.outro.is_running = True
                self.stage.outro.chose_ending('lose')
            deaths = pygame.sprite.groupcollide(self.stage.objects['shots'][0],
                                                enemies,
                                                True, True)
            power_up = pygame.sprite.spritecollideany(self.stage.objects['player'][0].sprites()[0], self.stage.objects['deads'][0])
            if power_up:
                self.stage.objects['player'][0].stats.power_up += 1
                power_up.kill()
            for arrow in deaths:
                for dead in deaths[arrow]:
                    self.stage.objects['deads'][0].died(dead)
                    self.stage.objects['player'][0].stats.kills += 1


class MenuRender(pygame.Surface):
    def __init__(self, menu):
        super().__init__(menu.size)
        self.is_running = True
        self.is_paused = False
        main_logger.succes('MenuRender init : OK')
        self.menu = menu
        main_logger.succes('Load Menu Object : OK')
        self.blit(self.menu.image, (0, 0))
        main_logger.succes('Display main menu : OK')

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX = event.pos[0] - self.menu.menu_body.rect.x - self.menu.item_boxes[0].rect.x
            posY = event.pos[1] - self.menu.menu_body.rect.y - self.menu.item_boxes[0].rect.y
            event_logger.debug(f'click : {posX}, {posY}')
            for box in self.menu.item_boxes:
                for button in box.items:
                    event_logger.debug(f'hitbox rect : {button.rect}')
                    event_logger.debug(f'collidepoint : {button.rect.collidepoint(event.pos)}')
                    if button.rect.collidepoint((posX, posY)):
                        self.menu.click_down(button)

        elif event.type == pygame.MOUSEBUTTONUP:
            posX = event.pos[0] - self.menu.menu_body.rect.x - self.menu.item_boxes[0].rect.x
            posY = event.pos[1] - self.menu.menu_body.rect.y - self.menu.item_boxes[0].rect.y
            event_logger.debug(f'click : {posX}, {posY}')
            for box in self.menu.item_boxes:
                for button in box.items:
                    event_logger.debug(f'hitbox rect : {button.rect}')
                    event_logger.debug(f'collidepoint : {button.rect.collidepoint(event.pos)}')
                    if button.rect.collidepoint((posX, posY)):
                        self.menu.click_up(button)

    def update(self):
        self.menu.update()
        self.blit(self.menu.image, (0, 0))














