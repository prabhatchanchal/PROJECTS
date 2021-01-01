import pygame
import sys
from pygame.locals import *
import random
import time
from tiles import *

WIDTH = 480
HEIGHT = 520
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color_list=list(pygame.colordict.THECOLORS)
# initialize pygame and create window -------------->
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atary Break Down")
myf=pygame.font.SysFont('Comic Sans MS',30)
clock = pygame.time.Clock()
#Board values ------------>
tiles=[[(0, 0), (80, 0), (160, 0), (240, 0), (320, 0), (400, 0)],\
      [(-40, 40), (40, 40), (120, 40), (200, 40), (280, 40), (360, 40), (440, 40)],\
      [(0, 80), (80, 80), (160, 80), (240, 80), (320, 80), (400, 80)],\
      [(-40, 120), (40, 120), (120, 120), (200, 120), (280, 120), (360, 120), (440, 120)],\
      [(0, 160), (80, 160), (160, 160), (240, 160), (320, 160), (400, 160)],\
      [(-40, 200), (40, 200), (120, 200), (200, 200), (280, 200), (360, 200), (440, 200)]]
rects=[]
for i in tiles:
    temp=[]
    for j in i:
        temp.append(pygame.Rect(j+(80,40)))
    rects.append(temp)
def get_collide_index(rect):
    for i in range(6):
        if i%2!=0:
            for j in range(7):
                if rect.colliderect(rects[i][j]):
                    return True,i,j
        else:
            for j in range(6):
                if rect.colliderect(rects[i][j]):
                    return True,i,j
    return False
is_active=[[True, True, True, True, True, True],\
            [True, True, True, True, True, True, True],\
            [True, True, False, True, True, True],\
            [True, True, True, True, True, True, True],\
            [True, True, True, True, True, True],\
            [True, True, True, True, True, True, True]]

slide_board=pygame.Rect(WIDTH//2-70,HEIGHT-50,140,50)
ball=pygame.Rect(WIDTH//2-25,HEIGHT-75,25,25)
hit='hello'

# Mainloop ----------------->
right_wall=pygame.Rect(480,0,60,480)
running = True
count=0
going_down,going_up,going_left,going_right=True,False,False,False
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    keys=pygame.key.get_pressed()
    if  count<42:
        for i in range(6):
            if i%2!=0:
                for j in range(7):
                    # print(rects[i][j])
                    if is_active[i][j]:
                        pygame.draw.rect(screen,RED,rects[i][j])
            else:
                for j in range(6):
                    # print(rects[i][j])
                    if is_active[i][j]:
                        pygame.draw.rect(screen,RED,rects[i][j])

        # time.sleep(0.1)
        #ball menuvers
        check=get_collide_index(ball)
        if check==False:
            pass
        else:
            val,i,j=check
            is_active[i][j]=False

        if ball.left<=25:
            going_down=True
            hit='left'
            going_up,going_left,going_right=False,False,False
        if ball.right>=505:
            going_up=True
            hit='right'
            # print("this worked")
            going_left,going_right,going_down=False,False,False
        if ball.top<=25:
            going_left=True
            hit='top'
            going_right,going_up,going_down=False,False,False
        if ball.bottom>=505:
            going_right=True
            hit='bottom'
            going_up,going_down,going_left=False,False,False


        if going_up:
            ball.centerx-=3
            ball.centery-=3
        if going_down:
            ball.centerx+=3
            ball.centery+=3
            going=None
        if going_left:
            ball.centerx-=3
            ball.centery+=3
            going=None
        if going_right:
            ball.centerx+=3
            ball.centery-=3
            going=None
        # print(ball.bottom)
        # if ball.colliderect(slide_board):
        #     if hit=='left':
        #         going_right,going_up,going_down,going_left=True,False,False,False
        #     else:
        #         going_left,going_up,going_down,going_right=True,False,False,False
        if keys[K_LEFT] and slide_board.centerx>=0:
            if ball.colliderect(slide_board):
                ball.centerx-=5
            slide_board.x-=5
        if keys[K_RIGHT] and slide_board.centerx<=480:
            if ball.colliderect(slide_board):
                ball.centerx+=5
            slide_board.x+=5
        pygame.draw.circle(screen,WHITE,ball[:2],25)
        pygame.draw.rect(screen,BLUE,slide_board)
    else:
        text=myf.render("End game",False,pygame.colordict.THECOLORS['lawngreen'])
        screen.blit(text,(HEIGHT//2,WIDTH//2))
        text=myf.render("Press p for play again",False,pygame.colordict.THECOLORS['lawngreen'])
        screen.blit(text,(HEIGHT//2,WIDTH//2+50))
        if keys[K_p]:
            play=True
            is_active=[[True, True, True, True, True, True],\
                        [True, True, True, True, True, True, True],\
                        [True, True, False, True, True, True],\
                        [True, True, True, True, True, True, True],\
                        [True, True, True, True, True, True],\
                        [True, True, True, True, True, True, True]]


    pygame.display.flip()

pygame.quit()
