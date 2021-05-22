import pygame
from Resources import *
from GlobalVariables import *
class PlayerSprite(pygame.sprite.Sprite):
    PW = None
    PH = None
    jumped = False
    def __init__(self, loc, im):
        super().__init__()
        self.PW = im.get_width()
        self.PH = im.get_height()
        self.image = im
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.rect.centery -= self.PH/2
        self.rect.centerx -= self.PW / 2
        self.mask = pygame.mask.from_surface(self.image)
        self.movingLeft = True
        self.x = loc[0]
        self.y = loc[1]
        self.jumpheight = 150
        self.jumpnow = 0
        self.fell = False
        self.collide = False
        self.addpoint = False
        self.life = 5
        self.collideWhere = 'None'

    def moveRight(self):
        if self.rect.centerx == SCREENW:
            self.rect.centerx = 0
        self.rect.centerx += 1

    def moveLeft(self):
        if self.rect.centerx == 0:
            self.rect.centerx = SCREENW
        self.rect.centerx -= 1

    def update(self):
        if self.jumped == False and self.collideWhere != 'bottom':
            self.rect.centery += 1
        if self.jumped == True:
            self.rect.centery -= 1
            self.jumpnow += 1
        if self.jumpheight == self.jumpnow:
            self.jumped = False
            self.jumpnow = 0
        if self.rect.centery == SCREENH:
            self.life = 0
        if self.jumpnow == 1:
            self.addpoint = False

    def colliding(self, val, where):
        self.collide = val
        self.collideWhere = where
    def jump(self):
        if self.collide and self.collideWhere == 'bottom' and self.jumpnow == 0:
            self.addpoint = True
            self.jumped = True
            jumpsound.play()

    def shoot(self):
        pass
