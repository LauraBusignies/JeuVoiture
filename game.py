# coding : utf-8

# IMPORT
import pygame
import random
import time
import math
from player import Player
from enemy import Enemy

class Game:

    def __init__(self, screen) :
        self.player = Player(self, screen)
        self.enemy1 = Enemy(self, random.randint(280, 380), -200)
        self.enemy2 = Enemy(self, random.randint(457, 557), -600)
        self.enemy3 = Enemy(self, random.randint(633, 733), -10) 
        self.list_enemy = [self.enemy1, self.enemy2, self.enemy3] 
        self.list_random = [[280, 380], [457, 557], [633, 733]]
        self.pressed = {}
        self.defeat = False
        self.is_playing = False
        self.to_strat = True
        self.counter_score = 0
        # Permet d'agrementer le compteur de score
        self.counter_loop_score = 0
        


    def update(self, screen):
        #afficher le joueur et les voitures ennemis
        if self.is_playing :
            screen.blit(self.player.image, self.player.image_rect)
            screen.blit(self.enemy1.image, self.enemy1.rect)
            screen.blit(self.enemy2.image, self.enemy2.rect)
            screen.blit(self.enemy3.image, self.enemy3.rect)

            # Si un enemy sort de la map ou si il est en contact avec le player
            for enemy in self.list_enemy :  
                if enemy.rect.y > 720 or self.player.image_rect.colliderect(enemy.rect):
                    # si collision le player perd une vie
                    if self.player.image_rect.colliderect(enemy.rect) :
                        self.player.health -= 1
                        time.sleep(0.2)
                    # la voiture ennemi redémarre au debut
                    enemy.rect.y = random.randint(-600, -50)
                    enemy.rect.x = random.randint(self.list_random[self.list_enemy.index(enemy)][0], self.list_random[self.list_enemy.index(enemy)][1])
            
            # Mouvement voiture enemy et voiture player
            self.enemy1.move_enemy()
            self.movement()

            # Print les points de vie
            self.display_health(screen)
            self.display_score(screen)

            # Définis la fin de partie
            self.finish_game()


        # Pour chaque touche fléché du clavier, une méthode est appelé
    def movement(self) :
        if self.pressed.get(pygame.K_RIGHT) and self.player.image_rect.x + self.player.velocity < 735 :
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.image_rect.x - self.player.velocity > 275:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.image_rect.y - self.player.velocity > 0 :
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.image_rect.y + self.player.velocity < 580 :
            self.player.move_down()


    def display_score(self, screen) :
        # permet d'agrémenter le score pas trop vite
        self.counter_loop_score += 1
        if self.counter_loop_score == 20 :
            self.counter_score += 1
            self.counter_loop_score = 0
        
        # print le score sur le background
        font = pygame.font.Font(None, 45)
        text = font.render(str(self.counter_score),  1, (255,255,255))
        text_rect = text.get_rect()
        text_rect.x = screen.get_width() - 100
        text_rect.y = 10
        screen.blit(text, text_rect)

    def display_health(self, screen):
        self.player.health_image_rect.x = screen.get_width() - 250
        for player in range (self.player.health) :
            screen.blit(self.player.health_image, self.player.health_image_rect)
            self.player.health_image_rect.x += 30

    def finish_game(self):
        if self.player.health == 0 :
            self.is_playing = False
            self.defeat = True
            self.to_strat = False

    def game_replay(self):
        self.player.health = 3
        self.counter_score = 0
        self.enemy1.change_velocity = 5
        self.player.image_rect.x = 500
        self.player.image_rect.y = 570
        self.defeat = False
        self.is_playing = False
        self.to_strat = True

    def score_defeat(self, screen):
        font = pygame.font.Font(None, 45)
        text = font.render("SCORE :", 1, (255,255,255))
        text_rect = text.get_rect()
        text_rect.x = math.ceil(screen.get_width() /2)+ 340
        text_rect.y = 280
        screen.blit(text, text_rect)
     
        text = font.render(str(self.counter_score),  1, (255,255,255))
        text_rect = text.get_rect()
        text_rect.x = math.ceil(screen.get_width() /2)+ 340
        text_rect.y = 320
        screen.blit(text, text_rect)
