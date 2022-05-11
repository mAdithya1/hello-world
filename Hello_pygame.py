import pygame, sys

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((600,600))

f = pygame.font.SysFont(None, 55)
def fun(text, color, x, y):
    t = f.render(text, True, color)
    win.blit(t, [x, y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    win.fill((255,255,255))
    fun('Hello World', (255,0,0), 200, 200)
    pygame.display.update()
