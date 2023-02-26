import pygame
import os
import AI
import numpy as np
pygame.init()
import random
class Fighter():
    def __init__(self,player,x,y,data,sheet,step):
        super().__init__()
        self.size=data[0]
        self.scale=data[1]
        self.offset=data[2]
        self.player=player #assigns player number
        self.flip=False #Decides which way the sprite faces
        if self.player==2 or self.player==3:#since these players are on the other side of the screen the flip variable is set to true
            self.flip=True
        self.anim_list=self.load_images(sheet,step)#This loads the sprite sheet alongside the Frames required for each movement
        self.action=0
        self.frind=0 #frame index ,or frind, is set to 0 initially meaning that all actions start from the beginning
        self.image=self.anim_list[self.action][self.frind] #The sprite frame that will be displayed at any given moment
        self.uptime=pygame.time.get_ticks()#
        self.rect=pygame.Rect((x,y,80,180))
        self.grav=0#Dictates the base movement both up and down
        self.running=False
        self.jump=1
        self.lclick=False
        self.rclick=False
        self.attack_type=0#Variable shows the attack being used 
        self.aing=False
        self.hp=100
        self.b=False#block variable that shows when other player/enemy can attack
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
        self.file=open("combo.txt","w")
        self.id=id
        self.bin=[0,1]
        self.inp2=[0,0,0,0,0]
    
        
    def load_images(self,sheet,step): #this function is self explanatory as it loads the images into separate lists 
        anim_list=[]
        for y, anim in enumerate(step):
            temp_list=[]
            for x in range(anim):
                temp=sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                temp_list.append(pygame.transform.scale(temp,(self.size*self.scale,self.size*self.scale)))
            anim_list.append(temp_list)
        
        return anim_list
        
    def move(self,sw,sh,surface,target):
        SPEED=10 
        GRAV=1 #How fast the sprite will fall over time
        dx=0 #direction on x axis
        dy=0 #direction on y axis   
        self.running=False
        self.hit=False
        round_over=False
        key=pygame.key.get_pressed() 
        mouse=pygame.mouse.get_pressed()
        if self.player==1 and self.hp>0 and self.hit==False:#movement variable in this case will only work if its the first player, if the player is alive and isn't being hit
            if self.aing==False: #ensures players cant move and attack at the same time
                if key[pygame.K_a]:#Move left
                    dx=-SPEED 
                    self.running=True
                if key[pygame.K_d]:#Move right      
                    dx=SPEED
                    self.running=True
                if key[pygame.K_w] and (self.jump==1):#Jump. The second part ensures the player can't continuosly press space to fly.
                    self.grav=-20
                    self.jump*=2
            if self.aing==False: #Ensures players cant use an attack before cooldown is done and so that 2 attacks can't be used at once
                if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_e] ) and self.b==False:
                    self.attack(surface,target)
                    if key[pygame.K_r]:#Attack 1
                        self.attack_type=1
                    if key[pygame.K_t]:#Attack 2
                        self.attack_type=2
                        if self.jump2==1 and self.aing==True:
                            self.grav=-20
                            self.jump2=2
                    if key[pygame.K_c]:#blocking to nullify damage done to player briefly
                        self.attack_type=3
                        self.b=True
                    if key[pygame.K_e]:
                        self.attack_type=4
            if (key[pygame.K_r] or key[pygame.K_t]) == False:
                self.b=False       
        if self.player==2 and self.hp>0  and self.hit==False: #Same as before 
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
            if (key[pygame.K_RALT] or key[pygame.K_RSHIFT]) == False:
                self.b=False    
        if self.player==3 and self.hp>0 and self.hit==False:

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
                        self.attack_type=2
                    if self.inp==6:
                        self.attack_type=3
                    self.b=True
        if self.player==4 and round_over==False and self.hit==False:
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

        self.grav+=GRAV #controls player's fall rate to make sure they're affected by gravity
        dy+=self.grav
        if self.rect.left+dx<0: #Ensures players can't run off screen
            dx=-self.rect.left
        if self.rect.right+dx>sw: #Ensures players can't run off screen
            dx=sw-self.rect.right
        if self.rect.bottom+dy>(sh-110):#Ensures players have a floor to run on
            self.grav=0
            self.jump=1
            self.jump2=1
            dy=(sh-110)-self.rect.bottom
       
        if target.rect.centerx>self.rect.centerx: #Ensures player is always facing their target
            self.flip=False
        else:
            self.flip=True

        if self.cool>0:
            self.cool-=1
        self.rect.x+=dx 
        self.rect.y+=dy
        self.time+=10
        if self.time>100:
            self.inp2=AI.ran2(self.inp2)
            self.time=0
        
    def attack(self,surface,target):
        if self.cool==0:#Ensures cooldown is done before attacks can be done
            self.aing=True
            atrec=pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip),self.rect.y, (2*self.rect.width),self.rect.height)#
            
            if target.hp>1:
                if atrec.colliderect(target.rect) :
                    if atrec.colliderect(target.rect):    
                        if self.attack_type==1:
                            target.hp-=5
                        if self.attack_type==2:
                            target.hp-=10
                            target.grav-=20
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

           
    def combo(self):
        print()
        
    def upac(self,new):
        if new != self.action:
            self.action=new
            self.frind=0
            self.uptime=pygame.time.get_ticks()

    def draw(self,surface):
        img=pygame.transform.flip(self.image, self.flip,False)
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
