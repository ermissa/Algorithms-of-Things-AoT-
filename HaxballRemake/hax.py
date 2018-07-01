import pygame
from pygame.locals import *
from sys import exit
import random
from haxball_colors import *
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Haxball!")



#Score area
score_area_height = 30
score_area_width = screen_width
score_surface  = pygame.Surface((score_area_width,score_area_height))
score_area_position= (0,0)


#game area
game_height = screen_height-score_area_height
game_width = screen_width
game_surface = pygame.Surface((game_width,game_height))
game_area_position = (0,score_area_height)

clock = pygame.time.Clock()




class Kale:
    def __init__(self,y,x=0,width=4,height=80,color=purple):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,(self.x,self.y,self.width,self.height))


class Ball:
    def __init__(self,x,y,radius=15,color=white):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)


class Player:
    def __init__(self,x,y,color,teamNumber,radius = 50):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.teamNumber = teamNumber

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)

#Kaleler
#Kale-1
kale_height = 80
#kale_x = 0
kale_y = (game_height-kale_height)/2
#kale_position = (kale_x,kale_y)

kale1 = Kale(kale_y,0)
kale2 = Kale(kale_y,screen_width-4,color=yellow)

#Ball
ball = Ball(int(game_width/2),int(game_height/2))

#Players
player1 = Player(100,int(game_height/2),blue,1)
player2 = Player(game_width-100,int(game_height/2),green,2)



#Frame
cerceve_rengi = red
kale_rengi = purple

fps = 30
while True:

    
    #Skor alanının çizimleri

    #Oyun alanının çizimleri
    pygame.draw.rect(game_surface,cerceve_rengi, (0,0,game_width,game_height) , 2 )
    player1.draw(game_surface)
    player2.draw(game_surface)
    #pygame.draw.rect(game_surface,kale_rengi,(kale_x,kale_y,4,kale_height))
    kale1.draw(game_surface)
    kale2.draw(game_surface)
    ball.draw(game_surface)
    #Screen Update
    screen.blit(game_surface,game_area_position)
    pygame.display.update()
    clock.tick(fps)