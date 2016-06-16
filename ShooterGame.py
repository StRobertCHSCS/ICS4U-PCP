"""
-------------------------------------------------------------------------------
Name:        ShooterGame.py
Purpose:
A simple, fun 2d shooter game based on python and pygame
Author:        P. Andy
Created on:        06/16/2016
------------------------------------------------------------------------------
"""

# Import necessary library
import pygame
#from pygame.locals import *

# Initialize the game
pygame.init()
width, height = 1200, 600
screen=pygame.display.set_mode((width, height))

### Load images

# The character that the player will control
player = pygame.image.load("image/man.png").convert_alpha()
player = pygame.transform.scale(player, (100, 100))

# The wooden tiles on the bakcground
background = pygame.image.load("image/background.png")
background = pygame.transform.scale(background, (100, 100))

# The girls that the player must protect
objective = pygame.image.load("image/girl.png")
objective = pygame.transform.scale(objective, (90, 90))

### Loop until game is completed
while 1:

    # Clear the screen
    screen.fill(0)

    # Draw the background and objective
    for x in range(width/background.get_width()+1):
        for y in range(height/background.get_height()+1):
            screen.blit(background,(x*100,y*100))

    # Draw the objective (girls)
    screen.blit(objective, (0,10))
    screen.blit(objective, (0,110))
    screen.blit(objective, (0,210))
    screen.blit(objective, (0,310))
    screen.blit(objective, (0,410))
    screen.blit(objective, (0,510))

    # Draw the various objects onto the screen
    screen.blit(player, (50,50))

    # Update the screen
    pygame.display.flip()

    # Main loop for the event codes
    for event in pygame.event.get():

        # Allow the player to end the game at their convenience
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)