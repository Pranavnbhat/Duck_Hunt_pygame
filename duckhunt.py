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
        
        
        self.flyright=[duckright1, duckright2, duckright3]                    #animation list 
        self.flyrightimage=self.flyright[self.birdindex]
        self.flyrightrect=self.flyrightimage.get_rect(mid bottom=(x,y))
        
        self.flyleft=[duckleft1, duckleft2, duckleft3]
        self.flyleftimage=self.flyleft[self.birdindex]
        self.flyleft=self.flyrightimage.get_rect(mid bottom=(x,y))
        
        
        #self.flyrdiagonalleft=[duckdiagonalleft1, duckdiagonalleft2, duckdiagonalleft3]
        #self.flyrdiagonalleftimage=self.flyrdiagonalleft[self.birdindex]
        #self.flyrdiagonalleft=self.flyrdiagonalleftimage.get_rect(mid bottom=(x,y))
        
        #self.flydiagonalright=[duckdiagonalright1, duckdiagonalright2, duckdiagonalright3]
        #self.flydiagonalrightimage=self.flydiagonalright[self.birdindex]
        #self.flydiagonalright=self.flydiagonalrightimage.get_rect(mid bottom=(x,y))
        
        #diagonals may not be reuired at the start this part might need a modification 
        
        
        
        self.fall=[duckfall1,duckfall2]
        self.fallimage=self.fall[fallindex]
        sefl.fallrect=self.fallimage.get_rect(midbottom =(x,y))              #x and y has to be coordinate of collision 
        
        
        
        
    def collision(self):
        collide=self.rect.colliderect(self.crosshairrect)
        return collide
        
    def fallanim(self):
        if self.collision():
            self.rect
            
        
            
        
#creating the crosshair
class crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        crosshair1=pygame.load.image('assets/crosshair/crosshairs_white.png').convert.alpha()
        crosshair2=pygame.load.image('assets/crosshair/crosshairs_red.png').convert.alpha()
        self.firesound = pygame.mixer.Sound('assets/sounds/fire.mp3')
        self.crosshairindex=0
        self.crosshairanim=[crosshair1,crosshair2]
        self.crosshairimage=self.crosshairanim[self.crosshairindex]
        
    def firesound(self):
        mouseclick=mouse.pygame.get_pressed()
        if mouseclick==[0]:
            sound.firesound.play()
            
    def display_crosshair(self):
        mousepos=pygame.mouse.get_pos()
        self.crosshairrect=self.crosshairimage,get_rect(centre=mousepos)
        
    def update(self):
        self.firesound()
        self.display_crosshair()
            


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
            
            
        