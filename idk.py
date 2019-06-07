import pygame
import time
import random
import pandas as pd

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

player_width  = 60

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A Generic RPG')
clock = pygame.time.Clock()

vulpia_a = pygame.image.load('vulpia_a.png')
vulpia_s = pygame.image.load('vulpia_s.png')
vulpia_d = pygame.image.load('vulpia_d.png')
vulpia_w = pygame.image.load('vulpia_w.png')




def player(x,y,stance):
    gameDisplay.blit(pygame.transform.scale(stance,(60,81)),(x,y))

def title_screen():
    screen = True
    while screen:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf', 100)
            TextSurf, TextRect = text_objects("A Generic RPG", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(15)
def text_objects(text,font):
    textsurf = font.render(text,True,black)
    return textsurf, textsurf.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf',115)
    textsurface, textrectangle = text_objects(text,largetext)
    textrectangle.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textsurface,textrectangle)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def defeated():
    message_display('Game Over')


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gameDisplay, 'button.png', (150, 450, 100, 50))
        pygame.draw.rect(gameDisplay, 'button.png', (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)

def game_loop():
    x= (display_width*0.45)
    y =(display_height*0.8)

    x_change = 0
    y_change = 0

    gameExit = False
    stance = vulpia_s
    room = 0
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -4
                    stance = vulpia_a
                if event.key == pygame.K_d:
                    x_change = 4
                    stance = vulpia_d
                if event.key == pygame.K_w:
                    y_change = -4
                    stance = vulpia_w
                if event.key == pygame.K_s:
                    y_change = 4
                    stance = vulpia_s



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change=0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change=0
        x += x_change
        y += y_change
        gameDisplay.fill(white)

        if x > display_width-player_width or x < 0:
            room += 1


        if y > display_height-player_width or y<0 :
            y -= y_change
        player(x,y,stance)
        pygame.display.update()

        clock.tick(60)
title_screen()
game_loop()
pygame.quit()
quit()

