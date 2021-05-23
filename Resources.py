import pygame
from GlobalVariables import *

resourcesS = 'resources//'
playerim = pygame.image.load(resourcesS + "playerimg.png")
enemyim = pygame.image.load(resourcesS + "asteroidimg.png")
platformim = pygame.image.load(resourcesS + "platformimg.png")
jumpim = pygame.image.load(resourcesS + "jumpimg.png")
leftim = pygame.image.load(resourcesS + "leftimg.png")
rightim = pygame.image.load(resourcesS + "rightimg.png")
bulletim = pygame.image.load(resourcesS + "bulletimg.png")
# holeim = pygame.image.load(resourcesS + "")
background_image_filename = resourcesS + 'backgroundimg.png'
sprite_image_filename = resourcesS + 'playerimg.png'
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREENW, SCREENH), 0, 32)
pygame.mixer.music.load(resourcesS + "bubbles.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play()
pygame.display.set_caption("Shoot all 50 falling enemies to win the game")
jumpsound = pygame.mixer.Sound(resourcesS + "jump.wav")
# shootsound = pygame.mixer.Sound(resourcesS + "shoot.wav")
# hitsound = pygame.mixer.Sound(resourcesS + "hit.wav")
# diesound = pygame.mixer.Sound(resourcesS + "gameover.wav")
msg = "Lecture Survivor! Click to Play!"
msg2 = "YOU DIED!"
my_font = pygame.font.SysFont("arial bold", 32)
splash = my_font.render(msg, True, (0, 0, 0), (255, 0, 0))
splash2 = my_font.render(msg2, True, (250, 0, 0), (0, 0, 0))
splashrect = splash.get_rect()
splashrect.center = (SCREENW / 2, SCREENH / 2)
background = pygame.image.load(background_image_filename).convert()
spriteim = pygame.image.load(sprite_image_filename).convert_alpha()
