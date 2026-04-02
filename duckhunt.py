#Remake of NES game Duck Hunt in pygame
import pygame
from sys import exit
from random import randint

#creating duck sprite 
class duck(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        duckdiagonalleft= pygame.image.load('assets/duck/duckdiagonalleft.png').convert_alpha()
        duckdiagonalright= pygame.image.load('assets/duck/duckdiagonalright.png').convert_alpha()
        duckleft= pygame.image.load('assets/duck/duckleft.png').convert_alpha()
        duckright= pygame.image.load('assets/duck/duckright.png').convert_alpha()
        self.index =0                                                               #controls the animation we'll need to change this depending on the speed and direction later on 
        self.fly=['duckleft','duckright','duckdiagonalleft','duckdiagonalright']    #animation list 
        self.image=sellf.fly[self.index]
        self.rect= self.image.get_rect(midbottom =(x,y))    #we'll keep it x and y until we decide how the spawn logic should work remeber to chane this