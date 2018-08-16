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

class Caterpillar():
    def __init__(self):
        colourScheme = [black, white, green, red, yellow, purple, brown]
        colorChoice = 0
        bugSize = random.randrange(0,4)
        x = random.randrange(50,950)
        y = random.randrange(600,700)
        self.xcoord = x
        self.ycoord = y
        self.size = bugSize
        self.colors = colourScheme
        self.colorIndex = colorChoice
        self.colorBody = colourScheme[self.colorIndex]
        self.colorFace = colourScheme[3]

    def draw_critter(self, screen):
        x = self.xcoord 
        y = self.ycoord
        size = self.size
        incrementX = 25
        bodyColor = self.colorBody
        while size >0:
           pygame.draw.ellipse(screen, bodyColor, [x+incrementX, y, 40, 45])
           incrementX+=25
           size-=1
        pygame.draw.ellipse(screen, red, [x, y, 40, 45])
        pygame.draw.ellipse(screen,black, [x+6, y+10, 10, 15])
        pygame.draw.ellipse(screen,black, [x+24, y+10, 10, 15])
        pygame.draw.line(screen,black, (x+11, y+1), (x+9, y-10), 3)
        pygame.draw.line(screen,black, (x+25, y+1), (x+26, y-10), 3)

    def change_colour(self):
        super.colorIndex+=1
        if super.colorIndex>len(super.colors):
            super.colorIndex=0


class Butterfly():
    def __init__(self):
        colourScheme = [black, white, green, red, yellow, purple, brown]
        x = random.randrange(50, 950)
        y = random.randrange(50, 500)
        self.xcoord = x
        self.ycoord = y
        self.colorWings = colourScheme[random.randrange(0,len(colourScheme)-1)]
        self.colorBody = colourScheme[3]
    def draw_critter(self, screen):
        x = self.xcoord
        y = self.ycoord
        colorWings = self.colorWings
        colorBody = self.colorBody
        pygame.draw.ellipse(screen, colorWings , [x - 50, y, 70, 90]) #left wing
        pygame.draw.ellipse(screen, colorWings, [x + 25, y, 70, 90]) #right wing
        pygame.draw.ellipse(screen, colorBody, [x, y, 40, 80]) #body
        pygame.draw.ellipse(screen, black, [x + 6, y + 10, 10, 15])
        pygame.draw.ellipse(screen, black, [x + 24, y + 10, 10, 15])
        pygame.draw.line(screen, black, (x + 11, y + 1), (x + 9, y - 10), 3)
        pygame.draw.line(screen, black, (x + 25, y + 1), (x + 26, y - 10), 3)
            
            
            