import time,math,random
import pygame,sys
import pygame,sys
from pygame.locals import *
import math

pygame.init()
screenlenth=800
screen=pygame.display.set_mode((screenlenth,screenlenth))
icon=pygame.image.load('sun.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("Planetary rotation")

mercury=pygame.image.load('Mercury-PNG-Photos.png')
mercury=pygame.transform.scale(mercury,(int(50),int(50)))

sun=pygame.image.load('sun.png')
sun=pygame.transform.scale(sun,(120,120))

bg=pygame.image.load('Milky-Way-Galaxy-2560x1600.jpg')
bg=pygame.transform.scale(bg,(screenlenth,screenlenth))

x=int(screenlenth/2)
y=int(screenlenth/2)

'''
to see the full orbit set path_len in 400 at speed 1,speed is
depended on your computer,
you can control speed by using speed variable,
'''
 
r=250
dfs=100
speed=1
angc=0
angp=0
arr=[]
path_len=1200

def orbit_pos(r,a,centre):
    yp=centre[0]+(r*math.sin(math.pi*a/180))
    xp=centre[1]+(r*math.cos(math.pi*a/180))
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
                    
     
        ec=orbit_pos(dfs,angc,(x,y))
    
        mp=orbit_pos(r,angp,ec)
        
        arr.append(mp)
        if(len(arr)>=path_len):
            arr.pop(0)
        for i in range(1,len(arr)):
            pygame.draw.line(screen,(angc%255,angp%255,150),arr[i-1],arr[i],4)
        pygame.draw.aaline(screen,(255,255,255),(x,y),mp,100)
        sun_copy=pygame.transform.rotate(sun,angp*2)
        screen.blit(sun_copy,(x-int(sun_copy.get_width()/2),y-int(sun_copy.get_height()/2)))
        
        mercury_copy=pygame.transform.rotate(mercury,angp*4)
        screen.blit(mercury_copy,(mp[0]-int(mercury_copy.get_width()/2),mp[1]-int(mercury_copy.get_height()/2)))
        
        angc+=speed
        angp+=(speed*6)
        pygame.display.update()       
        
        