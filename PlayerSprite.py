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
        self.rect.centery -= self.PH/2
        self.rect.centerx -= self.PW / 2
        self.mask = pygame.mask.from_surface(self.image)
        self.movingLeft = True
        self.x = loc[0]
        self.y = loc[1]
        self.jumped = False
        self.jumphight = 150
        self.jumpnow = 0
        self.fell = False

    def moveRight(self):
        self.rect.centerx += 1

    def moveLeft(self):
        self.rect.centerx -= 1

    def update(self):
        if self.jumpnow == self.jumphight:
            self.jumped = False

        if self.jumped == True:
            self.rect.centery -= 1
            self.jumpnow += 1
        elif self.fell == True:
            self.rect.centery += 1
        elif self.fell == False:
            if self.jumpnow > 0:
                self.jumpnow -= 1

    #this is a test

    def falling(self):
        self.fell = True

    def standing(self):
        self.fell = False

    def jump(self):
        if self.jumpnow == 0:
            self.jumped = True

    def shoot(self):
        pass
