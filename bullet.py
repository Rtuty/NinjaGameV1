import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('pictures/suriken.png')
        self.rotate_image = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor
        self.angle = 0


    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.rotate_image = pygame.transform.rotate(self.image, self.angle)
        self.angle += 4
    def draw_bullet(self):
        self.screen.blit(self.rotate_image, self.rect)
