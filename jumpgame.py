import pygame
from pygame.locals import *
from random import randint
from pygame import Vector2
from sys import exit
from PlayerSprite import *
from AstroidSprite import *
from PlatformSprite import *
from LavaSprite import *
from Resources import *
from GlobalVariables import *

screen.blit(splash, splashrect.topleft)
clock = pygame.time.Clock()
paddle_group = pygame.sprite.Group()
paddle_group.add()

font = pygame.font.Font('freesansbold.ttf', 32)

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
all_sprites.add(AstroidSprite((100, 100), spriteim))
screen.blit(background, (0, 0))

platform_group = pygame.sprite.Group()
platform = PlatformSprite((SCREENW / 2, SCREENH), platformim)
platform2 = PlatformSprite((SCREENW / 2 + 100, SCREENH / 2 + 200), platformim)
platform3 = PlatformSprite((SCREENW / 2 - 100, SCREENH / 2 + 200), platformim)
platform4 = PlatformSprite((SCREENW / 2, SCREENH / 2 + 100), platformim)
platform5 = PlatformSprite((SCREENW / 2 + 100, SCREENH / 2 + 10), platformim)
platform6 = PlatformSprite((SCREENW / 2 - 100, SCREENH / 2 + 10), platformim)
platform7 = PlatformSprite((SCREENW / 2 - 200, SCREENH / 2 + 100), platformim)
platform8 = PlatformSprite((SCREENW / 2 - 200, SCREENH), platformim)
platform9 = PlatformSprite((SCREENW / 2 + 200, SCREENH), platformim)
platform10 = PlatformSprite((SCREENW / 2 + 200, SCREENH / 2 + 100), platformim)
platform11 = PlatformSprite((SCREENW / 2 + 200, SCREENH / 2 - 100), platformim)
platform12 = PlatformSprite((SCREENW / 2 - 200, SCREENH / 2 - 100), platformim)
platform13 = PlatformSprite((SCREENW / 2, SCREENH / 2 - 100), platformim)
platform_group.add(platform, platform2, platform3, platform4, platform5, platform6, platform7, platform8, platform9,
                   platform10, platform11, platform12, platform13)

player = PlayerSprite((SCREENW / 2, SCREENH - platform.PH), netim)
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
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mixer.quit()
                pygame.quit()
            if Fullscreen:
                screen = pygame.display.set_mode((640, 400), 0, 32)
            if event.key == K_f and (event.mod & pygame.KMOD_SHIFT):
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((640, 500), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((640, 500), 0, 32)
            elif event.type == MOUSEBUTTONDOWN:
                pass

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    if keys[pygame.K_UP]:
        player.jump()

    time_passed = clock.tick(120)
    time_passed_seconds = time_passed / 1000.0

    screen.blit(font.render(str(SCORE), False, (0, 0, 0)), (0, 0))

    testcollision = False
    for plat in platform_group:
        if pygame.sprite.collide_mask(plat, player):
            testcollision = True
    player.colliding(testcollision)

    player.update()
    player_group.draw(screen)
    platform_group.update()
    platform_group.draw(screen)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
