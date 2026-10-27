from logger import log_state
from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from logger import log_event
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    wahr = True
    Clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    a1 = AsteroidField()
    p1 = Player(x, y)
    while wahr == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black") 
        dt = Clock.tick(60) / 1000
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        updatable.update(dt)
        for object in asteroids:
            if p1.collides_with(object) == True:
                log_event("player_hit")
                print(f" Game over!")
                sys.exit()
        for x in shots:
            for y in asteroids:
                if x.collides_with(y):
                    log_event("asteroid_shot")
                    y.split()
                    x.kill()

        print(f" Dt: {dt}")
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    ##print(f"Screen height: {SCREEN_HEIGHT}")
   
    


if __name__ == "__main__":
    main()
