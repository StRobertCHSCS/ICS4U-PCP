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

# nitialize the game
pygame.init()
width, height = 1200, 800
screen=pygame.display.set_mode((width, height))

# Load images
player = pygame.image.load("image/commando.png").convert_alpha()
player = pygame.transform.scale(player, (100, 100))

# Loop until game is completed
while 1:

    # Clear the screen
    screen.fill(0)

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