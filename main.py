#this allows us to use code from the open-source pygame lihbrary throughout this file
import pygame
import constants
from player import Player

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

    Player.containers = (updatable, drawable)

    player = Player(x = constants.SCREEN_WIDTH/2, y = constants.SCREEN_HEIGHT/2)

  

    while True:
        #get the quit button working
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill the screen blue
        screen.fill((0,0,255))

        for updatable_object in updatable:
            updatable_object.update(dt)
        
        for drawable_object in drawable:
            drawable_object.draw(screen)


        #update the screen
        pygame.display.flip()
        dt = timer.tick(60)/1000

if __name__ == "__main__":
    main()