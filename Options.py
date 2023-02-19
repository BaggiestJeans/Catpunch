import pygame
import sys
pygame.init()
def base():
    SW=1080
    SH=720

    screen=pygame.display.set_mode((SW,SH))
    clock=pygame.time.Clock()

    pygame.display.set_caption("Options")

    soundimg=pygame.image.load("Sound.png").convert_alpha()
    class Button():
        def __init__(self,x,y,image,scale):
            width=image.get_width()
            height=image.get_height()
            self.image=pygame.transform.scale(image,(int(width/scale),int(height/scale)))
            self.rect=self.image.get_rect()
            self.rect.center=(x,y)
            self.click=False
            self.type=image
        def draw(self,x,y):
            pos=pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()==(1,0,0) and self.click==False:
                    if self.type==soundimg:
                        print("balls")
                        self.click=True
            if pygame.mouse.get_pressed()==(0,0,0):
                self.click=False
            screen.blit(self.image,(self.rect.x,self.rect.y))
    sound=Button((SW/2),(SH/3),soundimg,10)
    run=True
    while run:
        clock.tick(60)
        screen.fill((100,1,0))
        sound.draw((SW/2),SH/2)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        run=False
        pygame.display.update()
