import pygame
import BaseGame
import Online
import AI
import Options
pygame.init()

SW=1080
SH=720
screen=pygame.display.set_mode((SW,SH))
clock=pygame.time.Clock()

pygame.display.set_caption("CATPUNCH")
title=pygame.image.load("title4.png").convert_alpha()
bg_image=pygame.image.load("Untitled.png").convert_alpha()
back=pygame.image.load("bg.png").convert_alpha()
playimg=pygame.image.load("play2.png").convert_alpha()
psimg=pygame.image.load("pselect3.png").convert_alpha()
asimg=pygame.image.load("aselect3.png").convert_alpha()
tsimg=pygame.image.load("tselect.png").convert_alpha()
osimg=pygame.image.load("oselect.png").convert_alpha()
aimg=pygame.image.load("ai2.png").convert_alpha()
tuimg=pygame.image.load("tut2.png").convert_alpha()
optimg=pygame.image.load("opt2.png").convert_alpha()
font=pygame.font.Font("joystix.ttf",80)

def draw_bg():
    scaled_bg=pygame.transform.scale(back,(SW,SH))
    screen.blit(scaled_bg,(0,0))
def draw_title():
    scaled_title=pygame.transform.scale(title,((SW/2),(SH/8)))
    screen.blit(scaled_title,(SW/4,20))
def options():
    screen2=pygame.display.set_mode((SW,SH))
    run2=True
    clock2=pygame.time.Clock()
    draw_bg()
    while run2:
        clock2.tick(60)
        screen2.fill((255,0,219))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2=False

    pygame.display.update()
class Button():
    def __init__(self,x,y,image,scale,select):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width/scale),int(height/scale)))
        self.select=pygame.transform.scale(select,(int(width/scale),int(height/scale)))
        self.hover=False
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.click=False
        self.type=image
    def draw(self,x,y):
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.hover=True
        else:
            self.hover=False
        if pygame.mouse.get_pressed()==(1,0,0) and self.click==False and self.hover==True:
            if self.type==playimg:
                Online.base(2)
                self.click=True
            if self.type==optimg:
                print("options")
                Options.base()
                self.click=True    
            if self.type==tuimg:
                print("Tutorial")
                self.click=True
            if self.type==aimg:
                BaseGame.base(3)
                self.click=True
        if pygame.mouse.get_pressed()==(0,0,0):
            self.click=False
        if self.hover==False:
            screen.blit(self.image,(self.rect.x,self.rect.y))
        if self.hover==True:
            screen.blit(self.select,(self.rect.x,self.rect.y))
        

play=Button((SW/2),(SH/3)-50,playimg,10,psimg)
ai=Button((SW/2),(SH/3)+50,aimg,10,asimg)
tut=Button((SW/2),(SH/3)+150,tuimg,10,tsimg)
opt=Button((SW/2),(SH/3)+250,optimg,10,osimg)
run=True

while run:
    clock.tick(60)
    # screen.fill((255-45,1,219-45))
    screen.fill((255,255,255))
    draw_bg()
    play.draw((SW/2),SH/3.2)
    ai.draw((SW/2),SH/2)
    opt.draw((SW/2),SH/1.5)
    tut.draw((SW/2),SH/1)
    draw_title()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()
