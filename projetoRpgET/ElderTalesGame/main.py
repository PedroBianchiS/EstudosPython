import pygame
import time
import random

width, height = 1000, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Elder Tales RPG')

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ == '__name__':
    main()