import pygame, sys
from pygame.locals import QUIT
from ball import Ball

pygame.init()

FPS = 30
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Balls")
clock = pygame.time.Clock()
active = True

#game constants
GRAVITY = 9.8

#colors
TURQUOISE = (64,224,208)
VIOLET = (143, 0, 255)

ballList = [\
    Ball(SCREEN_WIDTH, SCREEN_HEIGHT, 250, 50, 30, 100, TURQUOISE, FPS, GRAVITY), \
    #Ball(SCREEN_WIDTH, SCREEN_HEIGHT, 20, 70, 20, 100, TURQUOISE, FPS, GRAVITY), \
    #Ball(SCREEN_WIDTH, SCREEN_HEIGHT, 200, 100, 40, 200, TURQUOISE, FPS, GRAVITY), \
]


while active:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            active = False

    SCREEN.fill(VIOLET)
    
    for ball in ballList:
        ball.draw(SCREEN)
    
    for ball in ballList:
        ball.update()

    pygame.display.update()

pygame.quit()
sys.exit()