#Remake of NES game Duck Hunt in pygame
import pygame
from sys import exit
from random import randint
from random import choice 

#creating duck sprite 
class duck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        
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
        
        self.flap=pygame.mixer.Sound('assets/sound/flap.mp3')
        self.flapy_played=False
        
        self.flap.set_volume(0.35)
        
        self.fallsound=pygame.mixer.Sound('assets/sound/fallsound.mp3')
        
        self.fallsound_played=False
        
        
        self.thud=pygame.mixer.Sound('assets/sound/thud.mp3')
        self.thud_played=False
        
        
        
        
        duckdead= pygame.image.load('assets/duck/dead.png').convert_alpha()
        
        self.left= [duckleft1,duckleft2,duckleft3]
        self.right=[duckright1,duckright2,duckright3]
        
        
        
        self.fall=[duckfall1,duckfall2, duckfall3, duckfall4]
        
        self.move=True
        
        global gameround
        
        if 0<=gameround<=19:
            speed=4
        elif 20<=gameround<=49:
            speed=6
        elif 50<=gameround<=79:
            speed=8
        else:
            speed=10
            
        self.vx = choice([ (-1*speed)-1, -1*speed, speed, speed+1])
        self.vy = choice([(-1*speed)-1, -1*speed, speed, speed+1])
        
        self.image = self.right[1]
        self.rect = self.image.get_rect(midbottom=(randint(100, 700), 770))
        
   
        self.birdindex =0                                                               
        self.fallindex =0
        self.directionindex=0
    


        self.font7=pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 20)
        self.score_text = self.font7.render('500', False, (255, 255, 255))   

        self.score_x = -100
        self.score_y = -100
        self.score_captured = False
        
   
    def direction(self):
        if self.vx>0:
            self.directionindex=0                                                     #0 means its going right 
            
        else:
            self.directionindex=1                                                      #1 means its going left 
            
    def animation(self):
        if self.directionindex==0:
            self.birdindex += 0.3
            if self.birdindex> len(self.right) :
                self.birdindex =0 
            self.image=self.right[int(self.birdindex)]
        
        elif self.directionindex==1:
            self.birdindex += 0.3
            if self.birdindex> len(self.left) :
                self.birdindex =0 
            self.image=self.left[int(self.birdindex)]
            
    def duckmove(self):
        global duck_missed
        if self.move and not game_over_screen:
            if not self.flapy_played and not round_intro:
                self.flap.play(-1)       
                self.flapy_played=True
                
                
            if self.directionindex==0:
                self.rect.x +=self.vx 
                self.rect.y +=self.vy
                if self.rect.right >= 1024 or self.rect.left <= 0:
                    self.vx *= -1
                elif self.rect.top <= 0 or self.rect.bottom >= 775:
                    if not duck_missed: self.vy *= -1
                    
            elif self.directionindex==1:
                self.rect.x +=self.vx   
                self.rect.y +=self.vy
                if self.rect.left <=0 or self.rect.right >=1024: 
                    self.vx *= -1
                elif self.rect.top <= 0 or self.rect.bottom >= 775:
                    if not duck_missed: self.vy *= -1  
                    
            if duck_missed==True :
                self.vy=0
                self.rect.y -=8
                
                
    
    def duckfall(self,shoot,crosshairindex):
        global score
        mousepos=pygame.mouse.get_pos()
        if self.move==False or (shoot==True and crosshairindex==1):    #add mousebutton down also here 
            self.move =False
            self.flap.stop()
            pygame.time.set_timer(roundtime, 0)
            
        
            if not self.score_captured:
                self.score_x = self.rect.centerx
                self.score_y = self.rect.centery
                self.score_captured = True
                score+=500
                  
        
            if not self.fallsound_played:
                self.fallsound.play()
                self.fallsound_played=True
                
                
            self.image=self.fall[int(self.fallindex)]
            self.fallindex +=0.1
            if self.fallindex> len(self.fall):  self.fallindex=0 
            duck_x = self.rect.centerx
            
            
             
            
            if 0<duck_x<200:  duck_x=325
            elif 750<duck_x<910:  duck_x=660
            
                
            if self.rect.bottom <= 760:
                self.rect.y +=7
                             #this is for the dog 
                
            else:
                self.fallsound.stop() 
                if self.thud_played==False:
                    self.thud.play()
                    self.thud_played=True
                self.kill()
                doggroup.add(dog(duck_x))
                
                self.move =True
                #start dog animation timer here optionaly add dog animations here too 
            


    def update(self,shoot,crosshairindex):
        self.duckmove()
        self.direction()
        self.animation()
        self.duckfall(shoot,crosshairindex,)
        




#creating the dog sprite 
class dog(pygame.sprite.Sprite):
    def __init__(self,x):
        super().__init__()
        dogwin=pygame.image.load('assets/dog/dogwin.png')
        dogwin=pygame.transform.scale(dogwin, (150,150))
        self.down=False
        
        global gameactive
        global round_intro
        
        dog1 = pygame.image.load('assets/dog/dog1.png').convert_alpha()
        dog2 = pygame.image.load('assets/dog/dog2.png').convert_alpha()
        dog3 = pygame.image.load('assets/dog/dog3.png').convert_alpha()
        dog4 = pygame.image.load('assets/dog/dog4.png').convert_alpha()
        dog5 = pygame.image.load('assets/dog/dog5.png').convert_alpha()
        dog6 = pygame.image.load('assets/dog/dog6.png').convert_alpha()
        dog7 = pygame.image.load('assets/dog/dog7.png').convert_alpha()
        dog8 = pygame.image.load('assets/dog/dog8.png').convert_alpha()
        
        dog1 = pygame.transform.scale(dog1, (150, 150))
        dog2 = pygame.transform.scale(dog2, (150, 150))
        dog3 = pygame.transform.scale(dog3, (150, 150))
        dog4 = pygame.transform.scale(dog4, (150, 150))
        dog5 = pygame.transform.scale(dog5, (150, 150))
        dog6 = pygame.transform.scale(dog6, (150, 150))
        dog7 = pygame.transform.scale(dog7, (150, 150))
        dog8 = pygame.transform.scale(dog8, (150, 150))
        
        
        doglaugh1=pygame.image.load('assets/dog/doglaugh1.png').convert_alpha()
        doglaugh2=pygame.image.load('assets/dog/doglaugh2.png').convert_alpha()
        
        doglaugh1 = pygame.transform.scale(doglaugh1, (100, 150))
        doglaugh2 = pygame.transform.scale(doglaugh2, (100, 150))
        
        self.dog_laugh_list=[doglaugh1,doglaugh2]
        self.dog_laugh_index=0
        
        
        
        
        self.doglist=[dog1, dog2, dog3, dog4, dog5, dog6, dog7, dog8]
        self.dogindex=0
        
        self.dog_laugh_sound=pygame.mixer.Sound('assets/sound/laugh_sound.mp3')
        self.laugh_played=False
        
        self.game_over_sound=pygame.mixer.Sound('assets/sound/gameover.mp3')
        
        
        self.win_sound=pygame.mixer.Sound('assets/sound/win_sound.mp3')
        self.win_sound_played=False
        
        
        
        
        #x=0
        self.image=dogwin
        self.rect=self.image.get_rect(midtop =(x,760))     #x here is the position of duck dying 
        
        
        if round_intro==True and gameactive==True:
            self.image=self.doglist[int(self.dogindex)]
            self.rect = self.image.get_rect(bottomleft=(0,770))
            
    
    def dog_win_animation(self):
        global gameround
        global ammo
        if len(duckgroup)==0:
            
            if self.rect.top <= 760 and self.down==False:
                self.rect.y-=5
                if self.rect.top==550:
                    self.down=True
            elif self.down==True:
                self.rect.y +=5 
                if self.rect.top >= 790:
                    self.kill()
                    gameround+=1
                    ammo =3
            if not self.win_sound_played:
                self.win_sound_played=True
                self.win_sound.play()
            pygame.time.set_timer(roundtime, 0)  
            
    def dog_laugh_animation(self):
        global duck_missed
        global ammo
        global gameround
        global gameactive
        
        if duck_missed and  duckgroup.sprite.move:
            
            
            self.dog_laugh_index+=0.2
            if self.dog_laugh_index >= len(self.dog_laugh_list):    self.dog_laugh_index = 0
            self.image=self.dog_laugh_list[int(self.dog_laugh_index)]
            
            if self.rect.top <= 780 and self.down==False:
                if not game_over_screen:    self.rect.y-=3
                elif game_over_screen:  self.rect.y-=2
                if self.rect.top==550:
                    self.down=True
            elif self.down==True:
                if not game_over_screen:    self.rect.y +=3
                elif game_over_screen:  self.rect.y+=2
                if self.rect.top >= 790:
                    duck_missed=False
                    self.kill()
                    gameround+=1
                    ammo =3
                    duckgroup.sprite.flap.stop()
                    duckgroup.sprite.kill()
                    if game_over_screen:    gameactive=False
            
            if self.laugh_played==False:
                self.laugh_played=True
                self.dog_laugh_sound.play()
                if game_over_screen:    self.game_over_sound.play()
            
            pygame.time.set_timer(roundtime, 0)
        
  

    def dog_intro(self):
        global ammo
        global round_intro
        global round_intro_sound_played
        if round_intro==True:
            if self.rect.x< 500 :
                self.dogindex+=0.1
                if self.dogindex>4: self.dogindex=0
                self.image=self.doglist[int(self.dogindex)]
                
                self.rect.x+=2
            
            elif self.rect.centerx>=500:
                
                
                if self.dogindex<5:  self.dogindex=5
                self.dogindex+=0.05
                self.image=self.doglist[int(self.dogindex)]
                
                if self.dogindex>=6:
                    
                    if self.dogindex>7 :  self.dogindex=7
                    self.dogindex+=0.04
                    self.image=self.doglist[int(self.dogindex)]
                    self.rect.x+=3
                    
                
                    
                
                
                
                
                if self.rect.centery>=560 and self.down==False and self.dogindex>5.8:
                    self.rect.y-=3
                    if self.rect.centery<560:
                        self.down=True
                elif self.down==True:
                    self.rect.y +=3.5
                    if self.rect.top >= 790:
                        self.kill()
                        ammo=3
                        round_intro_sound_played = False
                        round_intro=False
                        
                
        


    def update(self):
        if duck_missed:
            self.dog_laugh_animation()
        elif round_intro:
            self.dog_intro()
        else:
            self.dog_win_animation()
        
        

#creating the crosshair sprite 
class crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        crosshair1=pygame.image.load('assets/crosshair/crosshairs_white.png').convert_alpha()
        crosshair2=pygame.image.load('assets/crosshair/crosshairs_red.png').convert_alpha()
        crosshair3=pygame.image.load('assets/crosshair/invis.png').convert_alpha()
        
        crosshair1=pygame.transform.scale(crosshair1 , (25,25))
        crosshair2=pygame.transform.scale(crosshair2 , (25,25))
        
        self.fire_sound = pygame.mixer.Sound('assets/sound/fire.mp3')
        self.relaod_sound=pygame.mixer.Sound('assets/sound/reload.mp3')
        self.shoot=False # this wil be true only the frame the gun fires 
       
        self.crosshairindex=0
        self.crosshairanim=[crosshair1,crosshair2,crosshair3]
        self.image=self.crosshairanim[self.crosshairindex]
        self.rect = self.image.get_rect()
        
        
        
        self.reload = False
        self.reloadtime = pygame.USEREVENT + 1
        
        
    def firesound(self,event):
        global ammo 
        if self.reload ==True :
            self.reload= False
            self.shoot=False
            if not round_intro: self.relaod_sound.play()
            
        if event.type == pygame.MOUSEBUTTONDOWN and self.reload==False and len(duckgroup)!=0:
            self.reload=True
            if not self.crosshairindex==2 and not round_intro:  self.fire_sound.play()
            ammo -=1
            self.shoot = True
               
            
            
    def display_crosshair(self,birdrect):                                #when ever you call this function outside now remebe to call it as   self.collision(duck.rect) not self.collision(duckgroup.sprite.rect) remember to use this everywhere 
        mousepos=pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=mousepos)
        if len(doggroup)!=0:
            self.crosshairindex=2
          
        elif self.collision(birdrect):
            self.crosshairindex=1
        else:
            self.crosshairindex=0    
        self.image=self.crosshairanim[self.crosshairindex]
        self.rect=self.image.get_rect(center=mousepos)
     
    def collision(self,birdrect):
        if not duck_missed:
        
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
gameround=0
round_intro=False
duck_missed=False
duck_missed_counter=0
game_over_screen=False
ammo =3 
duckcount=0





menu_theme=pygame.mixer.Sound('assets/sound/menu_theme.mp3')
round_intro_theme=pygame.mixer.Sound('assets/sound/round_intro_theme.mp3')
menu_sound_played = False
round_intro_sound_played = False



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



doggroup=pygame.sprite.GroupSingle()




screen.fill((66, 192, 255))            
tree=pygame.image.load('assets/bg/tree.png').convert_alpha()
treerect=tree.get_rect(midbottom=(121, 963))
            


grass = pygame.image.load('assets/bg/grass.png').convert_alpha()
grassrect = grass.get_rect(bottomleft=(0, 1316))       #it's 1316 casue the image has some extra transparent parts so i had to find this manually 



cloud2 = pygame.image.load('assets/bg/cloud2.png').convert_alpha()
cloud2rect = cloud2.get_rect(topleft=(80, 40))

cloud3 = pygame.image.load('assets/bg/cloud3.png').convert_alpha()
cloud3rect = cloud3.get_rect(topleft=(480, 25))

cloud1 = pygame.image.load('assets/bg/cloud1.png').convert_alpha()
cloud1rect = cloud1.get_rect(topleft=(660, 60))

bullet=pygame.image.load('assets/bg/bullet.png').convert_alpha()

round_intro_counter=pygame.image.load('assets/bg/round_intro_counter.png').convert_alpha()
round_intro_counter_rect=round_intro_counter.get_rect(center=(512,180))


fly_away_card=pygame.image.load('assets/bg/fly_away_screen.png').convert_alpha()
fly_away_card_rect=fly_away_card.get_rect(center=(512,180))

game_over_card = pygame.image.load('assets/bg/game_over_card.png').convert_alpha()
game_over_card_rect = game_over_card.get_rect(center=(512, 180))




  

#timer 
roundtime = pygame.USEREVENT + 2
timer_started=False




#score and highscore text file creation 
score=0
with open('highscore.txt' ,'r') as f:
    highscore=int(f.read())
    


while True:
    screen.fill((66, 192, 255))
    screen.blit(cloud2, cloud2rect)
    screen.blit(cloud3, cloud3rect)
    screen.blit(cloud1, cloud1rect) 
    

    mousepos = pygame.mouse.get_pos()
    #print(mousepos)
    for event in pygame.event.get():
        if gameactive:  
            crosshairgroup.sprite.firesound(event)
            
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==roundtime:
            if duckgroup.sprite and duckgroup.sprite.move and len(doggroup)==0:
                duck_missed = True
                duck_missed_counter+=1
                doggroup.add(dog(512))
                timer_started=False
                
     

    if round_intro==True and gameactive==True:
        pygame.mouse.set_visible(False)
        if duck_missed_counter>=3 and 0<=gameround<=19:
            duck_missed=True
            round_intro=False
            doggroup.add(dog(512))
            game_over_screen=True
            
            
            
        elif duck_missed_counter>=2 and 20<=gameround<=49:
            duck_missed=True
            round_intro=False
            doggroup.add(dog(512))
            game_over_screen=True
            
        elif duck_missed_counter>=3 and 50<=gameround:
            duck_missed=True
            round_intro=False
            doggroup.add(dog(512))
            game_over_screen=True
            
        else:
            duck_missed_counter=0
            if not round_intro_sound_played:
                round_intro_theme.play()
                round_intro_sound_played=True
            
            screen.blit(round_intro_counter, round_intro_counter_rect)
            round_text=font6.render(f" {(gameround//10)+1}", False, (255, 255, 255))
            
            screen.blit(round_text, (480,190))
            
            if doggroup.sprite.dogindex>=7:
                doggroup.update()
                doggroup.draw(screen)    
                screen.blit(tree, treerect)
                screen.blit(grass, grassrect)
            else:
                screen.blit(tree, treerect)
                screen.blit(grass, grassrect)
                doggroup.update()
                doggroup.draw(screen)
            
                

        
    elif gameactive==True:
        if not timer_started:
            pygame.time.set_timer(roundtime, 5000, 1)
            timer_started=True
        pygame.mouse.set_visible(False)
        
        if len(duckgroup)==0 and len(doggroup)==0: 
            duckgroup.add(duck())   
            timer_started=False
            duckcount+=1
            if duckcount%10 ==0 and duckcount!=0:
                round_intro=True
                
                
                doggroup.add(dog(0))
            
        if ammo<=0 and duckgroup.sprite and duckgroup.sprite.move and len(doggroup)==0 and not crosshairgroup.sprite.shoot: 
            duck_missed=True
            duck_missed_counter+=1
            doggroup.add(dog(512))
        if duck_missed==True: 
            if not game_over_screen:    screen.fill((227,163,150))
            
            if duckgroup:   duckgroup.sprite.flap.stop()
        
            
        
            
        duckgroup.draw(screen)
        duckgroup.update(crosshairgroup.sprite.shoot, crosshairgroup.sprite.crosshairindex)
        
        doggroup.update()
        doggroup.draw(screen)        
            
        screen.blit(tree, treerect)
        screen.blit(grass, grassrect)
        
        if duckgroup.sprite:   screen.blit(duckgroup.sprite.score_text, (duckgroup.sprite.score_x,duckgroup.sprite.score_y)) 
        if duck_missed and not game_over_screen: screen.blit(fly_away_card, fly_away_card_rect)  
        elif duck_missed and game_over_screen:  screen.blit(game_over_card, game_over_card_rect)

        
        crosshairgroup.draw(screen)
        if duckgroup.sprite :
            crosshairgroup.update(duckgroup.sprite.rect)
        else:
            crosshairgroup.update(pygame.Rect(-100, -100, 0, 0))
            
        round_text=font6.render(f" {(gameround//10)+1}", False, (255, 255, 255))
        screen.blit(round_text, (130,807))    
        
        score_display=font3.render(f" {(score)}", False, (255,255,255))
        screen.blit(score_display, (800,870))


        if ammo==1:
            bulletrect=bullet.get_rect(center=(110,880))
            screen.blit(bullet, bulletrect)
        if ammo==2: 
            bulletrect1 = bullet.get_rect(center=(110, 880))
            screen.blit(bullet, bulletrect1) 
            bulletrect2 = bullet.get_rect(center=(140, 880))
            screen.blit(bullet, bulletrect2)    
        if ammo==3: 
            bulletrect1 = bullet.get_rect(center=(110, 880))
            screen.blit(bullet, bulletrect1) 
            bulletrect2 = bullet.get_rect(center=(140, 880))
            screen.blit(bullet, bulletrect2)
            bulletrect3 = bullet.get_rect(center=(170, 880))
            screen.blit(bullet, bulletrect3)
        
        
        if score>highscore:
            with open('highscore.txt','w') as f:
                f.write(str(score))
        else:
            with open('highscore.txt','r') as f:
                highscore=int(f.read())    
            
            
    else:
        screen.fill((0,0,0))
        pygame.mouse.set_visible(True)
        
        if not menu_sound_played:
            menu_theme.play()
            menu_sound_played=True
        
        if score>highscore:
            with open('highscore.txt','w') as f:
                f.write(str(score))
        else:
            with open('highscore.txt','r') as f:
                highscore=int(f.read())
        
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
        
        
        titlescreen5 = font5.render(f'High Score:{highscore}', False, (0, 200, 0))
        titlescreen5rect=titlescreen5.get_rect(topleft=(180, 470))
        screen.blit(titlescreen5, titlescreen5rect)
        
        
        if event.type == pygame.MOUSEBUTTONDOWN and titlescreen3rect.collidepoint(mousepos):
            gameactive=True
            duckgroup.add(duck())
            
            menu_theme.stop()
            menu_sound_played=False
            
            round_intro=True
            
            doggroup.add(dog(0))
            
            game_over_screen=False
            duck_missed=False
            duck_missed_counter=0
            gameround=0
            score=0
            
        if event.type == pygame.MOUSEBUTTONDOWN and titlescreen4rect.collidepoint(mousepos):
            pygame.quit()
            exit()
          
 
    fps_text = font6.render(f"FPS: {int(clock.get_fps())}", False, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    #print(ammo)
    #print(duck_missed_counter)
    
    pygame.display.update()
    clock.tick(60)    
 

       