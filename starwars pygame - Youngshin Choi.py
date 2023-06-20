import pygame
import time
i = 0
score_value = 0
stage_value = 1

start_screen = pygame.image.load("startbackground.png")
time.sleep(1.5)
#display
pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Evade the Empire!")

#covers
#cover for when the game starts
start_background = pygame.image.load("startbackground.png").convert_alpha()
s_background = start_background.get_rect(center = (400, 300))
screen.blit(start_background, s_background)
pygame.display.update()
time.sleep(1)

#cover for when the game ends
end_background = pygame.image.load("endbackground.png").convert_alpha()
e_background = end_background.get_rect(center = (400, 300))

#deathstar settings
ds_x_speed, ds_y_speed = 1, 1
deathstar_image = pygame.image.load("deathstar.png").convert_alpha()
rect = deathstar_image.get_rect(center = (200, 200))

#tiefighter settings
tie_xspeed, tie_yspeed = 2, 3
tie_2_xspeed, tie_2_yspeed = -3, -4
tie_3_xspeed, tie_3_yspeed = -2, 2
tie_image = pygame.image.load("Tiefighter.png").convert_alpha()
tie_1 = tie_image.get_rect(center = (400, 300))
tie_2 = tie_image.get_rect(center = (200, 400))
tie_3 = tie_image.get_rect(center = (600, 200))

#falcon settings
falcon_image = pygame.image.load("falcon.png").convert_alpha()
rect2 = pygame.Rect(800, 600, 50, 50)
rect2 = falcon_image.get_rect(center = (800, 600))
vel = 8

#score & stage display
font = pygame.font.Font('freesansbold.ttf', 20)
def score_display(x, y):
    global score_value
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def stage_display(x, y):
    global stage_value
    stage = font.render("Stage: " + str(stage_value), True, (255, 255, 255))
    screen.blit(stage, (x, y))

textX = 10
textY = 10
stageX = 10
stageY = 50

#stopwatch (the score increases by 1 every second)
clock = pygame.time.Clock()
milliseconds = 0

#control rectangle border
def char_border():
    global rect2, vel, screen_height, screen_width
    if rect2.x <= 0:
        rect2.x = 0
    elif rect2.x >= screen_width - 100:
        rect2.x = screen_width - 100
    if rect2.y <= 0:
        rect2.y = 0
    elif rect2.y >= screen_height - 70:
        rect2.y = screen_height - 70

#rectangle bounce
def rect_bounce():
    global ds_x_speed, ds_y_speed, tie_xspeed, tie_yspeed, tie_2_xspeed, tie_2_yspeed, tie_3_xspeed, tie_3_yspeed
    rect.x += ds_x_speed
    rect.y += ds_y_speed
    tie_1.x += tie_xspeed
    tie_1.y += tie_yspeed
    tie_2.x += tie_2_xspeed
    tie_2.y += tie_2_yspeed
    tie_3.x += tie_3_xspeed
    tie_3.y += tie_3_yspeed

    #collision with screen borders
    if rect.right >= screen_width or rect.left <= 0:
        ds_x_speed *= -1
    if rect.bottom >= screen_height or rect.top <= 0:
        ds_y_speed *= -1

    if tie_1.right >= screen_width or tie_1.left <= 0:
        tie_xspeed *= -1
    if tie_1.bottom >= screen_height or tie_1.top <= 0:
        tie_yspeed *= -1
    
    if tie_2.right >= screen_width or tie_2.left <= 0:
        tie_2_xspeed *= -1
    if tie_2.bottom >= screen_height or tie_2.top <= 0:
        tie_2_yspeed *= -1

    if tie_3.right >= screen_width or tie_3.left <= 0:
        tie_3_xspeed *= -1
    if tie_3.bottom >= screen_height or tie_3.top <= 0:
        tie_3_yspeed *= -1

    #collision with rect
    if rect.colliderect(rect2):
        screen.blit(end_background, e_background)
        pygame.display.update()
        time.sleep(1)
        pygame.quit()

    if tie_1.colliderect(rect2):
        screen.blit(end_background, e_background)
        pygame.display.update()
        time.sleep(1)
        pygame.quit()

    if tie_2.colliderect(rect2):
        screen.blit(end_background, e_background)
        pygame.display.update()
        time.sleep(1)
        pygame.quit()
    
    if tie_3.colliderect(rect2):
        screen.blit(end_background, e_background)
        pygame.display.update()
        time.sleep(1)
        pygame.quit()

running = True

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #loading background, deathstar, tie fighters
    screen.fill((30, 30, 30))
    screen.blit(deathstar_image, rect)
    screen.blit(falcon_image, rect2)
    screen.blit(tie_image, tie_1)
    screen.blit(tie_image, tie_2)
    screen.blit(tie_image, tie_3)

    keys = pygame.key.get_pressed()

    #character movement
    if keys[pygame.K_LEFT]:
        rect2.x -= vel
  
    if keys[pygame.K_RIGHT]:
        rect2.x += vel
      
    if keys[pygame.K_UP]:
        rect2.y -= vel
        
    if keys[pygame.K_DOWN]:
        rect2.y += vel

    #scoring & stages
    milliseconds += clock.tick_busy_loop(60)
    if milliseconds > 500:
        score_value += 1
        milliseconds -= 500
        screen.blit (screen, (0, 0))
        if score_value % 15 == 0:
            stage_value += 1
            ds_x_speed *= 1.5
            ds_y_speed *= 1.5
            tie_xspeed *= 1.5
            tie_yspeed *= 1.5

    #score and stage display
    score_display(textX, textY)
    stage_display(stageX, stageY)
    
    #bouncing
    rect_bounce()
    char_border()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)