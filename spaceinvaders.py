import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello World!')

font = pygame.font.SysFont('sans',50)
space = pygame.transform.scale(pygame.image.load('space.png'),(600,600))
red = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('redship.png'),(50,50)),90)
yellow = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('yellowship.png'),(50,50)),-90)
redhealth  = 10
yellowhealth = 10
border = pygame.Rect(290,0,20,600)
redbullets = []
yellowbullets = []

redrect = pygame.Rect(50,300,50,50)
yellowrect = pygame.Rect(500,300,50,50)

Redgetshit = pygame.USEREVENT
#print(Redhit)

Yellowgetshit = pygame.USEREVENT+1

def movement():
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w] and redrect.top>0:
        redrect.y = redrect.y-2
    if keypress[pygame.K_s]and redrect.bottom<600:
        redrect.y = redrect.y+2
    if keypress[pygame.K_a] and redrect.left>0:
        redrect.x = redrect.x-2
    if keypress[pygame.K_d]and redrect.right<290:
        redrect.x = redrect.x+2
        
    if keypress[pygame.K_UP]and yellowrect.top>0:
        yellowrect.y = yellowrect.y-2
    if keypress[pygame.K_DOWN]and yellowrect.bottom<600:
        yellowrect.y = yellowrect.y+2
    if keypress[pygame.K_LEFT]and yellowrect.left>310:
        yellowrect.x = yellowrect.x-2
    if keypress[pygame.K_RIGHT] and yellowrect.right<600:
        yellowrect.x = yellowrect.x+2

def loadscreen():
    screen.blit(space,(0,0))
    screen.blit(red,(redrect.x,redrect.y))
    screen.blit(yellow,(yellowrect.x,yellowrect.y))
    redhealthbar = font.render('Health = '+ str(redhealth),True,'white')
    screen.blit(redhealthbar,(0,0))
    yellowhealthbar = font.render('Health = ' +str(yellowhealth),True,'white')
    screen.blit(yellowhealthbar, (320,0))
    pygame.draw.rect(screen,'white',border)
    for i in redbullets:
        pygame.draw.rect(screen,'red',i)
    for i in yellowbullets:
            pygame.draw.rect(screen,'yellow',i)




def bulletmovement():
    for i in redbullets:
        i.x = i.x+5
        if i.x >600:
            redbullets.remove(i)
        if yellowrect.colliderect(i):
            pygame.event.post(pygame.event.Event(Yellowgetshit))#Creating event using this code, 
            #and then you make it usable
            redbullets.remove(i)
    for i in yellowbullets:
        i.x = i.x-5
        if i.x <10:
            yellowbullets.remove(i)
        if redrect.colliderect(i):
            pygame.event.post(pygame.event.Event(Redgetshit))
            yellowbullets.remove(i)
            


delay = pygame.time.Clock()



while True:
    
    delay.tick(60)
    loadscreen()
    movement()
    bulletmovement()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(redbullets) <3 and yellowhealth>0 and redhealth>0:
                 
                redbullet = pygame.Rect(redrect.right,redrect.y+20,10,10)
                redbullets.append(redbullet)
            
            if event.key == pygame.K_RSHIFT and len(yellowbullets) <3 and redhealth>0 and yellowhealth>0:
                yellowbullet = pygame.Rect(yellowrect.left,yellowrect.y+20,10,10)
                yellowbullets.append(yellowbullet)
        if event.type == Yellowgetshit:
            if yellowhealth>0:
                yellowhealth = yellowhealth-1 
            else:
                yellowhealth = 0

        if event.type == Redgetshit:
            if redhealth>0:
                redhealth = redhealth-1
            else:
                redhealth = 0
        
    if redhealth == 0 and yellowhealth>0:
        redlost = font.render('Yellow Wins',True,'Yellow')
        screen.blit(redlost,(200,300))
    if yellowhealth == 0 and  redhealth>0:
        yellowlost = font.render('Red Wins',True,'Red')
        screen.blit(yellowlost,(200,300))
    if yellowhealth == 0  and redhealth==0:
        tie = font.render('TIE',True,'Orange')
        screen.blit(tie,(200,300))
        
            

         
    pygame.display.update()