#this allows us to use code from the open-source pygame lihbrary throughout this file
import pygame
import constants
import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    


    player = Player(x = constants.SCREEN_WIDTH/2, y = constants.SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

  

    while True:
        #get the quit button working
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        print(player.shot_timer)
        #fill the screen blue
        screen.fill((0,0,255))

        for updatable_object in updatable:
            updatable_object.update(dt)
        
        for drawable_object in drawable:
            drawable_object.draw(screen)

        for individual_asteroid in asteroids:
            if player.check_collisions(individual_asteroid):
                print("Game over!")
                sys.exit()
            for individual_bullet in shots:
                if individual_asteroid.check_collisions(individual_bullet):
                    individual_bullet.kill()
                    individual_asteroid.split() 

        #update the screen
        pygame.display.flip()
        dt = timer.tick(60)/1000

if __name__ == "__main__":
    main()