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
        self.fire_sound = pygame.mixer.Sound('assets/sound/fire.mp3')
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
font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 50)  
gameactive= False


#groups 
crosshairgroup = pygame.sprite.GroupSingle()
crosshairgroup.add(crosshair())


#timer used for all animatios right now placeholder 
#animationtimer = pygame.USEREVENT + 1
#pygame.time.set_timer(animationtimer,1500)    

while True:
    
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
    if gameactive=True:        
	#add the game loop here 
    pygame.mouse.set_visible(False)
    
    
    else:
        scree.fill((0,0,0))
        font1 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 72) 
        titlescreen1=font1.render('DUCK', False, (0,255,255))
        titlescreen1rect=titlescreen1.get_rect(topleft=(140, 80))
        screen.blit(titlescreen1, titlescreen1rect)
        
        font2 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 72) 
        titlescreen2=font2.render('HUNT', False, (0,255,255))
        titlescreen2rect=titlescreen2.get_rect(topleft=(200, 180))
        screen.blit(titlescreen2, titlescreen2rect)
        
        font3 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 24) 
        titlescreen3rect = pygame.Rect(220, 300, 0, 0)  # temp rect for hover check
        if titlescreen3rect.collidepoint(mouse_pos):
            titlescreen3 = font3.render('Start', False, (255,255,255))  # highlight
        else:
            titlescreen3 = font3.render('Start', False, (248, 152, 0))
        titlescreen3rect = titlescreen3.get_rect(topleft=(220,300))    
        screen.blit(titlescreen3, titlescreen3rect)
        
        font4=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 24) 
        titlescreen4rect = pygame.Rect(220, 350, 0, 0)
        if titlescreen4rect.collidepoint(mouse_pos):
            titlescreen4 = font4.render('Exit', False, (255,255,255))  
        else:
            titlescreen4 = font4.render('Exit', False, (248, 152, 0))
        titlescreen4rect = titlescreen4.get_rect(topleft=(220,350))
        screen.blit(titlescreen4, titlescreen4rect)
        
        font5=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 20)
        titlescreen5=font5.render('High Score', False, (0, 200, 0))
        titlescreen5rect=titlescreen5.get_rect(topleft=(180, 470))
        screen.blit(titlescreen5, titlescreen5rect)
        
        
        
        
        
       
        
        
        
        
    
    
    crosshairgroup.draw(screen)
    crosshairgroup.update(birdrect)
    
    
    pygame.display.update()
	clock.tick(60)    
            
            
        