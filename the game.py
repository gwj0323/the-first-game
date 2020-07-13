import pygame
import sys
pygame.init()

size = width,height = 1280,720
bg = (255,153,18)
speed = [-2,1]

#screen
screen = pygame.display.set_mode(size)
#title
pygame.display.set_caption("this is a test py")
#load picture
example = pygame.image.load("1.jpg")
#get position
position = example.get_rect()

#part 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #picture move
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        speed[0] = -speed[0]
    
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    
    screen.fill(bg)
    screen.blit(example,position)
    pygame.display.flip()
    pygame.time.delay(10)
    
