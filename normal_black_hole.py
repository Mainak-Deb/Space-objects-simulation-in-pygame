import time,math,random
import pygame,sys
import pygame,sys
from pygame.locals import *
import math

screenlenthx=1000
screenlenthy=700
screen=pygame.display.set_mode((screenlenthx,screenlenthy))
pygame.display.set_caption("Line rotate")

x=int(screenlenthx/2)
y=int(screenlenthy/2)

def hole_pos(r,ang):
    a=.5*r;b=2*r;ang-=90
    yp=y+(a*math.sin(math.pi*ang/180))
    xp=x+(b*math.cos(math.pi*ang/180))
    return (int(xp),int(yp))



running=True

l=600
r=300
arr=[]
for i in range(800):
    arr.append([x,y,(random.randint(-35,35)/100),(random.randint(400,600)/100)])
arr2=[]
for i in range(800):
    arr2.append([random.randint(0,360),random.randint(50,200)])
    
while running:
        screen.fill((0,0,0))  
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
        for i in range(len(arr)):
            pygame.draw.circle(screen, (int(((arr[i][1]-y)*.5)%255),int(((arr[i][1]-y)*.65)%255),255),(int(arr[i][0]),2*y -int(arr[i][1])),2)
            l=i
            color=(255,int(arr2[l][1]%120),0)
            pygame.draw.circle(screen, color,hole_pos(arr2[l][1],arr2[l][0]),2)
            pygame.draw.line(screen, color,hole_pos(arr2[l][1],arr2[l][0]),hole_pos(arr2[l][1],arr2[l][0]-14),2)
            
            arr2[l][1]+=1
            arr2[l][0]+=4
            if(arr2[l][1]>300):
                arr2[l][0]=random.randint(0,360)
                arr2[l][1]=random.randint(50,200)
                    
            pygame.draw.circle(screen, (int(((arr[i][1]-y)*.6)%255),int(((arr[i][1]-y)*.65)%255),255),(int(arr[i][0]),int(arr[i][1])),2)
            arr[i][0]+=arr[i][2]
            arr[i][1]-=arr[i][3]
            if(arr[i][1]<0):
                arr[i]=[x,y,(random.randint(-35,35)/100),(random.randint(400,600)/100)]
                
        #pygame.draw.ellipse(screen,(255,255,255),(x-l/2,y-r/2,l,r)) 
        
        pygame.draw.circle(screen, (0,0,0), (x,y-12),50)
        pygame.draw.ellipse(screen,(0,0,0),(x-75,y-34,150,75)) 
      
        pygame.display.update()       
        
        