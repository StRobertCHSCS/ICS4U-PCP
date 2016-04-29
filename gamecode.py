"""
-------------------------------------------------------------------------------
Name:        gamecode.py
Purpose:
All the code for the game

Author:        Park.Andy

Created:        29/04/2016
------------------------------------------------------------------------------
"""

# Get necessary tools from the pygame package
import pygame

# Set up all the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Player(pygame.sprite.Sprite):
    """
    The class is the sprite that will be controlled by the player
    """
    def __init__(self, x, y):
        # Call the parent's constructor
        super(Player, self).__init__()

        # Set height, weight and colour of the sprite
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        # Make the top-left corner as the passed-in location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """
        Change the speed of the player
        :param x: int - speed for moving left and right
        :param y: int - speed for moving up and down
        :return: None
        """
        self.change_x += x
        self.change_y += y

    def update(self):
        """
        Update the position for the player
        :return: None
        """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

def main():
    """
    Main code for the game
    :return: None
    """
    # Initialize the pygame library
    pygame.init()

    # Create a 1100 x 650 screen
    screen = pygame.display.set_mode([1100, 650])

    # Set the title of the window
    pygame.display.set_caption('Demo Game')

    # Create the player object
    player = Player(50, 50)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)

    # Create the clock object to help track time
    clock = pygame.time.Clock()

    # Status for the game (uncompleted or completed)
    done = False

    # Run the game while the goal has not been met
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)

        # Update all the sprites
        all_sprites_list.update()

        # Clear screen
        screen.fill(WHITE)

        # Draw sprites
        all_sprites_list.draw(screen)

        # Flip screen
        pygame.display.flip()

        # Update the clock
        clock.tick(60)

# Run the main code
if __name__ == "__main__":
    main()

# End the program
pygame.quit()