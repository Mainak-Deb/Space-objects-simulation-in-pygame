import time,math,random
import pygame,sys
import pygame,sys
from pygame.locals import *
import math

screenlenthx=1000
screenlenthy=700
screen=pygame.display.set_mode((screenlenthx,screenlenthy))
pygame.display.set_caption("Blck hole")

x=int(screenlenthx/2)
y=int(screenlenthy/2)

def hole_pos(r,ang):
    ang=ang%360
    angle=90
    
    if(270-angle<ang<angle+270):
        a=(.4*r)+(.6*r*(math.cos(math.pi*(ang-270)/180)**(3)))
        b=2*r-(1*r*(math.cos(math.pi*(ang-270)/180)**(.2)))
    else:
        a=.2*r;b=2*r
    yp=y+(a*math.sin(math.pi*ang/180))
    xp=x+(b*math.cos(math.pi*ang/180))
    return (int(xp),int(yp))

def lower_pos(r,ang):
    ang=ang%360
    yp=y+(r*math.sin(math.pi*ang/180))
    xp=x+(r*math.cos(math.pi*ang/180))
    
    return (int(xp),int(yp))


running=True

l=600
r=300
arr=[]
arr2=[]
for i in range(1200):
    arr2.append([random.randint(0,360),random.randint(100,200)])

for i in range(100):
    arr.append([random.randint(0,360),random.randint(50,55)])
        
while running:
        screen.fill((0,0,0))  

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
        for l in range(len(arr2)):
            color=(255,int(arr2[l][1]%150),0)
            if((l<len(arr))):
                if((arr[l][0]%360)>180):
                    pygame.draw.circle(screen, (252, 165, 93),hole_pos(arr[l][1],arr[l][0]),1)
                    pygame.draw.line(screen, (252, 165, 93),hole_pos(arr[l][1],arr[l][0]),hole_pos(arr[l][1],arr[l][0]-10),1)

                elif(30<(arr[l][0]%360)<160):
                    pygame.draw.circle(screen, (252, 165, 93),lower_pos(arr[l][1]*2,arr[l][0]),1)
                    pygame.draw.line(screen, (252, 165, 93),lower_pos(arr[l][1]*2,arr[l][0]),lower_pos(arr[l][1]*2,arr[l][0]-10),2)

                arr[l][0]+=4

            pygame.draw.circle(screen, color,hole_pos(arr2[l][1],arr2[l][0]),2)
            pygame.draw.line(screen, color,hole_pos(arr2[l][1],arr2[l][0]),hole_pos(arr2[l][1],arr2[l][0]-14),2)
            
            if(30<(arr2[l][0]%360)<160  and 150<arr2[l][1]<250):
              pn=lower_pos(arr2[l][1],arr2[l][0]-14)
              if(pn[1]>(y+0)):
                pygame.draw.circle(screen, color,lower_pos(arr2[l][1],arr2[l][0]),2)
                pygame.draw.line(screen, color,lower_pos(arr2[l][1],arr2[l][0]),lower_pos(arr2[l][1],arr2[l][0]-14),2)
            
                
            arr2[l][1]+=1
            arr2[l][0]+=8
            
            
            if(arr2[l][1]>300):
                arr2[l][1]=random.randint(100,200)
                    
    
        pygame.display.update()       
        
        