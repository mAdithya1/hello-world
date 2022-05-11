import pygame, sys

pygame.init()

win = pygame.display.set_mode((600,600))
pygame.display.set_caption('Hello Title')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    win.fill((255,255,255))
    pygame.display.update()
    
