import os
import pygame
from Player import Fighter
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
    sheet1=pygame.image.load("cat6.png").convert_alpha()
    sheet2=pygame.image.load("cat7.png").convert_alpha()
    thumbs=pygame.image.load("thumbs.png").convert_alpha()
    font=pygame.font.Font("joystix.ttf",80)
    score=pygame.font.Font("joystix.ttf",20)
    def keybind():
        key=pygame.key.get_pressed()
        moves1=[key[pygame.K_w],key[pygame.K_a],key[pygame.K_d],key[pygame.K_r],key[pygame.K_t],key[pygame.K_c]]#jump,left,right,attack1,attack2,block
    step1=[4,8,8,10,7,7,6,8,13,10,9,8,8,8,6]
    size=64
    scale=5
    offset=[25,18]
    data1=[size,scale,offset]
    scores=[]
    ic=3
    oc=5
    lcu=pygame.time.get_ticks()
    lcu2=pygame.time.get_ticks()

    fig1=Fighter(1,200,SH-290,data1,sheet1,step1)
    fig2=Fighter(player,SW-280,SH-290,data1,sheet2,step1)
    fighters=[fig1,fig2]
    # fig1=Fighter(1,200,SH-290,data1,sheet1,step1)
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
            pygame.draw.rect(screen, (0,199,200),(x,y,(400*(hp/100)),30))
        elif player==2:
            pygame.draw.rect(screen, (0,199,200),(x,y,400,30))
            pygame.draw.rect(screen, (255,255,0),(x,y,(-1*(hp-100)/100)*400,30))
            # pygame.draw.rect(screen, (255,255,0),(x,y,400,30))
            # pygame.draw.rect(screen, (0,0,255),(x,y,(400*(hp/100)),30))

    pause=False
    run=True
    while run:
        clock.tick(60)
        draw_bg()
        dhb(fig1.hp,20,20,1)
        draw_text(str(fig1.hp),score,(200,0,0),(30),60)
        dhb(fig2.hp,SW-420,20,2) 
        draw_text(str(fig2.hp),score,(200,0,0),(SW-70),60)
        if ic<=0 :
            fig1.move(SW,SH,screen,fig2)
            fig2.move(SW,SH,screen,fig1)

        else:
            draw_text(str(ic),font,(200,0,0),(SW/2.1),SH/3)
            if pygame.time.get_ticks()-lcu>=1000:
                ic-=1
                lcu=pygame.time.get_ticks()

        for p in range(len(fighters)):
            fighters[p].draw(screen)
            fighters[p].update()

            if fighters[p].hp<=0 and oc>=0:
                screen.blit(thumbs,(0,0))
                draw_text("Player "+str(p)+" wins",font,(200,0,0),(SW/5),SH/3)
                if oc<=0:
                        run=False
                        
                if pygame.time.get_ticks()-lcu2>=1000:
                    lcu2=pygame.time.get_ticks()
                    oc-=1
                    lcu2=pygame.time.get_ticks()

        for event in pygame.event.get():                   
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False         
            if event.type == pygame.QUIT:
                sys.exit()
            
        
        pygame.display.update()
