import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

SW=1080
SH=720
ratio=SW/SH
FLOOR=SH/10
screen=pygame.display.set_mode((SW,SH))
clock=pygame.time.Clock()
fps=60
VEL=5

pygame.display.set_caption("Game")
# bg_image=pygame.image.load("Capture2.png").convert_alpha()
title=pygame.image.load("title.png").convert_alpha()
sheet1=pygame.image.load("cat6.png").convert_alpha()
sheet2=pygame.image.load("cat7.png").convert_alpha()
thumbs=pygame.image.load("thumbs.png").convert_alpha()

class Fighter():
    def __init__(self,player,x,y,data,sheet,step):
        super().__init__()
        self.size=data[0]
        self.scale=data[1]
        self.offset=data[2]
        self.player=player
        self.flip=False 
        if self.player==2:
            self.flip=True
        if self.player==3:
            self.flip=True
        self.anim_list=self.load_images(sheet,step)
        self.action=0
        self.frind=0
        self.image=self.anim_list[self.action][self.frind]
        self.uptime=pygame.time.get_ticks() 
        self.rect=pygame.Rect((x,y,80,180))
        self.grav=0
        self.running=False
        self.jump=1
        self.lclick=False
        self.rclick=False
        self.attack_type=0
        self.aing=False
        self.hp=100
        self.b=False
        self.alive=True
        self.sprites=[]
        self.animate=False
        self.hit=False
        self.action=0
        self.current_sprite=0
        self.cool=0
        self.jump2=1
        self.inp=0
        self.combo=0
        self.combo_list=[]
        self.time=0
        self.special=0
        self.file=open("combo.txt","w")
        self.bin=[0,1]
        self.inp2=[0,0,0,0,0]
    
        
    def load_images(self,sheet,step):
        anim_list=[]
        for y, anim in enumerate(step):
            temp_list=[]
            for x in range(anim):
                temp=sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                temp_list.append(pygame.transform.scale(temp,(self.size*self.scale,self.size*self.scale)))
            anim_list.append(temp_list)
        
        return anim_list
        
    def move(self,sw,sh,surface,target):
        # self.inp=random.randint(0,5)
        SPEED=10
        GRAV=1
        dx=0
        dy=0    
        self.running=False
        self.hit=False
        key=pygame.key.get_pressed() 
        mouse=pygame.mouse.get_pressed()
        if self.player==1 and self.hp>0 and self.hit==False:
            if mouse[0]==True and self.lclick==False:
                print("Lclick")
                self.lclick=True
            if mouse[2]==True and self.rclick==False:
                print("Rclick")
                self.rclick=True
            if self.aing==False:
                if key[pygame.K_a]:
                    dx=-SPEED
                    self.running=True
                if key[pygame.K_d]:
                    dx=SPEED
                    self.running=True
                if key[pygame.K_w] and (self.jump==1):
                    self.grav=-20
                    self.jump*=2
                    if key[pygame.K_d]:
                        dx=SPEED+5
                        self.running=True
            if self.aing==False:
                if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_e] ) and self.b==False:
                    self.attack(surface,target)
                    if key[pygame.K_r]:
                        self.attack_type=1
                    if key[pygame.K_t]:
                        self.attack_type=2
                        if self.jump2==1 and self.aing==True:
                            self.grav=-20
                            self.jump2=2
                    if key[pygame.K_c]:
                        self.attack_type=3
                        self.b=True
                    if key[pygame.K_e]:
                        self.attack_type=4
            if mouse[0]==False:
                self.lclick=False
            if mouse[2]==False:
                self.rclick=False
            if (key[pygame.K_r] or key[pygame.K_t]) == False:
                self.b=False       
        if self.player==2 and self.hp>0 and self.hit==False:
            if mouse[0]==True and self.lclick==False:
                print("Lclick")
                self.lclick=True
            if mouse[2]==True and self.rclick==False:
                print("Rclick")
                self.rclick=True
            if key[pygame.K_LEFT]:
                dx=-SPEED
                self.running=True
            if key[pygame.K_RIGHT]:
                dx=SPEED
                self.running=True
            if (key[pygame.K_UP] and(self.jump==1)):
                self.grav=-20
                self.jump*=2
                if key[pygame.K_RIGHT]:
                    dx=SPEED*2
                    self.running=True
            if self.aing==False:
                if (key[pygame.K_RALT] or key[pygame.K_RSHIFT]) and self.b==False:
                    self.attack(surface,target)
                    if key[pygame.K_RALT]:
                        self.attack_type=1
                    if key[pygame.K_RSHIFT]:
                        self.grav=-20
                        self.attack_type=2
                    if key[pygame.K_b]:
                        self.attack_type=3
                    self.b=True
            if mouse[0]==False:
                self.lclick=False
            if mouse[2]==False:
                self.rclick=False
            if (key[pygame.K_RALT] or key[pygame.K_RSHIFT]) == False:
                self.b=False    
        if self.player==3 and self.hp>0 and self.hit==False:
            # self.inp=random.randint(0,5)
            if self.inp==1 or self.inp2[0]==1:
                dx=-SPEED
                self.running=True
            if  self.inp==2 or self.inp2[1]==1:
                dx=SPEED
                self.running=True
            if (self.inp==3 or self.inp2[2]==1)and(self.jump==1):
                self.grav=-20
                self.jump*=2
            if self.aing==False:
                if (self.inp==4 or self.inp==5 or self.inp==6 or self.inp2[3]==1 or self.inp2[4]==1 )and self.b==False:
                    self.attack(surface,target)
                    if self.inp==4 or self.inp2[3]==1:
                        self.attack_type=1
                    if self.inp==5 or self.inp2[4]==1:
                        # self.grav-=20
                        self.attack_type=2
                    if self.inp==6:
                        self.attack_type=3
                    self.b=True
        if self.player==4 and self.hp>0 and self.hit==False:
            # self.inp=random.randint(0,5)
            if self.inp==1 or self.inp2[0]==1:
                dx=-SPEED
                self.running=True
            if  self.inp==2 or self.inp2[1]==1:
                dx=SPEED
                self.running=True
            if (self.inp==3 or self.inp2[2]==1)and(self.jump==1):
                self.grav=-20
                self.jump*=2
            if self.aing==False:
                if (self.inp==4 or self.inp==5 or self.inp==6 or self.inp2[3]==1 or self.inp2[4]==1 )and self.b==False:
                    self.attack(surface,target)
                    if self.inp==4 or self.inp2[3]==1:
                        self.attack_type=1
                    if self.inp==5 or self.inp2[4]==1:
                        # self.grav-=20
                        self.attack_type=2
                    if self.inp==6:
                        self.attack_type=3
                    self.b=True
        self.grav+=GRAV
        dy+=self.grav
        if self.rect.left+dx<0:
            dx=-self.rect.left
        if self.rect.right+dx>sw:
            dx=sw-self.rect.right
        if self.rect.bottom+dy>(sh-110):
            self.grav=0
            self.jump=1
            self.jump2=1
            dy=(sh-110)-self.rect.bottom
       
        if target.rect.centerx>self.rect.centerx:
            self.flip=False
        else:
            self.flip=True

        if self.cool>0:
            self.cool-=1
        self.rect.x+=dx
        self.rect.y+=dy
        # print(self.rect.x,self.rect.y)
        self.time+=10
        if self.time>100:
            # self.inp=random.randint(0,6)
            # self.inp=AI.ran(self.inp)
            self.inp2=AI.ran2(self.inp2)
            
            # print(self.inp2)
            self.time=0
        
    def attack(self,surface,target):
        if self.cool==0:
            self.aing=True
            atrec=pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip),self.rect.y, (2*self.rect.width),self.rect.height)
            ratrec=pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip),self.rect.centery, (2*self.rect.width),self.rect.height/2)
            if target.hp>1:
                if atrec.colliderect(target.rect) or ratrec.colliderect(target.rect):
                    if atrec.colliderect(target.rect):    
                        if self.attack_type==1:
                            target.hp-=5
                        if self.attack_type==2:
                            target.hp-=10
                            target.grav-=20
                    if ratrec.colliderect(target.rect):
                        if self.attack_type==4:
                            target.hp-=10
                    if target.combo>0:
                        target.combo_list.append(target.combo)
                    target.combo=0
                    if target.hp<=0:
                        self.alive=False
                    self.combo+=1
                    print(self.combo)
                    print(target.hp)
                    target.hit=True
                else:
                    target.hit=False
                    
            if len(self.combo_list)>0:
                print(sum(self.combo_list)/len(self.combo_list))


            pygame.draw.rect(surface,(0,0,0),atrec)
            pygame.draw.rect(surface,(0,255,0),ratrec)
    def combo(self):
        print()
    def upac(self,new):
        if new != self.action:
            self.action=new
            self.frind=0
            self.uptime=pygame.time.get_ticks()
    def draw(self,surface):
        if self.player==1:
            img=pygame.transform.flip(self.image, self.flip,False)
            # pygame.draw.rect(surface,(255,0,50),self.rect)
            surface.blit(img,(self.rect.x -(self.offset[0]*self.scale) ,self.rect.y-(self.offset[1]*self.scale)))
        if self.player==2:
            img=pygame.transform.flip(self.image, self.flip,False)
            # pygame.draw.rect(surface,(150,0,250),self.rect)
            surface.blit(img,(self.rect.x -(self.offset[0]*self.scale) ,self.rect.y-(self.offset[1]*self.scale)))
        if self.player==3:
            img=pygame.transform.flip(self.image, self.flip,False)
            # pygame.draw.rect(surface,(150,0,250),self.rect)
            surface.blit(img,(self.rect.x -(self.offset[0]*self.scale) ,self.rect.y-(self.offset[1]*self.scale)))
        if self.player==4:
            img=pygame.transform.flip(self.image, self.flip,False)
            # pygame.draw.rect(surface,(150,0,250),self.rect)
            surface.blit(img,(self.rect.x -(self.offset[0]*self.scale) ,self.rect.y-(self.offset[1]*self.scale)))
    def update(self):
        cooldown=50
        if self.hit==True:
            self.upac(10)
        if self.running ==True:
            self.upac(1)
        elif self.jump==2:
            if self.attack_type==2 and self.aing==True and self.b==False:
                self.upac(3)
            else:
                self.upac(2)
        elif self.hit==True:
            self.upac(10)
        elif self.hp<=0:
            self.upac(4)
        elif self.aing==True:
            cooldown=30
            if self.attack_type==1:
                self.upac(9)
                
                    
            elif self.attack_type==2 and self.jump!=2:
                self.upac(8)
            elif self.attack_type==4:
                cooldown=30
                self.upac(5)
            elif self.attack_type==5:
                self.upac(7)
        else:
            # cooldown=50
            self.upac(0)
        self.image=self.anim_list[self.action][self.frind]
        

        if pygame.time.get_ticks()-self.uptime>cooldown:
            self.frind+=1
            self.uptime=pygame.time.get_ticks()
            if self.frind>=len(self.anim_list[self.action]):
                if self.hp<=0:
                    self.frind=len(self.anim_list[self.action])-1
                else:
                    self.frind=0
                if self.action==8:
                    self.aing=False
                    self.cool=20
                elif self.action==9: 
                    self.aing=False
                    self.cool=5
                elif self.action==3:
                    self.aing=False
                    self.cool=20
                elif self.action==5:
                    self.aing=False
                    self.cool=20
                elif self.action==7:
                    self.aing=False
                    self.cool=20

def get_bg(name):
    image=pygame.image.load(name)
    _,_,width,height=image.get_rect()
    tiles=[]

    for i in range(SW//width+1):
        for j in range(SH//height+1):
            pos=(i*width,j*height)
            tiles.append(pos)
    return tiles,image

def draw(screen,bg,bg_img,player):
    for tile in bg:
        screen.blit(bg_img,tile)
    player.draw(screen)
    pygame.display.update()

def handler(player):
    keys=pygame.key.get_pressed() 
    player.velx=0
    if keys[pygame.K_a]:
        player.left(VEL)
    if keys[pygame.K_d]:
        player.right(VEL)

def main(screen):
    clock=pygame.time.Clock()
    bg,bg_img=get_bg("Tile_Purple.png")

    

    run=True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run=False
                break
        player.loop(fps)
        handler(player)
        draw(screen,bg,bg_img,player)
    pygame.quit()
    quit()        
                



if __name__=="__main__":
    main(screen)