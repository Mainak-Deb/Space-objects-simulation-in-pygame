import time,math,random
import pygame,sys
import pygame,sys
from pygame.locals import *
import math

pygame.init()
screenlenth=850
screen=pygame.display.set_mode((screenlenth,screenlenth))
icon=pygame.image.load('sun.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("Planetary rotation")

earth=pygame.image.load('earth.png')
earth=pygame.transform.scale(earth,(80,80))

mars=pygame.image.load('mars.png')
mars=pygame.transform.scale(mars,(int(80*.53),int(80*.53)))

sun=pygame.image.load('sun.png')
sun=pygame.transform.scale(sun,(180,180))

bg=pygame.image.load('Milky-Way-Galaxy-2560x1600.jpg')
bg=pygame.transform.scale(bg,(screenlenth,screenlenth))

x=int(screenlenth/2)
y=int(screenlenth/2)
sa=0
er=250
s=0
r=300

m=2
ea=0
ma=0
speed=5
def planet_pos(r,a):
    yp=(screenlenth/2)+(r*math.sin(math.pi*a/180))
    xp=(screenlenth/2)+(r*math.cos(math.pi*a/180))
    return (int(xp),int(yp))


running=True

while running:
        screen.fill((0,0,0))  
        screen.blit(bg,(0,0))  
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                    
        for i in range(0,s,5):
            pygame.draw.line(screen,(150,150,150),planet_pos(int(er),i*2*(360/365)),planet_pos(int(er*1.52),i*2*(360/687)),1)
        
        
        sun_copy=pygame.transform.rotate(sun,sa*3)
        screen.blit(sun_copy,(x-int(sun_copy.get_width()/2),y-int(sun_copy.get_height()/2)))
        
        pygame.draw.circle(screen,(255,255,255),(x,y),int(er),2)
        pygame.draw.circle(screen,(255,255,255),(x,y),int(er*1.52),2)
        
        ep=planet_pos(int(er),ea)
        earth_copy=pygame.transform.rotate(earth,sa)
        screen.blit(earth_copy,(ep[0]-int(earth_copy.get_width()/2),ep[1]-int(earth_copy.get_height()/2)))
        
        mp=planet_pos(int(er*1.52),ma)
        mars_copy=pygame.transform.rotate(mars,sa*2)
        screen.blit(mars_copy,(mp[0]-int(mars_copy.get_width()/2),mp[1]-int(mars_copy.get_height()/2)))
        
        
        ea=ea+(speed*2*(360/365))
        ma=ma+(speed*2*(360/687))
        sa=sa+1
        s=s+speed
        pygame.display.update()       
        
        