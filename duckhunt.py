#Remake of NES game Duck Hunt in pygame
import pygame
from sys import exit
from random import randint

#creating duck sprite 
class duck(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
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
        
        duckfall1= pygame.image.load('assets/duck/fall1.png')convert_alpha()
        duckfall2= pygame.image.load('assets/duck/fall2.png')convert_alpha()
        
        
        self.index =0                                                               #controls the animation we'll need to change this depending on the speed and direction later on 
        self.flyright=['duckright1', 'duckright2', 'duckright3']                    #animation list 
        self.flyleft=['duckleft1', 'duckleft2', 'duckleft3']
        self.flyrdiagonalleft=['duckdiagonalleft1', 'duckdiagonalleft2', 'duckdiagonalleft3']
        self.flydiagonalright=['duckdiagonalright1', 'duckdiagonalright2', 'duckdiagonalright3']
        self.fall=['duckfall1','duckfall2']
        self.image=sellf.fly[self.index]
        self.rect= self.image.get_rect(midbottom =(x,y))    #we'll keep it x and y until we decide how the spawn logic should work remeber to chane this
        #create one fucntioin for left one for right one for diagonal left one for diagonl right add this later 
        