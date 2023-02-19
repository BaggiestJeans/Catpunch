import os
import pygame
from fig1 import Fighter
import time
import sys
pygame.joystick.init()
pygame.init()
def base(player):
    SW=1080
    SH=720
    ratio=SW/SH
    FLOOR=SH/10
    screen=pygame.display.set_mode((SW,SH))
    clock=pygame.time.Clock()

    pygame.display.set_caption("Game")
    bg_image=pygame.image.load("Capture2.png").convert_alpha()
    title=pygame.image.load("title.png").convert_alpha()
    sheet1=pygame.image.load("cat6.png").convert_alpha()
    sheet2=pygame.image.load("cat7.png").convert_alpha()
    thumbs=pygame.image.load("thumbs.png").convert_alpha()

    # icon=pygame.image.load("0001.png")
    # pygame.display.set_icon(icon)
    font=pygame.font.Font("joystix.ttf",80)
    score=pygame.font.Font("joystix.ttf",20)

    step1=[4,8,8,10,7,7,6,13,13,10,9,8,8,8,6]
    size=64
    scale=5
    offset=[25,18]
    data1=[size,scale,offset]
    step2=[2,10,7]

    ic=3
    ic2=5
    lcu=pygame.time.get_ticks()
    lcu2=pygame.time.get_ticks()


    # fig1=Fighter(1,200,SH-290,data1,sheet1,step1)
    if player==1:
        fig1=Fighter(1,200,SH-290,data1,sheet1,step1)
        fig2=Fighter(2,SW-280,SH-290,data1,sheet2,step1)
    if player==2:
        fig1=Fighter(1,200,SH-290,data1,sheet1,step1)
        fig2=Fighter(3,SW-280,SH-290,data1,sheet2,step1)
    # fig3=Fighter(3,700,SH-290,data1,sheet1,step1)
    def draw_text(text,font,text_col,x,y):
        img=font.render(text,True,text_col)
        screen.blit(img,(x,y))

    def draw_bg():
        scaled_bg=pygame.transform.scale(bg_image,(SW,SH))
        screen.blit(scaled_bg,(0,0))
        pygame.draw.rect(screen, (0,150,0),(0,SH-110,SW,110))

    def dhb(hp,x,y,player):
        if player==1:
            pygame.draw.rect(screen, (255,255,0),(x,y,400,30))
            pygame.draw.rect(screen, (0,0,255),(x,y,(400*(hp/100)),30))
        elif player==2:
            pygame.draw.rect(screen, (0,0,255),(x,y,400,30))
            pygame.draw.rect(screen, (255,255,0),(x,y,(-1*(hp-100)/100)*400,30))
            # pygame.draw.rect(screen, (255,255,0),(x,y,400,30))
            # pygame.draw.rect(screen, (0,0,255),(x,y,(400*(hp/100)),30))

    def draw_title():
        scaled_title=pygame.transform.scale(title,(SW/2,SH-100))
        screen.blit(scaled_title,(SW/4,0))
    pause=False
    run=True
    while run:
        clock.tick(60)
        draw_bg()
        dhb(fig1.hp,20,20,1)
        draw_text(str(fig1.hp),score,(200,0,0),(30),60)
        dhb(fig2.hp,SW-420,20,2) 
        draw_text(str(fig2.hp),score,(200,0,0),(SW-70),60)
        if ic<=0 and pause==False:
            fig1.move(SW,SH,screen,fig2)
            fig2.move(SW,SH,screen,fig1)

        else:
            draw_text(str(ic),font,(200,0,0),(SW/2.1),SH/3)
            if pygame.time.get_ticks()-lcu>=1000:
                ic-=1
                lcu=pygame.time.get_ticks()

                
        fig1.update()
        fig1.draw(screen)
        fig2.draw(screen)
        fig2.update()
        if fig2.hp<=0:
                screen.blit(thumbs,(0,0))
                draw_text("player1 wins",font,(200,0,0),(SW/5),SH/3)
                if ic2<=0:
                    run=False
                if pygame.time.get_ticks()-lcu2>=1000:
                    lcu2=pygame.time.get_ticks()
                    ic2-=1
                    lcu2=pygame.time.get_ticks()
        if fig1.hp<=0:
                screen.blit(thumbs,(0,0))
                draw_text("player2 wins",font,(200,0,0),(SW/5),SH/3)
                if ic2<=0:
                    run=False
                if pygame.time.get_ticks()-lcu2>=1000:
                    lcu2=pygame.time.get_ticks()
                    ic2-=1
                    lcu2=pygame.time.get_ticks()
    
        for event in pygame.event.get():
                    
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
                    
                    
            if event.type == pygame.QUIT:
                sys.exit()
            
        
        pygame.display.update()
