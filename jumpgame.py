import pygame
from pygame.locals import *
from random import randint
from pygame import Vector2
from sys import exit
from PlayerSprite import *
from AstroidSprite import *
from PlatformSprite import *
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

enemy_sprites = pygame.sprite.Group()
screen.blit(background, (0, 0))

platform_group = pygame.sprite.Group()
test = randint(0, SCREENW)

platform = PlatformSprite((SCREENW / 2, SCREENH), platformim)
platform_group.add(platform)

layer = SCREENH-75
for x in range(0, 9):
    platform = PlatformSprite((randint(0, SCREENW), randint(layer, layer+75)), platformim)
    platform_group.add(platform)
    layer -= 75

player = PlayerSprite((SCREENW / 2, SCREENH - platform.PH), playerim)
player_group = pygame.sprite.Group()
player_group.add(player)

Fullscreen = False
loop = True

while loop:
    screen.blit(background, (0, 0))
    if player.life <= 0:
        pygame.mixer.quit()
        loop = False
        pygame.quit()
        exit()
    for event in pygame.event.get():
        if event.type == QUIT:
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

    global SCORE
    screen.blit(font.render(("Score: " + str(SCORE)), False, (0, 0, 0)), (0, 0))
    screen.blit(font.render(("Lives: " + str(player.life)), False, (0, 0, 0)), (SCREENW-125, 0))

    if player.addpoint:
        SCORE += 1
    if SCORE % 5 == 0 and SCORE != 0 and spawnAstroid:
        enemy_sprites.add(AstroidSprite((randint(0, SCREENW), -enemyim.get_height()-75), enemyim))
        spawnAstroid = False
    elif SCORE % 6 == 0:
        spawnAstroid = True

    testcollision = False
    for plat in platform_group:
        if plat.rect.centery == SCREENH:
            platform_group.add(PlatformSprite((randint(0, SCREENH), randint(layer, layer + 75)), platformim))
            platform_group.remove(plat)
        if pygame.sprite.collide_mask(plat, player):
            testcollision = True

    player.colliding(testcollision)

    for enemy in enemy_sprites:
        if pygame.sprite.collide_mask(enemy, player):
            enemy_sprites.remove(enemy)
            player.life -= 1

    player.update()
    player_group.draw(screen)
    platform_group.update(player.jumped)
    platform_group.draw(screen)
    enemy_sprites.update()
    enemy_sprites.draw(screen)
    pygame.display.update()
