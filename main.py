import pygame
from constants import *


def main():
    # Pygame Initialize
    pygame.init()

    # Set up the display screen with dimensions from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #print("Starting asteroids!")
    #print("Screen width: 1280")
    #print("Screen height: 720")

    # main game loop
    running = True
    while running:
        # handle events at the start of each loop itr
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # EXIT game when window is closed
    
        # step 2: Update the game world

        # step 3: Draw the game to screen
        screen.fill(("black")) # RGB fillscreen colour

        # refresh the screen
        pygame.display.flip()

    # clean up
    # temp comment - pygame.quit()


if __name__ == "__main__":

    main()
