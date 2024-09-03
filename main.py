import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0
    print("Starting asteroids!")
    
    while True:
        for event in pygame.event.get(): # handle events
            if event.type == pygame.QUIT: # update game state
                return
        
        for obj in updatable:    
            obj.update(dt)
        
        screen.fill("black") # draw everything
        
        for obj in drawable:
            obj.draw(screen)
            
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()
        
        pygame.display.flip() # update display
        
        dt = clock.tick(60) / 1000 # control frame rate and get dt
    
if __name__ == "__main__":
    main()