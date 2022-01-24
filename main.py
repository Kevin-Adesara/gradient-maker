import pygame
from pygame.locals import *
pygame.init()
size=(1366,768)
fullscreen=False
win=pygame.display.set_mode(size,RESIZABLE|SCALED)
def blit_text(text,size,color,pos):
    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(text, True, color)
    win.blit(textsurface,pos)

def redrawwin(win):
    win.fill((255,255,255))
    blit_text("Hello world",100,(255,0,0),(0,0))
    pygame.display.update()

while True:    
    redrawwin(win)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                quit()
            if event.key==K_f:
                if not fullscreen:
                    pygame.display.set_mode(size,FULLSCREEN)
                if fullscreen:
                    pygame.display.set_mode(size,RESIZABLE|SCALED)
                fullscreen=not fullscreen
        if event.type==pygame.QUIT:
            quit()