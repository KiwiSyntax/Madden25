# importing libraries
import pygame
import time
import random

# bg = pygame.image.load("bg.png")


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



# setting default playero direction
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

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
    
    time.sleep(2)
    
    pygame.quit()
    
    quit()



if compx_direction == 'RIGHT':
    impx = pygame.image.load("playerx_rams.png").convert()
elif compx_direction == 'LEFT':
    impx = pygame.image.load("playerx_rams_flip.png").convert()

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
        game_over()

    if playero_position[0] == (compx_position[0] - 5) and playero_position[1] == (compx_position[1] - 5):
        game_over()

    if playero_position[0] == (compx_position[0] + 5) and playero_position[1] == (compx_position[1] + 5):
        game_over()

   
    playero_body.insert(0, list(playero_position))
    playero_body.pop()
        
        
    game_window.fill(black)
    # game_window.blit(bg, (0, 0))

    
    
    for pos in playero_body:
        if direction == 'RIGHT':
            imp = pygame.image.load("player0_raider.png").convert()
        elif direction == 'LEFT':
            imp = pygame.image.load("player0_raider_flip.png").convert()
        game_window.blit(imp, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.display.flip()

    # pygame.draw.rect(game_window, white, pygame.Rect(
    #     compx_position[0], compx_position[1], 10, 10))
    
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
        game_window.blit(impx, pygame.Rect(compx_position[0], compx_position[1], 10, 10))
        pygame.display.flip()

    # Game Over conditions
    if playero_position[0] < 0 or playero_position[0] > window_x-10:
        game_over()
    if playero_position[1] < 0 or playero_position[1] > window_y-10:
        game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(playero_speed)
