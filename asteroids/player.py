from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from circleshape import CircleShape
import pygame
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from shot import Shot
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    "Unser Dreieck-Raumschiff"
    

    def __init__(self, coord_x, coord_y):
        
        super().__init__(coord_x,coord_y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
                self.shoot()
                




    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector  

    def shoot(self):
        
        if self.cooldown_timer > 0:
            pass
        else: 
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot1 = Shot(self.position.x, self.position.y)
            unit_vector = pygame.Vector2(0, 1)
            rotated_vector = unit_vector.rotate(self.rotation)
            shot1.velocity = rotated_vector * PLAYER_SHOOT_SPEED
        
    
            
