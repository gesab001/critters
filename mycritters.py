import pygame
import random

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
yellow   = ( 255,   255, 0)
purple   = ( 255,   0, 255)
brown     = ( 125, 100, 100)

class Caterpillar:
    def __init__(self):
        bugSize = random.randrange(0,4)
        x = random.randrange(50,950)
        y = random.randrange(50, 950)
        self.xcoord = x
        self.ycoord = y
        self.size = bugSize
      
    def draw_critter(self, screen):
        x = self.xcoord 
        y = self.ycoord
        size = self.size
        incrementX = 25
        while size >0:
           pygame.draw.ellipse(screen, brown, [x+incrementX, y, 40, 45])
           incrementX+=25
           size-=1
        pygame.draw.ellipse(screen, red, [x, y, 40, 45])
        pygame.draw.ellipse(screen,black, [x+6, y+10, 10, 15])
        pygame.draw.ellipse(screen,black, [x+24, y+10, 10, 15])
        pygame.draw.line(screen,black, (x+11, y+1), (x+9, y-10), 3)
        pygame.draw.line(screen,black, (x+25, y+1), (x+26, y-10), 3)
        
            
            
            