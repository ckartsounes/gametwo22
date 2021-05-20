import pygame
class PlayerSprite(pygame.sprite.Sprite):
    PW = None
    PH = None

    def __init__(self, loc, im):
        super().__init__()
        self.PW = im.get_width()
        self.PH = im.get_height()
        self.image = im
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.mask = pygame.mask.from_surface(self.image)
        self.movingLeft = True

    def update(self, pointx, pointy):
        self.rect.centerx = pointx
        self.rect.centery = pointy

    def jump(self):
        pass

    def shoot(self):pass
