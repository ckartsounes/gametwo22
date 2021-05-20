import pygame
from pygame.locals import *
from random import randint
from pygame import Vector2
from sys import exit

SCREENW = 640
SCREENH = 480
GRAV = 600


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



class AstroidSprite(pygame.sprite.Sprite):
    PW = None
    PH = None

    def __init__(self, loc, im):
        super().__init__()
        self.damage = 1

    def update(self):
        #goes down
        pass



resourcesS = 'resources//'
netim = pygame.image.load(resourcesS + "net.png")
brickim = pygame.image.load(resourcesS + "spongehead.png")
background_image_filename = resourcesS + 'spongebobback.png'
sprite_image_filename = resourcesS + 'jellyfishy.png'

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load(resourcesS + "bubbles.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play()
pygame.display.set_caption("Keep the jellyfish from reaching the ground!")

b5blaster = pygame.mixer.Sound(resourcesS + "boing.wav")
msg = "Jellyfish Wrangler! Click to Play!"
my_font = pygame.font.SysFont("arial", 32)
splash = my_font.render(msg, True, (0, 0, 0), (200, 10, 150))
splashrect = splash.get_rect()
splashrect.center = (SCREENW / 2, SCREENH / 2)

x, y = SCREENW/2, SCREENH-50
move_x, move_y = 0, 0

screen = pygame.display.set_mode((640, 480), 0, 32)
screen.blit(splash, splashrect.topleft)
background = pygame.image.load(background_image_filename).convert()
spriteim = pygame.image.load(sprite_image_filename).convert_alpha()
clock = pygame.time.Clock()
paddle_group = pygame.sprite.Group()
paddle_group.add()

font = pygame.font.Font('freesansbold.ttf', 32)
global score
score = 0

showSplash = True
while showSplash:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            showSplash = False
    pygame.display.update()

screen.blit(background, (0, 0))

all_sprites = pygame.sprite.Group()
all_sprites.add(AstroidSprite((100,100), ))
screen.blit(background, (0, 0))

player = PlayerSprite((x, y), netim)

player_group = pygame.sprite.Group()
player_group.add(player)

Fullscreen = False
loop = True

while loop:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT or len(all_sprites) == 0:
            pygame.mixer.quit()
            loop = False
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mixer.quit()
                pygame.quit()
            if Fullscreen:
                screen = pygame.display.set_mode((640, 400), 0, 32)
        if event.type == KEYDOWN:
            if event.key == K_f and (event.mod & pygame.KMOD_SHIFT):
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((640, 500), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((640, 500), 0, 32)
            elif event.type == MOUSEBUTTONDOWN:
                newsq = AstroidSprite(spriteim, pygame.mouse.get_pos())
                all_sprites.add(newsq)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 2
    if keys[pygame.K_RIGHT]:
        x += 2
    if keys[pygame.K_UP]:
        y -= 2
    if keys[pygame.K_DOWN]:
        y += 2
    player.update(x, y)
    player_group.draw(screen)

    time_passed = clock.tick(120)
    time_passed_seconds = time_passed / 1000.0

    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(font.render(str(score), False, (0, 0, 0)), (0, 0))
    screen.blit(font.render("Lives: " + str(len(all_sprites)), False, (0, 0, 0)), (SCREENW-175, 0))
    pygame.display.update()

    if score % 20 == 0 and score != 0:
        score = score + 1
        all_sprites.add(AstroidSprite(spriteim))
        print("Game Over")

    for jellyfish in all_sprites:
        if jellyfish.rect.x >= SCREENW - jellyfish.image.get_width():
            jellyfish.velocity[0] = -jellyfish.velocity[0]
        if jellyfish.rect.x <= 0:
            jellyfish.velocity[0] = -jellyfish.velocity[0]
        if jellyfish.rect.y < -250:
            jellyfish.velocity[1] = -jellyfish.velocity[1]
            jellyfish.bounced = False
        if jellyfish.rect.y > SCREENH:
            all_sprites.remove(jellyfish)
        elif pygame.sprite.collide_mask(jellyfish, player):
            jellyfish.bounce()
