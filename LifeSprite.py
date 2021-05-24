from Resources import *


class LifeSprite(pygame.sprite.Sprite):
    PW = None
    PH = None

    def __init__(self, loc):
        super().__init__()
        self.PW = lifeim.get_width()
        self.PH = lifeim.get_height()
        self.image = lifeim
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.rect.centery -= self.PH/2
        self.rect.centerx -= self.PW / 2
        self.mask = pygame.mask.from_surface(self.image)

        self.life = 1

    def update(self, val):
        if val:
            self.rect.centery += 1
