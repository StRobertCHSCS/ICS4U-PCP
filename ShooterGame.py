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
from pygame.locals import *
import math

### Initialize the game

# Screen
pygame.init()
width, height = 1200, 600
screen=pygame.display.set_mode((width, height))

# Player movement
keys = [False, False, False, False]
player_position = [600,300]

# Bullet
accuracy = [0,0]
bullets = []

### Load images

# The character that the player will control
player = pygame.image.load("image/hero.png").convert_alpha()
player = pygame.transform.scale(player, (100, 100))

# The wooden tiles on the bakcground
background = pygame.image.load("image/background.png")
background = pygame.transform.scale(background, (100, 100))

# The girls that the player must protect
objective = pygame.image.load("image/girl.png")
objective = pygame.transform.scale(objective, (90, 90))

# The bullet that the character will shoot
bullet = pygame.image.load("image/bullet.png")

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

    # Complicated math formula involving trigonometry
    # For rotation of the player based on the mouse cursor
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (player_position[1] + 32), mouse_position[0] - (player_position[0] + 26))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 57.29)
    player_position2 = (player_position[0] - player_rotation.get_rect().width / 2,
                        player_position[1] - player_rotation.get_rect().height / 2)
    screen.blit(player_rotation, player_position2)

    # Code for player firing bullet
    for i in bullets:

        # Initialize and set up basic info
        index = 0
        velx = math.cos(i[0]) * 10
        vely = math.sin(i[0]) * 10
        i[1] += velx
        i[2] += vely

        # If out of boundary, delete it.
        if i[1] < -64 or i[1] > 1200 or i[2] <- 64 or i[2] > 600:
            bullets.pop(index)

        index+=1

        # Calculate bullet's rotation and draw it on the screen
        for projectile in bullets:
            bullet2 = pygame.transform.rotate(bullet, 360 - projectile[0] * 57.29)
            screen.blit(bullet2, (projectile[1], projectile[2]))

    # Update the screen
    pygame.display.flip()

    # Main loop for the event codes
    for event in pygame.event.get():

        # Allow the player to end the game at their convenience
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)

        # Change the status to true when the keys are pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True

        # Revert when the keys are lifted
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key==pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

        # Complicated math formula for bullet and its rotation
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            accuracy[1] += 1
            bullets.append([math.atan2(position[1] - (player_position2[1] + 32), position[0]
                                      - (player_position2[0] + 26)),player_position2[0] + 32, player_position2[1] + 32])

    # While status is true, move the player (direction depends on which key)
    if keys[0]:
        player_position[1] -= 5
    elif keys[2]:
        player_position[1] += 5
    elif keys[1]:
        player_position[0] -= 5
    elif keys[3]:
        player_position[0] += 5