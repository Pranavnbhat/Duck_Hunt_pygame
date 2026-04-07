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
        duckright2= pygame.image.load('assets/duck/duckright2.png').convert_alpha()
        duckright3= pygame.image.load('assets/duck/duckright3.png').convert_alpha()
        
        duckfall1= pygame.image.load('assets/duck/fall1.png').convert_alpha()
        duckfall2= pygame.image.load('assets/duck/fall2.png').convert_alpha()
        duckfall3= pygame.image.load('assets/duck/fall3.png').convert_alpha()
        duckfall4= pygame.image.load('assets/duck/fall4.png').convert_alpha()
        
        
        
        duckdead= pygame.image.load('assets/duck/dead.png').convert_alpha()
        
        self.left= [duckleft1,duckleft2,duckleft3]
        self.right=[duckright1,duckright2,duckright3]
        
        self.fall=[duckfall1,duckfall2, duckfall3, duckfall4]
        
        self.move=True
        
        self.vx = choice([ -4, -3, 3, 4])
        self.vy = choice([ -4, -3, 3, 4]) 
        
        self.image = self.right[1]
        self.rect = self.image.get_rect(midbottom=(randint(100, 700), 760))
        
        
         
        
        
        
        
        self.birdindex =0                                                               
        self.fallindex =0
        self.directionindex=0
     
   
    def direction(self):
        if self.vx>0:
            self.directionindex=0                                                     #0 means its going right 
            
        else:
            self.directionindex=1                                                      #1 means its going left 
            
    def animation(self):
        if self.directionindex==0:
            self.birdindex += 0.1
            if self.birdindex> len(self.right) :
                self.birdindex =0 
            self.image=self.right[int(self.birdindex)]
        
        elif self.directionindex==1:
            self.birdindex += 0.1
            if self.birdindex> len(self.left) :
                self.birdindex =0 
            self.image=self.left[int(self.birdindex)]
            
    def duckmove(self):
        if self.move:
            if self.directionindex==0:
                self.rect.x +=self.vx 
                self.rect.y +=self.vy
                if self.rect.right >= 1024 or self.rect.left <= 0:
                    self.vx *= -1
                elif self.rect.top <= 0 or self.rect.bottom >= 765:
                    self.vy *= -1
                    
            elif self.directionindex==1:
                self.rect.x +=self.vx   
                self.rect.y +=self.vy
                if self.rect.left <=0 or self.rect.right >=1024: 
                    self.vx *= -1
                elif self.rect.top <= 0 or self.rect.bottom >= 765:
                    self.vy *= -1  
    
    def duckfall(self,shoot,crosshairindex):
        mousepos=pygame.mouse.get_pos()
        if self.move==False or (shoot==True and crosshairindex==1):    #add mousebutton down also here 
            self.move =False
            self.image=self.fall[int(self.fallindex)]
            self.fallindex +=0.1
            if self.fallindex> len(self.fall):  self.fallindex=0 
             
            
                
            if self.rect.bottom <= 760:
                self.rect.y +=7
            else:
                self.kill() 
                self.move =True
                #start dog animation timer here optionaly add dog animations here too 
            

            
            
            
    
        

    def update(self,shoot,crosshairindex):
        self.duckmove()
        self.direction()
        self.animation()
        self.duckfall(shoot,crosshairindex)
        
 
#creating the crosshair sprite 
class crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        crosshair1=pygame.image.load('assets/crosshair/crosshairs_white.png').convert_alpha()
        crosshair2=pygame.image.load('assets/crosshair/crosshairs_red.png').convert_alpha()
        crosshair1=pygame.transform.scale(crosshair1 , (25,25))
        crosshair2=pygame.transform.scale(crosshair2 , (25,25))
        
        self.fire_sound = pygame.mixer.Sound('assets/sound/fire.mp3')
        self.relaod_sound=pygame.mixer.Sound('assets/sound/reload.mp3')
        self.shoot=False # this wil be true only the frame the gun fires 
       
        self.crosshairindex=0
        self.crosshairanim=[crosshair1,crosshair2]
        self.image=self.crosshairanim[self.crosshairindex]
        self.rect = self.image.get_rect()
        
        self.reload = False
        self.reloadtime = pygame.USEREVENT + 1
        
        
    def firesound(self,event):
        if self.reload ==True :
            self.reload= False
            self.shoot=False
            self.relaod_sound.play()
            
        if event.type == pygame.MOUSEBUTTONDOWN and self.reload==False:
            self.reload=True
            self.fire_sound.play()
            self.shoot = True
               
            
            
    def display_crosshair(self,birdrect):                                #when ever you call this function outside now remebe to call it as   self.collision(duck.rect) not self.collision(duckgroup.sprite.rect) remember to use this everywhere 
        mousepos=pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=mousepos)
        if self.collision(birdrect):
            self.crosshairindex=1
        else:
            self.crosshairindex=0    
        self.image=self.crosshairanim[self.crosshairindex]
        self.rect=self.image.get_rect(center=mousepos)
     
    def collision(self,birdrect):
        collide=self.rect.colliderect(birdrect)                #when ever you call this function outside now remebe to call it as self.collision(duckgroup.sprite.rect)
        return collide                                         
        

    def update(self,birdrect):
        
        self.display_crosshair(birdrect)
        self.collision(birdrect)


pygame.init()
screen = pygame.display.set_mode((1024,960))
pygame.display.set_caption('Duck Hunt')
clock = pygame.time.Clock()
font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 50)  
gameactive= False




#font for main menu 
font1 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 72) 
font2 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 72) 
font3 = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 24) 
font4=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 24) 
font5=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 20)
font6=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 20)

#groups
duckgroup= pygame.sprite.GroupSingle()
duckgroup.add(duck())

crosshairgroup = pygame.sprite.GroupSingle()
crosshairgroup.add(crosshair())


screen.fill((66, 192, 255))
            
tree=pygame.image.load('assets/bg/tree.png')
treerect=tree.get_rect(midbottom=(121, 963))
            


grass = pygame.image.load('assets/bg/grass.png')
grassrect = grass.get_rect(bottomleft=(0, 1316))       #it's 1316 casue the image has some extra transparent parts so i had to find this manually 



cloud2 = pygame.image.load('assets/bg/cloud2.png')
cloud2rect = cloud2.get_rect(topleft=(80, 40))

cloud3 = pygame.image.load('assets/bg/cloud3.png')
cloud3rect = cloud3.get_rect(topleft=(480, 25))

cloud1 = pygame.image.load('assets/bg/cloud1.png')
cloud1rect = cloud1.get_rect(topleft=(660, 60))
            
            

#timer used for all animatios right now placeholder 
#timer = pygame.USEREVENT + 1
#pygame.time.set_timer(timer,1500) 


while True:
    screen.fill((66, 192, 255))
    screen.blit(cloud2, cloud2rect)
    screen.blit(cloud3, cloud3rect)
    screen.blit(cloud1, cloud1rect) 
    
    
    
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if gameactive:  
            crosshairgroup.sprite.firesound(event)
            
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    if gameactive==True:
        pygame.mouse.set_visible(False)
        
        if len(duckgroup)==0 : duckgroup.add(duck())            #x here will be the time dog takes to finish its animation after the duck hits the floor 
            
        duckgroup.draw(screen)
        duckgroup.update(crosshairgroup.sprite.shoot, crosshairgroup.sprite.crosshairindex)
         
            
        screen.blit(tree, treerect)
        screen.blit(grass, grassrect)
        
        crosshairgroup.draw(screen)
        if duckgroup.sprite:
            crosshairgroup.update(duckgroup.sprite.rect)  
            
    else:
        screen.fill((0,0,0))
        
        titlescreen1=font1.render('DUCK', False, (0,255,255))
        titlescreen1rect=titlescreen1.get_rect(topleft=(140, 80))
        screen.blit(titlescreen1, titlescreen1rect)
        
        
        titlescreen2=font2.render('HUNT', False, (0,255,255))
        titlescreen2rect=titlescreen2.get_rect(topleft=(200, 180))
        screen.blit(titlescreen2, titlescreen2rect)
        
        
        titlescreen3 = font3.render('Start', False, (248, 152, 0))
        titlescreen3rect = titlescreen3.get_rect(topleft=(220, 300))
        if titlescreen3rect.collidepoint(mousepos):
            titlescreen3 = font3.render('Start', False, (255, 255, 255))
        screen.blit(titlescreen3, titlescreen3rect)


        titlescreen4 = font4.render('Exit', False, (248, 152, 0))
        titlescreen4rect = titlescreen4.get_rect(topleft=(220, 350))
        if titlescreen4rect.collidepoint(mousepos):
            titlescreen4 = font4.render('Exit', False, (255, 255, 255))
        screen.blit(titlescreen4, titlescreen4rect)
        
        
        titlescreen5=font5.render('High Score', False, (0, 200, 0))
        titlescreen5rect=titlescreen5.get_rect(topleft=(180, 470))
        screen.blit(titlescreen5, titlescreen5rect)
        
        
        if event.type == pygame.MOUSEBUTTONDOWN and titlescreen3rect.collidepoint(mousepos):
            gameactive=True
        if event.type == pygame.MOUSEBUTTONDOWN and titlescreen4rect.collidepoint(mousepos):
            pygame.quit()
            exit()
          
 
    fps_text = font6.render(f"FPS: {int(clock.get_fps())}", False, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    pygame.display.update()
    clock.tick(60)    
 

       