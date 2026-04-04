#Remake of NES game Duck Hunt in pygame
import pygame
from sys import exit
from random import randint
from random import choice 

#creating duck sprite 
class duck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        duckdiagonalleft1= pygame.image.load('assets/duck/duckdiagonalleft1.png').convert_alpha()
        duckdiagonalleft2= pygame.image.load('assets/duck/duckdiagonalleft2.png').convert_alpha()
        duckdiagonalleft3= pygame.image.load('assets/duck/duckdiagonalleft3.png').convert_alpha()
        
        duckdiagonalright1= pygame.image.load('assets/duck/duckdiagonalright1.png').convert_alpha()
        duckdiagonalright2= pygame.image.load('assets/duck/duckdiagonalright2.png').convert_alpha()
        duckdiagonalright3= pygame.image.load('assets/duck/duckdiagonalright3.png').convert_alpha()
        
        duckleft1= pygame.image.load('assets/duck/duckleft1.png').convert_alpha()
        duckleft2= pygame.image.load('assets/duck/duckleft2.png').convert_alpha()
        duckleft3= pygame.image.load('assets/duck/duckleft3.png').convert_alpha()
        
        duckright1= pygame.image.load('assets/duck/duckright1.png').convert_alpha()
        duckright1= pygame.image.load('assets/duck/duckright2.png').convert_alpha()
        duckright3= pygame.image.load('assets/duck/duckright3.png').convert_alpha()
        
        duckfall1= pygame.image.load('assets/duck/fall1.png').convert_alpha()
        duckfall2= pygame.image.load('assets/duck/fall2.png').convert_alpha()
        
        self.left= [duckleft1,duckleft2,duckleft3]
        self.right=[duckright1,duckright2,duckright3]
        
        self.rightanimation=self.right[birdindex]
        self.leftanimation=self.left[birdindex]
        
        
        self.vx = choice([-6, -5, -4, -3, 3, 4, 5, 6])
        self.vy = choice([-6, -5, -4, -3, 3, 4, 5, 6]) 
        
        
        self.birdindex =0                                                               #controls the animation we'll need to change this depending on the speed and direction later on 
        self.fallindex =0
        self.directionindex=0
     
   
    def directiionindex(self):
        if vx>0:
            self.directionindex=0                                                     #0 means its going right 
        else:
            self.directionindex=1                                                      #1 means its going left 
            
    def animation(self):
        if directiionindex==0:
            birdindex += 0.1
            if birdindex> len(self.right) :
                birdindex =0 
            self.rightanimation=self.right[int(birdindex)]
        else:
            if directiionindex==0:
            birdindex += 0.1
            if birdindex> len(self.left) :
                birdindex =0 
            self.lefttanimation=self.left[int(birdindex)]
            
                
            
        
    
        
            
        
        

        
#creating the crosshair sprite 
class crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        crosshair1=pygame.image.load('assets/crosshair/crosshairs_white.png').convert_alpha()
        crosshair2=pygame.image.load('assets/crosshair/crosshairs_red.png').convert_alpha()
        self.fire_sound = pygame.mixer.Sound('assets/sound/fire.mp3')
        self.crosshairindex=0
        self.crosshairanim=[crosshair1,crosshair2]
        self.image=self.crosshairanim[self.crosshairindex]
        self.rect = self.image.get_rect()
    
        
    def firesound(self):
        mouseclick=pygame.mouse.get_pressed()
        if mouseclick[0]==1:
            self.fire_sound.play()
            
    def display_crosshair(self,birdrect):                                #when ever you call this function outside now remebe to call it as self.collision(birdrect)
        mousepos=pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=mousepos)
        if self.collision(birdrect):
            self.crosshairindex=1
        else:
            self.crosshairindex=0    
        self.image=self.crosshairanim[self.crosshairindex]
        self.rect=self.image.get_rect(center=mousepos)
     
    def collision(self,birdrect):
        collide=self.rect.colliderect(birdrect)                #when ever you call this function outside now remebe to call it as self.collision(birdrect)
        return collide
        

            
        
    def update(self,birdrect):
        self.firesound()
        self.display_crosshair(birdrect)
        self.collision(birdrect)


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Duck Hunt')
clock = pygame.time.Clock()
font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 50)  
gameactive= False
pygame.mouse.set_visible(False)

#font for main menu 
font1 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 72) 
font2 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 72) 
font3 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 24) 
font4=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 24) 
font5=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 20)

#groups
crosshairgroup = pygame.sprite.GroupSingle()
crosshairgroup.add(crosshair(birdrect))                          


#timer used for all animatios right now placeholder 
#animationtimer = pygame.USEREVENT + 1
#pygame.time.set_timer(animationtimer,1500)    

while True:
    
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    if gameactive==True: 
        pass                           #pass is temporary for now 
    #add the game loop here 
    
    
    
    else:
        screen.fill((0,0,0))
        
        titlescreen1=font1.render('DUCK', False, (0,255,255))
        titlescreen1rect=titlescreen1.get_rect(topleft=(140, 80))
        screen.blit(titlescreen1, titlescreen1rect)
        
        
        titlescreen2=font2.render('HUNT', False, (0,255,255))
        titlescreen2rect=titlescreen2.get_rect(topleft=(200, 180))
        screen.blit(titlescreen2, titlescreen2rect)
        
        
        titlescreen3rect = pygame.Rect(220, 300, 0, 0)  # temp rect for hover check
        if titlescreen3rect.collidepoint(mousepos):
            titlescreen3 = font3.render('Start', False, (255,255,255))  # highlight
        else:
            titlescreen3 = font3.render('Start', False, (248, 152, 0))
        titlescreen3rect = titlescreen3.get_rect(topleft=(220,300))    
        screen.blit(titlescreen3, titlescreen3rect)
        
        
        titlescreen4rect = pygame.Rect(220, 350, 0, 0)
        if titlescreen4rect.collidepoint(mousepos):
            titlescreen4 = font4.render('Exit', False, (255,255,255))  
        else:
            titlescreen4 = font4.render('Exit', False, (248, 152, 0))
        titlescreen4rect = titlescreen4.get_rect(topleft=(220,350))
        screen.blit(titlescreen4, titlescreen4rect)
        
        
        titlescreen5=font5.render('High Score', False, (0, 200, 0))
        titlescreen5rect=titlescreen5.get_rect(topleft=(180, 470))
        screen.blit(titlescreen5, titlescreen5rect)
        
        
        if event.type == pygame.MOUSEBUTTONDOWN and titlescreen3rect.collidepoint(mousepos):
            gameactive=True
        if event.type == pygame.MOUSEBUTTONDOWN and titlescreen4rect.collidepoint(mousepos):
            pygame.quit()
            exit()
        
       
        
        
        
        
       
        
        
        
        
    
    
    crosshairgroup.draw(screen)
    crosshairgroup.update(birdrect)                 
    
    
    pygame.display.update()
    clock.tick(60)    
            
            
        