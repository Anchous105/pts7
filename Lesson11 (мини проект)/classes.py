import pygame

class Drop(pygame.sprite.Sprite):
    def __init__(self,x,speed,group):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("IMAGES/img_3.png")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect(center=(x,0))
        self.speed=speed
        self.add(group)
    def update(self):
        self.rect.y+=self.speed


