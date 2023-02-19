import gym
import pygame 
import os
SW=1080
SH=720
FLOOR=SH/10
screen=pygame.display.set_mode((SW,SH))
clock=pygame.time.Clock()
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
                "fart"
            if pygame.mouse.get_pressed()==(0,0,0):
                self.click=False
        screen.blit(self.image,(self.rect.x,self.rect.y))

class Menu():
    def __init__(self):
        title=pygame.image.load("title.png").convert_alpha()
        bg_image=pygame.image.load("Untitled.png").convert_alpha()
        playimg=pygame.image.load("play.png").convert_alpha()
        aimg=pygame.image.load("AI.png").convert_alpha()
        tuimg=pygame.image.load("Tutorial.png").convert_alpha()
        optimg=pygame.image.load("options.png").convert_alpha()
        font=pygame.font.Font("joystix.ttf",80)