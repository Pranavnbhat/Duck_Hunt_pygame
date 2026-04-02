#Remake of NES game Duck Hunt in pygame
import pygame
from sys import exit
from random import randint

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
        duckright2= pygame.image.load('assets/duck/duckright2.png').convert_alpha()
        duckright3= pygame.image.load('assets/duck/duckright3.png').convert_alpha()
        
        duckfall1= pygame.image.load('assets/duck/fall1.png').convert_alpha()
        duckfall2= pygame.image.load('assets/duck/fall2.png').convert_alpha()
        
        
        self.birdindex =0                                                               #controls the animation we'll need to change this depending on the speed and direction later on 
        self.fallindex =0
        
        

        
#creating the crosshair sprite 
class crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        crosshair1=pygame.image.load('assets/crosshair/crosshairs_white.png').convert_alpha()
        crosshair2=pygame.image.load('assets/crosshair/crosshairs_red.png').convert_alpha()
        self.fire_sound = pygame.mixer.Sound('assets/sounds/fire.mp3')
        self.crosshairindex=0
        self.crosshairanim=[crosshair1,crosshair2]
        self.crosshairimage=self.crosshairanim[self.crosshairindex]
    
        
    def firesound(self):
        mouseclick=pygame.mouse.get_pressed()
        if mouseclick[0]==1:
            self.fire_sound.play()
            
    def display_crosshair(self,birdrect):                                #when ever you call this function outside now remebe to call it as self.collision(birdrect)
        mousepos=pygame.mouse.get_pos()
        self.crosshairrect = self.crosshairimage.get_rect(center=mousepos)
        if self.collision(birdrect):
            self.crosshairindex=1
        else:
            self.crosshairindex=0    
        self.crosshairimage=self.crosshairanim[self.crosshairindex]
        self.crosshairrect=self.crosshairimage.get_rect(center=mousepos)
     
    def collision(self,birdrect):
        collide=self.crosshairrect.colliderect(birdrect)                #when ever you call this function outside now remebe to call it as self.collision(birdrect)
        return collide
        

            
        
    def update(self,birdrect):
        self.firesound()
        self.display_crosshair(birdrect)
        self.collision(birdrect)


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Duck Hunt')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 50)  

#groups 
crosshairgroup = pygame.sprite.GroupSingle()
crosshairgroup.add(crosshair())


#timer used for all animatios right now placeholder 
animationtimer = pygame.USEREVENT + 1
pygame.time.set_timer(animationtimer,1500)          
            
            
        