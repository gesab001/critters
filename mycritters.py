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

    colourScheme = [black, white, red, yellow, purple, brown]
    colorOfBody = 1
    colorOfFace = 2
    colorOfAntenna = 3
    colorOfEyes = 4
    colorOfLegs = 5
    def __init__(self):

        bugSize = random.randrange(3,7)
        x = random.randrange(50,950)
        y = random.randrange(600,700)
        self.xcoord = x
        self.ycoord = y
        self.size = bugSize
        #self.colors = colourScheme
        #self.colorIndex = colorIndex
        #self.colorBody = self.colorOfBody
        #if self.colorIndex > 6:
        #    self.colorIndex=-1
        #self.colorFace = colourScheme[self.colorIndex+1]

    def draw_critter(self, screen):
        x = self.xcoord 
        y = self.ycoord
        size = self.size
        incrementX = 25
        bodyColor = self.colourScheme[self.colorOfBody]
        faceColor = self.colourScheme[self.colorOfFace]
        while size >0:
           pygame.draw.ellipse(screen, bodyColor, [x+incrementX, y, 40, 45])
           pygame.draw.line(screen, black, (x+incrementX + 11, y + 50), (x+incrementX + 9, y + 30), 3)  # left leg
           pygame.draw.line(screen, black, (x+incrementX + 25, y + 50), (x+incrementX + 26, y + 30), 3)  # right leg
           incrementX+=25
           size-=1
        pygame.draw.ellipse(screen, faceColor, [x, y, 40, 45]) #face
        pygame.draw.ellipse(screen,black, [x+6, y+10, 10, 15])#left eye
        pygame.draw.ellipse(screen,black, [x+24, y+10, 10, 15]) #right eye
        pygame.draw.line(screen,black, (x+11, y+1), (x+9, y-10), 3) #left leg
        pygame.draw.line(screen,black, (x+25, y+1), (x+26, y-10), 3) #right leg

    def change_colour(self):
        self.colorOfBody = self.colorOfBody+1
        if self.colorOfBody>len(self.colourScheme)-1:
            self.colorOfBody = 0


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
            
            
            