# importing libraries
import pygame
import time
import random

playero_speed = 15

# Window size
window_x = 1368
window_y = 712

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('MADDEN 2K25')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

playero_position = [0, 250]

playero_body = [[0, 250]]

compx_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

compx_body = [[0, 250]]

field_lines_body = [[120, 60],
               [120, 70],
               [120, 80],
               [120, 90],
               [120, 100],
               [240, 60],
               [240, 70],
               [240, 80],
               [240, 90],
               [240, 100],
               [360, 60],
               [360, 70],
               [360, 80],
               [360, 90],
               [360, 100],
               [480, 60],
               [480, 70],
               [480, 80],
               [480, 90],
               [480, 100],
               [600, 60],
               [600, 70],
               [600, 80],
               [600, 90],
               [600, 100],
               [720, 60],
               [720, 70],
               [720, 80],
               [720, 90],
               [720, 100],
               [840, 60],
               [840, 70],
               [840, 80],
               [840, 90],
               [840, 100],
               [960, 60],
               [960, 70],
               [960, 80],
               [960, 90],
               [960, 100],
               [1080, 60],
               [1080, 70],
               [1080, 80],
               [1080, 90],
               [1080, 100],
               [1200, 60],
               [1200, 70],
               [1200, 80],
               [1200, 90],
               [1200, 100]]

# setting default playero direction
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

down = 1

yardline = 90

def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('TOUCH DOWN Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

def show_yardline(choice, color, font, size):
  
    yardline_font = pygame.font.SysFont(font, size)
    
    yardline_surface = yardline_font.render(str(yardline), True, color)
    
 
    yardline_rect = yardline_surface.get_rect()
    yardline_rect.midtop = (140, 300)

    game_window.blit(yardline_surface, yardline_rect)

def show_nextyardline(choice, color, font, size):
  
    if yardline < 90:

        nextyardline_font = pygame.font.SysFont(font, size)
        
        nextyardline_surface = nextyardline_font.render(str(yardline + 10), True, color)
        
    
        nextyardline_rect = nextyardline_surface.get_rect()
        nextyardline_rect.midtop = (1225, 300)

        game_window.blit(nextyardline_surface, nextyardline_rect)
    
    else:
        #G
        goallineg_font = pygame.font.SysFont(font, size)
        goallineg_surface =  goallineg_font.render('G', True, color)
        goallineg_rect =  goallineg_surface.get_rect()
        goallineg_rect.midtop = (1225, 160)
        game_window.blit( goallineg_surface,  goallineg_rect)
        
        #O
        goallineo_font = pygame.font.SysFont(font, size)
        goallineo_surface =  goallineo_font.render('O', True, color)
        goallineo_rect =  goallineo_surface.get_rect()
        goallineo_rect.midtop = (1225, 260)
        game_window.blit( goallineo_surface,  goallineo_rect)
        
        #A
        goallinea_font = pygame.font.SysFont(font, size)
        goallinea_surface =  goallinea_font.render('A', True, color)
        goallinea_rect =  goallinea_surface.get_rect()
        goallinea_rect.midtop = (1225, 360)
        game_window.blit( goallinea_surface,  goallinea_rect)
        
        #L
        goallinel_font = pygame.font.SysFont(font, size)
        goallinel_surface =  goallinel_font.render('L', True, color)
        goallinel_rect =  goallinel_surface.get_rect()
        goallinel_rect.midtop = (1225, 460)
        game_window.blit( goallinel_surface,  goallinel_rect)



def downs():
      
    # creating font object my_font
    my_font = pygame.font.SysFont('Arial', 70)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render('DOWN ' + str(down), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, 300)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    playero_position[0] = playero_position[0]
    playero_position[1] = 300

    time.sleep(2)

def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    playero_position[0] = playero_position[0]
    playero_position[1] = 300

    time.sleep(2)
    
    pygame.quit()
    
    quit()


while True:
    
 
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP':
        direction = 'UP'
    if change_to == 'DOWN':
        direction = 'DOWN'
    if change_to == 'LEFT':
        direction = 'LEFT'
    if change_to == 'RIGHT':
        direction = 'RIGHT'

    # Moving the playero
    if direction == 'UP':
        playero_position[1] -= 10
    if direction == 'DOWN':
        playero_position[1] += 10
    if direction == 'LEFT':
        playero_position[0] -= 10
    if direction == 'RIGHT':
        playero_position[0] += 10

    if playero_position[0] == compx_position[0] and playero_position[1] == compx_position[1]:
        if down <= 4:
            downs()
            down = down + 1
            change_to ='RIGHT'
        else:
            game_over()     

    if playero_position[0] == (compx_position[0] - 5) and playero_position[1] == (compx_position[1] - 5):
        if down <= 4:
            downs()
            down = down + 1
            change_to ='RIGHT'
        else:
            game_over()  

    if playero_position[0] == (compx_position[0] + 5) and playero_position[1] == (compx_position[1] + 5):
        if down <= 4:
            downs()
            down = down + 1
            change_to ='RIGHT'
        else:
            game_over()  

   
    playero_body.insert(0, list(playero_position))
    playero_body.pop()
        
        
    game_window.fill(black)

    for pos in field_lines_body:
        pygame.draw.rect(game_window, white,
                         pygame.Rect(pos[0] + 20, pos[1], 10, 10))
        
    for pos in field_lines_body:
        pygame.draw.rect(game_window, white,
                         pygame.Rect(pos[0] + 20, pos[1] + 550, 10, 10))
    
    
    for pos in playero_body:
        if direction == 'RIGHT':
            imp = pygame.image.load("player0_raider.png").convert()
        elif direction == 'LEFT':
            imp = pygame.image.load("player0_raider_flip.png").convert()
        game_window.blit(imp, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.display.flip()

    #making the computer follow the player by coordinants 
    if compx_position[0] > playero_position[0]:
        compx_position[0] -= 5
        compx_direction = 'LEFT'
    
    if compx_position[0] < playero_position[0]:
        compx_position[0] += 5
        compx_direction = 'RIGHT'

    if compx_position[1] > playero_position[1]:
        compx_position[1] -= 5
    
    if compx_position[1] < playero_position[1]:
        compx_position[1] += 5


    for pos in compx_body:
        if compx_direction == 'RIGHT':
            impx = pygame.image.load("playerx_rams.png").convert()
        elif compx_direction == 'LEFT':
            impx = pygame.image.load("playerx_rams_flip.png").convert()

        game_window.blit(impx, pygame.Rect(compx_position[0], compx_position[1], 10, 10))
        pygame.display.flip()

    if playero_position[0] < 0:
        playero_position[0] = 0

    if playero_position[0] > 1300:

        if yardline > 80:
            playero_position[0] = 1000
            show_score(1, red, 'Arial', 80)

        playero_position[0] = 0
        yardline = yardline + 10
        down = 1
    
    if playero_position[1] < 0:
        playero_position[1] = 0

    if playero_position[1] > 620:
        playero_position[1] = 620


    show_yardline(1, white, 'Arial', 80)
    show_nextyardline(1, white, 'Arial', 80)


    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(playero_speed)
