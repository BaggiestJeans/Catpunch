import pygame
pygame.init()
pygame.joystick.init()
SH=600
SW=1000
screen=pygame.display.set_mode((SW,SH))
clock=pygame.time.Clock()
joysticks=[pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)
run=True
while run:
        clock.tick(60)
        screen.fill((100,1,0))
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        run=False                                                                                                                                                                                                                                                                   
                if event.type==pygame.JOYBUTTONDOWN:
                        print(event)
                        print(pygame.joystick.Joystick(0).get_button())
        pygame.display.update()