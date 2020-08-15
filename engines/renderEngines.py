from objects.menus import *


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.INFO)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)

class StageRender(pygame.Surface):
    def __init__(self, stage_scene, size=settings.SCREEN_SIZE):
        super().__init__(size)
        self.is_running = True
        self.is_paused = False
        self.scene = stage_scene
        self.update()
        display_logger.success('stageRender init: OK')

    def reset(self, stage_scene, hero, size=settings.SCREEN_SIZE):
        try:
            self.scene.reset(stage_scene.level, hero)
            super().__init__(size)
            self.is_running = True
            self.update()
            display_logger.success(f'StageRender reset to level : {self.scene.level}')
        except:
            display_logger.exception('StageRender reset failled')

    def update(self):
        if self.is_running is True:
            if self.scene.is_running:
                self.scene.topbar.update()
                self.blit(self.scene.background, (0, 0))
                self.blit(self.scene.topbar.image, (0, 0))
                if self.scene.intro.is_running:
                    self.scene.intro.update()
                    for object in self.scene.objects:
                        for elem in self.scene.objects[object]:
                            for sprite in elem.sprites():
                                self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))
                    self.blit(self.scene.intro.image, self.scene.intro.rect)
                elif self.scene.outro.is_running:
                    self.scene.outro.update()
                    for object in self.scene.objects:
                        for elem in self.scene.objects[object]:
                            for sprite in elem.sprites():
                                self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))
                    self.blit(self.scene.outro.image, self.scene.outro.rect)
                elif self.scene.hero.kills == self.scene.level.total_unit:
                    self.scene.outro.chose_ending('win')
                    self.scene.outro.is_running = True
                else:
                    self.scene.update()
                    self._collisionHandler()
                    for object in self.scene.objects:
                        for elem in self.scene.objects[object]:
                            elem.update()
                            for sprite in elem.sprites():
                                self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))
            else:
                self.is_running = False

    def handleEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_paused = True
                event_logger.success(f"Event 'PauseMenu' received... Setting stage.is_paused to True")
            self.scene.objects['shots'][0].fireShot(self.scene.objects['player'][0].sprites()[0].rect, event)
        if self.scene.outro.is_running:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.scene.outro.is_running:
                    posX = event.pos[0] - self.scene.outro.rect.x - self.scene.outro.buttons.rect.x
                    posY = event.pos[1] - self.scene.outro.rect.y - self.scene.outro.buttons.rect.y
                    event_logger.debug(f'click : {posX}, {posY}')
                    for button in self.scene.outro.buttons.items:
                        event_logger.debug(f'hitbox rect : {button.rect}')
                        event_logger.debug(f'collidepoint : {button.rect.collidepoint(event.pos)}')
                        if button.rect.collidepoint((posX, posY)):
                            self.scene.outro.click_down(button)
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.scene.outro.is_running:
                    posX = event.pos[0] - self.scene.outro.rect.x - self.scene.outro.buttons.rect.x
                    posY = event.pos[1] - self.scene.outro.rect.y - self.scene.outro.buttons.rect.y
                    event_logger.debug(f'click : {posX}, {posY}')
                    for button in self.scene.outro.buttons.items:
                        event_logger.debug(f'hitbox rect : {button.rect}')
                        event_logger.debug(f'collidepoint : {button.rect.collidepoint(event.pos)}')
                        if button.rect.collidepoint((posX, posY)):
                            self.scene.outro.click_up(button)

    def _collisionHandler(self):
        for enemies in self.scene.objects['enemies']:
            if pygame.sprite.spritecollideany(self.scene.objects['player'][0].sprites()[0], enemies):
                self.scene.outro.is_running = True
                self.scene.outro.chose_ending('lose')
            deaths = pygame.sprite.groupcollide(self.scene.objects['shots'][0],
                                                enemies,
                                                True, True)
            power_up = pygame.sprite.spritecollideany(self.scene.objects['player'][0].sprites()[0], self.scene.objects['deads'][0])
            if power_up:
                self.scene.hero.power_up += 1
                power_up.kill()
            for arrow in deaths:
                for dead in deaths[arrow]:
                    self.scene.objects['deads'][0].died(dead)
                    self.scene.hero.kills += 1


class MenuRender(pygame.Surface):
    def __init__(self, menu):
        super().__init__(menu.size)
        self.is_running = True
        self.is_paused = False
        self.scene = menu
        self.blit(self.scene.image, (0, 0))
        display_logger.success('menuRender init: OK')

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if type(self.scene) == HeroMenuScene:
                posX = event.pos[0] - self.scene.menu_body.rect.x - self.scene.item_boxes[0].rect.x
                posY = event.pos[1] - self.scene.menu_body.rect.y - self.scene.item_boxes[0].rect.y
                rect_logger.debug(f'menu-body : ({self.scene.menu_body.rect.x}; eventX : {event.pos[0]} posX : {posX}')
                rect_logger.debug(f'{self.scene.item_boxes[0].name} : {self.scene.item_boxes[0].rect.x}; posX : {posX}')
                self.scene.search_itembox('Datas')
                posX -= self.scene.targetbox.rect.x
                posY -= self.scene.targetbox.rect.y
                rect_logger.debug(f'{self.scene.targetbox.name} : {self.scene.targetbox.rect.x}; posX : {posX}')
                self.scene.search_itembox('PowerUps')
                posX -= self.scene.targetbox.rect.x
                posY -= self.scene.targetbox.rect.y
                rect_logger.debug(f'{self.scene.targetbox.name} : {self.scene.targetbox.rect.x}; posX : {posX}')
                rect_logger.debug(f'Target Box = {self.scene.targetbox.name} : {[item.name for item in self.scene.targetbox.items]}')
                for box in self.scene.targetbox.items[2:]:
                    rect_logger.debug(f'box {box.name} - rect: {box.rect} ')
                    for item in box.items:
                        rect_logger.debug(f'item {item.name} - rect: {item.rect},  posX : {posX}-{item.rect.x}-{box.rect.x} = {posX-item.rect.x-box.rect.x} ')
                        rect_logger.debug(f'item {item.name} - rect: {item.rect},  posY : {posY}-{item.rect.y}-{box.rect.y} = {posY-item.rect.y-box.rect.y} ')
                        if type(item) == ItemBox:
                            tmp_posX = posX
                            tmp_posX -= item.rect.x
                            tmp_posX -= box.rect.x
                            tmp_posY = posY
                            tmp_posY -= item.rect.y
                            tmp_posY -= box.rect.y
                            for button in item.items:
                                rect_logger.debug(f'button {button.name} - rect: {button.rect} ')
                                if button.rect.collidepoint((tmp_posX, tmp_posY)):
                                    self.scene.click_down(button)
                                    rect_logger.success(f'is_collide : {button.rect.collidepoint((tmp_posX, tmp_posY))}')
                posX = event.pos[0] - self.scene.menu_body.rect.x - self.scene.item_boxes[0].rect.x
                posY = event.pos[1] - self.scene.menu_body.rect.y - self.scene.item_boxes[0].rect.y
                self.scene.search_itembox('Buttons')
                posX -= self.scene.targetbox.rect.x
                posY -= self.scene.targetbox.rect.y
                for button in self.scene.targetbox.items:
                    if button.rect.collidepoint((posX, posY)):
                        self.scene.click_down(button)
                        main_logger.debug(f'scene.hero.stats : {self.scene.hero.datas}')

            else:
                posX = event.pos[0] - self.scene.menu_body.rect.x - self.scene.item_boxes[0].rect.x
                posY = event.pos[1] - self.scene.menu_body.rect.y - self.scene.item_boxes[0].rect.y
                event_logger.debug(f'click : {posX}, {posY}')
                for box in self.scene.item_boxes:
                    for button in box.items:
                        event_logger.debug(f'hitbox rect : {button.rect}')
                        event_logger.debug(f'collidepoint : {button.rect.collidepoint(event.pos)}')
                        if button.rect.collidepoint((posX, posY)):
                            self.scene.click_down(button)

        elif event.type == pygame.MOUSEBUTTONUP:
            if type(self.scene) == HeroMenuScene:
                posX = event.pos[0] - self.scene.menu_body.rect.x - self.scene.item_boxes[0].rect.x
                rect_logger.debug(f'menu-body : ({self.scene.menu_body.rect.x}; eventX : {event.pos[0]} posX : {posX}')
                rect_logger.debug(f'{self.scene.item_boxes[0].name} : {self.scene.item_boxes[0].rect.x}; posX : {posX}')
                self.scene.search_itembox('Datas')
                posX -= self.scene.targetbox.rect.x
                rect_logger.debug(f'{self.scene.targetbox.name} : {self.scene.targetbox.rect.x}; posX : {posX}')
                self.scene.search_itembox('PowerUps')
                posX -= self.scene.targetbox.rect.x
                rect_logger.debug(f'{self.scene.targetbox.name} : {self.scene.targetbox.rect.x}; posX : {posX}')
                posY = event.pos[1] - self.scene.menu_body.rect.y - self.scene.item_boxes[0].rect.y
                self.scene.search_itembox('Datas')
                posY -= self.scene.targetbox.rect.y
                self.scene.search_itembox('PowerUps')
                posY -= self.scene.targetbox.rect.y
                rect_logger.debug(
                    f'Target Box = {self.scene.targetbox.name} : {[item.name for item in self.scene.targetbox.items]}')
                for box in self.scene.targetbox.items[2:]:
                    rect_logger.debug(f'box {box.name} - rect: {box.rect} ')
                    for item in box.items:
                        rect_logger.debug(
                            f'item {item.name} - rect: {item.rect},  posX : {posX}-{item.rect.x}-{box.rect.x} = {posX - item.rect.x - box.rect.x} ')
                        rect_logger.debug(
                            f'item {item.name} - rect: {item.rect},  posY : {posY}-{item.rect.y}-{box.rect.y} = {posY - item.rect.y - box.rect.y} ')
                        if type(item) == ItemBox:
                            tmp_posX = posX
                            tmp_posX -= item.rect.x
                            tmp_posX -= box.rect.x
                            tmp_posY = posY
                            tmp_posY -= item.rect.y
                            tmp_posY -= box.rect.y
                            for button in item.items:
                                rect_logger.debug(f'button {button.name} - rect: {button.rect} ')
                                if button.rect.collidepoint((tmp_posX, tmp_posY)):
                                    self.scene.click_up(button)
                                    rect_logger.success(
                                        f'is_collide : {button.rect.collidepoint((tmp_posX, tmp_posY))}')
                            posX = event.pos[0] - self.scene.menu_body.rect.x - self.scene.item_boxes[0].rect.x
                            posY = event.pos[1] - self.scene.menu_body.rect.y - self.scene.item_boxes[0].rect.y
                            self.scene.search_itembox('Buttons')
                            posX -= self.scene.targetbox.rect.x
                            posY -= self.scene.targetbox.rect.y
                            for button in self.scene.targetbox.items:
                                if button.rect.collidepoint((posX, posY)):
                                    self.scene.click_up(button)
            else:
                posX = event.pos[0] - self.scene.menu_body.rect.x - self.scene.item_boxes[0].rect.x
                posY = event.pos[1] - self.scene.menu_body.rect.y - self.scene.item_boxes[0].rect.y
                event_logger.debug(f'click : {posX}, {posY}')
                for box in self.scene.item_boxes:
                    for button in box.items:
                        event_logger.debug(f'hitbox rect : {button.rect}')
                        event_logger.debug(f'collidepoint : {button.rect.collidepoint(event.pos)}')
                        if button.rect.collidepoint((posX, posY)):
                            self.scene.click_up(button)

    def update(self):
        self.scene.update()
        self.blit(self.scene.image, (0, 0))














