import pygame
from pygame.locals import *
import sys
import numpy as np

pygame.init()
fps = 120
frames = pygame.time.Clock()

screen_size = (1000,500)
disp = pygame.display.set_mode(screen_size)

white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
yellow = (255, 255, 0)

main_triangle = [(400,400), (0, 400), (200, 100)]
random_posx = np.random.randint(100,300)
random_posy = np.random.randint(500 - 2 * random_posx if random_posx <= 200 else 2 * random_posx - 300, 300)

dots = [(random_posx, random_posy)]

def midpoint(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

while True:
    pygame.display.update()
    disp.fill(white)
    for i in main_triangle:
        pygame.draw.line(disp, black, i, i)
        
    for i in dots:
        pygame.draw.line(disp, black, i, i)
        
    dots.append(midpoint(dots[-1], main_triangle[np.random.randint(3)]))
    
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    frames.tick(fps)