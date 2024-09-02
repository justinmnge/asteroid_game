import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get(): # handle events
            if event.type == pygame.QUIT: # update game state
                return
            
        pygame.Surface.fill(screen, (0, 0, 0)) # draw everythong
        pygame.display.flip() # update display
        dt = clock.tick(60) / 1000 # control frame rate and get dt
    
if __name__ == "__main__":
    main()