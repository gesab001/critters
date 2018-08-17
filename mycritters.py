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
    bodyParts = [colorOfAntenna, colorOfFace, colorOfEyes, colorOfBody, colorOfLegs]
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
        antennaColor = self.colourScheme[self.bodyParts[0]]
        faceColor = self.colourScheme[self.bodyParts[1]]
        eyeColor = self.colourScheme[self.bodyParts[2]]
        bodyColor = self.colourScheme[self.bodyParts[4]]
        legColor = self.colourScheme[self.bodyParts[3]]


        while size >0:
           pygame.draw.ellipse(screen, bodyColor, [x+incrementX, y, 40, 45])
           pygame.draw.line(screen, legColor, (x+incrementX + 11, y + 50), (x+incrementX + 9, y + 30), 3)  # left leg
           pygame.draw.line(screen, legColor, (x+incrementX + 25, y + 50), (x+incrementX + 26, y + 30), 3)  # right leg
           incrementX+=25
           size-=1
        pygame.draw.ellipse(screen, faceColor, [x, y, 40, 45]) #face
        pygame.draw.ellipse(screen,eyeColor, [x+6, y+10, 10, 15])#left eye
        pygame.draw.ellipse(screen,eyeColor, [x+24, y+10, 10, 15]) #right eye
        pygame.draw.line(screen,antennaColor, (x+11, y+1), (x+9, y-10), 3) #antenna
        pygame.draw.line(screen,antennaColor, (x+25, y+1), (x+26, y-10), 3) #antenna

    def change_colour(self):
        for x in range(0,len(self.bodyParts), 1):
          if self.bodyParts[x]>len(self.bodyParts)-1:
            self.bodyParts[x] = 0
          else:
              self.bodyParts[x] = self.bodyParts[x]+1


class Butterfly():
    colourScheme = [black, white, green, red, yellow, purple, brown]
    colourOfAntenna = 0
    colourOfWing1 = 1
    colourOfWing2 = 1
    colourOfWing3 = 1
    colourOfWing4 = 1
    colourOfEyes = 2
    colourOfBody = 3
    bodyParts = [colourOfAntenna, colourOfWing1, colourOfWing2, colourOfWing3, colourOfWing4, colourOfEyes, colourOfBody]

    def __init__(self):
        x = random.randrange(50, 950)
        y = random.randrange(50, 500)
        self.xcoord = x
        self.ycoord = y

    def draw_critter(self, screen):
        x = self.xcoord
        y = self.ycoord
        colorAntenna = self.colourScheme[self.bodyParts[0]]
        colorWing1 = self.colourScheme[self.bodyParts[1]]
        colorWing2 = self.colourScheme[self.bodyParts[2]]
        colorWing3 = self.colourScheme[self.bodyParts[3]]
        colorWing4 = self.colourScheme[self.bodyParts[4]]
        colorEyes = self.colourScheme[self.bodyParts[5]]
        colorBody = self.colourScheme[self.bodyParts[6]]
        pygame.draw.ellipse(screen, colorWing1 , [x - 50, y, 70, 90]) #left wing
        pygame.draw.ellipse(screen, colorWing2, [x + 25, y, 70, 90]) #right wing
        pygame.draw.ellipse(screen, colorBody, [x, y, 40, 80]) #body
        pygame.draw.ellipse(screen, colorEyes, [x + 6, y + 10, 10, 15]) #left eye
        pygame.draw.ellipse(screen, colorEyes, [x + 24, y + 10, 10, 15]) # right eye
        pygame.draw.line(screen, colorAntenna, (x + 11, y + 1), (x + 9, y - 10), 3) #left antenna
        pygame.draw.line(screen, colorAntenna, (x + 25, y + 1), (x + 26, y - 10), 3) #right antenna

    def change_colour(self):
        for x in range(0, 7, 1):
            if self.bodyParts[x] == 6 :
                self.bodyParts[x] = 0
            else:
                self.bodyParts[x] = self.bodyParts[x] + 1
            
            