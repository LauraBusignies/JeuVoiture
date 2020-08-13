# coding : utf-8

# IMPORT
import pygame
import random

class Enemy :

    def __init__(self, game, x, y) :
        self.game = game
        self.image = pygame.image.load('image/carRed.png')
        self.health = 3
        self.velocity = 5
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rang_velocity = [500, 1000, 1500]
        self.counter_move = 0
        self.change_velocity = 5

    def more_speed(self):
        if self.game.counter_score in self.rang_velocity :
            self.change_velocity -= 1
            self.game.player.health += 1
            del self.rang_velocity[0]

    def move_enemy(self):

        
        self.counter_move += 1
        # print(f'{self.counter_move} / {self.change_velocity}')
        if self.counter_move == self.change_velocity :
            self.more_speed()
            self.game.enemy1.rect.y += self.game.enemy1.velocity
            self.game.enemy2.rect.y += self.game.enemy2.velocity
            self.game.enemy3.rect.y += self.game.enemy3.velocity
            self.counter_move = 0
