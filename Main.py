import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black=(0,0,0)
white=(255,255,255)
red = (255,0,0)

car_width = 100

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('race game')
clock = pygame.time.Clock()

carImg = pygame.image.load('simple-travel-car-top-view.png')

def things(thingx,thingy,thingw,thingh, color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def crash():
    message_display('you crashed')
    
def text_objects(text,font):
    textSurface =  font.render(text,True,black)
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    pygame.display.update()
#     time.sleep(2)
#     game_loop()
    
def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.5)
        
    x_change=0
    
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width=100
    thing_height=100
    
    gameExit = False
    
    
    
    while not gameExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            x -= 5
    
        if keys_pressed[pygame.K_RIGHT]:
            x += 5
    
        if keys_pressed[pygame.K_UP]:
            x -= 5
    
        if keys_pressed[pygame.K_DOWN]:
            x += 5    
  
        
          #  print(event)
              
        gameDisplay.fill(white)
        
#         things(thingx,thingy,thingw,thingh, color):
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty +=thing_speed
        
        car(x,y)    
        if x > display_width-car_width or x<0:
            crash()
            
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()

quit()