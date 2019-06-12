import pygame as pg
import time
import random
#import pandas as pd

pg.init()

class MyGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pg.display.set_mode((self.width,self.height))
        self.gamename= pg.display.set_caption('A Generic RPG')
        self.title_picture = pg.image.load('forest.jpg')
        self.void = pg.image.load('')
        self.clock = pg.time.Clock()
        self.event = pg.event.wait()
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = (0,200,0)
        self.light_purple = (165,167,186)
        self.dark_purple = (52,54,73)


    def draw(self,text,color,size,location):
        font = pg.font.Font(None,size)
        message = font.render(text,True,color)
        self.screen.blit(message,location)
        pg.display.flip()

    def dialogue(self,text):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        break
            pg.draw.rect(self.screen, self.dark_purple, (50, 500, 700, 200))
            self.draw(text, self.white, 13, (150, 525))
            self.draw('Press space to continue',self.white,10,(400,750))



    def run(self):
        GameExit = False
        while not GameExit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()


                else:
                    self.intro_screen()



    def intro_screen(self):
        intro = True
        while intro:
            self.screen.fill(self.white)
            self.draw('Made by Ariel',self.black,40,(400,300))
            time.sleep(2)
            intro = False
        self.title_screen()

    def title_screen(self):
        intro = True

        while intro:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                self.screen.blit(self.title_picture, (0, 0))

                pg.draw.rect(self.screen, self.light_purple, (150, 450, 100, 50))
                self.draw("Exit", self.black, 20, (200, 475))
                pg.draw.rect(self.screen, self.light_purple, (550, 450, 100, 50))
                self.draw('Start', self.black, 20, (600, 475))
                pg.display.update()
                self.clock.tick(15)
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    posx = pos[0]
                    posy = pos[1]
                    if posx >= 150 and posx <= 250 and posy <= 500 and posy >= 450:
                        pg.quit()
                        quit()
                    if posx >= 550 and posx <= 650 and posy <= 500 and posy >= 450:
                        pg.display.flip()
                        self.choose_name()

    def choose_name(self):



MyGame().run()
pg.display.quit()
pg.quit()
quit()

"""display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
light_purple = (165, 167, 186)
dark_purple = (52, 54, 73)

player_width  = 40

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A Generic RPG')
clock = pygame.time.Clock()

vulpia_a = pygame.image.load('vulpia_a.png')
vulpia_s = pygame.image.load('vulpia_s.png')
vulpia_d = pygame.image.load('vulpia_d.png')
vulpia_w = pygame.image.load('vulpia_w.png')
title = pygame.image.load('forest.jpg')



def player(x,y,stance):
    gameDisplay.blit(pygame.transform.scale(stance,(40,54)),(x,y))

def title_screen():
    screen = True
    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(white)
            message_display('Made by Lunaarii',black,50,((display_width/2),(display_height/2)))
            time.sleep(2)
            game_intro()
def text_objects(text,font,color):
    textsurf = font.render(text,True,color)
    return textsurf, textsurf.get_rect()

def message_display(text,color,size,dest):
    largetext = pygame.font.Font('freesansbold.ttf',size)
    textsurface, textrectangle = text_objects(text,largetext,color)
    textrectangle.center = (dest[0],dest[1])
    gameDisplay.blit(textsurface,textrectangle)

    pygame.display.update()

def message_display(text,color,size,location):
    sys_font = pygame.font.SysFont('None',size)
    rendered = sys_font.render(text,True,color)
    gameDisplay.blit(rendered,location)
    pygame.display.update()






def main():
    font = pygame.font.Font(None, 32)
    input_box = pygame.draw.rect(gameDisplay,light_purple,(300,300, 140,32))
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    message_display("Choose a name.", white, 20, (100, 100))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        player_name = text
                        dialogue(f"Your name is {player_name}?")



                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        gameDisplay.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(gameDisplay, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)




def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            gameDisplay.blit(title,(0,0))


            pygame.draw.rect(gameDisplay, light_purple, (150, 450, 100, 50))
            message_display("Exit",black,20,(200,475))
            pygame.draw.rect(gameDisplay, light_purple, (550, 450, 100, 50))
            message_display('Start',black,20,(600,475))
            pygame.display.update()
            clock.tick(15)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posx= pos[0]
                posy= pos[1]
                if posx >= 150 and posx<=250 and posy <= 500 and posy >= 450:
                    pygame.quit()
                    quit()
                if posx >= 550 and posx<=650 and posy <= 500 and posy >= 450:
                    main()

def dialogue(text):
    pygame.draw.rect(gameDisplay, dark_purple, (50 ,500, 700, 200))
    message_display(text,white,13,(150,525))
    pygame.display.update()
    


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
                    x_change = -3
                    stance = vulpia_a
                if event.key == pygame.K_d:
                    x_change = 3
                    stance = vulpia_d
                if event.key == pygame.K_w:
                    y_change = -3
                    stance = vulpia_w
                if event.key == pygame.K_s:
                    y_change = 3
                    stance = vulpia_s



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change=0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change=0
        x = (x+x_change)%(display_width+100)
        y += y_change
        gameDisplay.fill(white)


        if x > display_width-player_width or x < 0:
            room += 1
            gameDisplay.fill(black)

        if y > display_height-player_width or y<0+player_width :
            y -= y_change
        player(x,y,stance)
        pygame.display.update()

        clock.tick(60)

title_screen()
game_intro()
game_loop()
pygame.quit()
quit()"""
