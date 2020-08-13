# coding : utf-8

# IMPORT
import pygame

class Player :

    def __init__(self, game, screen) :
        self.game = game
        self.image = pygame.image.load('image/carBlue.png')
        self.health_image = pygame.image.load('image/health.png')

        self.health = 3
        self.velocity = 1
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 500
        self.image_rect.y = 570

        self.health_image_rect = self.health_image.get_rect()
        self.health_image_rect.x = screen.get_width() - 200
        self.health_image_rect.y = 10

    def move_right(self):
        self.image_rect.x += self.velocity
    
    def move_left(self):
        self.image_rect.x -= self.velocity

    def move_up(self):
        self.image_rect.y -= self.velocity

    def move_down(self):
        self.image_rect.y += self.velocity
