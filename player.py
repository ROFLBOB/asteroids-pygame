import constants
import pygame
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape):
    shot_timer = 0

    def __init__(self, x, y):
        print("About to use PLAYER_RADIUS:", constants.PLAYER_RADIUS)
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_SPACE]:
            if self.shot_timer < 0:
                self.shoot()

        self.shot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        #create a new shot at the position of the player
        bullet = Shot(self.position.x,self.position.y,constants.SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        self.shot_timer = constants.PLAYER_SHOOT_COOLDOWN
