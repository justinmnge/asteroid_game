import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    print("Starting asteroids!")
    
    while True:
        for event in pygame.event.get(): # handle events
            if event.type == pygame.QUIT: # update game state
                return
            
        screen.fill("black") # draw everything
        player.draw(screen)
        pygame.display.flip() # update display
        dt = clock.tick(60) / 1000 # control frame rate and get dt
    
if __name__ == "__main__":
    main()