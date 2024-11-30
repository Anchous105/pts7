import pygame

from classes import *
from random import *
pygame.init()

clock=pygame.time.Clock()
new_drop=pygame.USEREVENT
pygame.time.set_timer(new_drop,500)


mets=pygame.sprite.Group()    #группа спрайтов
def createDrop(g):
    x=randint(50,950)
    speed=randint(1,5)
    return Drop(x,speed,g)

# for i in range(120):
#     createDrop(mets)

H=1000
W=1000
win=pygame.display.set_mode((W,H))

ufo=pygame.image.load('IMAGES//ufo.png')
ufo=pygame.transform.scale(ufo, (60,60))
ufo_rect=ufo.get_rect(center=(400,800))



while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            quit()

        if i.type==pygame.USEREVENT:
            createDrop(mets)

    pos=pygame.mouse.get_pos()
    ufo_rect.center=pos
    for i in mets:
        if ufo_rect.collidepoint(i.rect.center):
            quit()

    win.fill((135,206,235))
    mets.draw(win)
    mets.update()


    win.blit(ufo,ufo_rect)
    pygame.display.update()
    # clock.tick(60)