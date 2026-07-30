from pygame import * 
from pygame.locals import *
import ctypes
import random

if hasattr(ctypes,'windll'):
    ctypes.windll.user32.SetProcessDPIAware() #making window scale to 100% by default (mine is set to 125%)

init()

clock = time.Clock()

w,h = 864,936

screen = display.set_mode((w,h))
display.set_caption('Flappy Bird')

#load images
bg = image.load('assets/bg.png')
gi = image.load('assets/ground.png')
btn_img = image.load('assets/restart.png')
pause_img = transform.scale(image.load('assets/pause.png'),(30,30))
score_bg_img = transform.scale(image.load('assets/score_bg.png'),(200,200))
start_btn_img = transform.scale(image.load('assets/start.png'),(407*(4/11),150*(4/11)))
title_img = transform.scale(image.load('assets/title.png'),(141*2,37*2))


#define game variables
scroll = 0
scroll_speed = 4
start = False
game_over = False
pipe_gap = 170
pipe_frequency = 1500 # 1.5 seconds
last_pipe = time.get_ticks()
score = 0
pass_pipe = False
font_name = font.SysFont('04b_19',50)  #flappy bird font which i added to assets
pixel_font = font.SysFont('ByteBounce',50)
white = (255,255,255)
black = (0,0,0)
jump = mixer.Sound('assets/woosh.mp3')
coin = mixer.Sound('assets/score.wav')
over = mixer.Sound('assets/die.mp3')
play_sound = True
pause = False
time_at_pause = 0
time_now = 0
scores = [0]
menu = True

def reset_game():
    pipe_group.empty()
    bird.rect.x = 100
    bird.rect.y = h/2
    score = 0
    return score

def draw_text(text,font,x,y,text_col):
    img = font.render(text,True,text_col)
    text_rect = img.get_rect(center = (x,y))
    screen.blit(img,text_rect)

class Bird(sprite.Sprite):
    def __init__(self, x,y):
        sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = image.load(f'assets/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0

    def update(self):
        
        #gravity
        if start == True and not menu:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        #jump
        if game_over == False:
            if mouse.get_just_pressed()[0] or key.get_just_pressed()[K_SPACE]:
                self.vel = -10
                jump.play() 

            #handles animation
            self.counter += 1
            frame = 3
            if self.counter > frame:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            #bird rotation
            if start:
                self.image = transform.rotate(self.images[self.index], -2 * self.vel)
            if not start:
                self.image = transform.rotate(self.images[self.index], 0)
        else:
            self.image = transform.rotate(self.images[self.index], -90)

class pipe(sprite.Sprite):
    def __init__(self,x,y,pos):
        sprite.Sprite.__init__(self)
        self.image = image.load('assets/pipe.png')
        self.rect = self.image.get_rect()

        #pos 1 is from top and -1 is from bottom
        if pos == 1:
            self.image = transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y - pipe_gap/2]
        if pos == -1:
            self.rect.topleft = [x,y + pipe_gap/2]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def draw(self):
    
        #draw button
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def click(self):
        mp = mouse.get_pos()
        
        if self.rect.collidepoint(mp):
            if mouse.get_just_pressed()[0]:
                return True

bird_group = sprite.Group()
pipe_group = sprite.Group()


bird = Bird(100, int(h/2))

bird_group.add(bird)

#making the resteart btn 
btn = button(w/2 - 60,h/2 - 100,btn_img)
pause_btn = button(w - 60,30,pause_img) 
score_bg = button(w/2 - 100 , h/2 - 50, score_bg_img)
start_btn = button(w/2 - 74,h/2 - 100,start_btn_img)
title = button(w/2 - 141,200,title_img)

run = True
while run:

    clock.tick(60)

        
    #drawing process
    
    if menu:
        
        screen.fill((84, 192, 201))
        screen.blit(bg,(0,h-768))

        title.draw()

        start_btn.draw()
        if start_btn.click():

            start = False    
            menu = False  

    if not menu:

        screen.blit(bg,(0,0))

        pipe_group.draw(screen)
        bird_group.draw(screen)
        if not pause:
            bird_group.update()
            

        # print(clock.get_fps())

        screen.blit(gi, (scroll,768))  #768 is height of the bg image

            #score checker
        if len(pipe_group) > 0:   #a group is treated like a list
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    coin.play()
                    pass_pipe = False

        #collision checks
        if sprite.groupcollide(bird_group,pipe_group,False,False) or bird.rect.top < 0 or bird.rect.bottom >= 768:
            
            if not game_over:
                scores.append(score)
            
            game_over = True
            
            if play_sound:
                play_sound = False
                over.play()

        if game_over == False and start == True and not pause:        

            draw_text(str(score),font_name,int(w/2),40,white)
            pipe_group.update() #game over means pipes stop moving

            #pipe generation
            time_now = time.get_ticks()
            

            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-170,170)
                btm_pipe = pipe(w,int(h/2) - pipe_height,-1)
                top_pipe = pipe(w,int(h/2) - pipe_height,1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now
            

            #draw and scroll ground
            scroll -= scroll_speed
            if abs(scroll) > 35:
                scroll = 0

        #reset logic
        if game_over == True:
            
            btn.draw()
            score_bg.draw()
            draw_text('SCORE:',pixel_font,w/2,h/2-25,white)
            draw_text('BEST:',pixel_font,w/2,h/2+65,white)
            draw_text(str(score),font_name,w/2,h/2+20,white)
            draw_text(str(max(scores)),font_name,w/2,h/2+110,white)

            if btn.click() or key.get_just_pressed()[K_SPACE]:
                game_over = False
                start = False
                score = reset_game()
                play_sound = True

        if start == False and game_over == False:
            draw_text('press space to play',pixel_font,w/2,h/2 - 200,white)

        if pause:
            draw_text('PAUSED',pixel_font,w/2,h/2-200,white)

        pause_btn.draw()

        if key.get_just_pressed()[K_ESCAPE] or pause_btn.click() and game_over == False and start == True :
            pause = not pause
            
            time_at_pause = time.get_ticks()
            pause_dur = time_now - time_at_pause
            last_pipe -= pause_dur

    for events in event.get():
            if events.type == QUIT:
                run = False
            if events.type == MOUSEBUTTONDOWN or key.get_just_pressed()[K_SPACE] and start == False and game_over == False:
                start = True
    
    display.update()
    
quit()
