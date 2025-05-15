import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(x, y)
    asteroidField = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for drawable in Player.containers[1]:
            drawable.draw(screen)

        dt = fps.tick(60) / 1000
        Player.containers[0].update(dt)
        player.timer -= dt

        for obj in asteroids:
            if obj.collision_check(player):
                print("Game over!")
                sys.exit(1)
            for shot in shots:
                if obj.collision_check(shot):
                    obj.split()
                    shot.kill()
        pygame.display.flip()

if __name__ == "__main__":
    main()
