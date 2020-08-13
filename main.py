# coding : utf-8

# IMPORT
import pygame
import math
from player import Player
from game import Game

pygame.init()
pygame.display.set_caption("Jeu de voiture")
screen = pygame.display.set_mode((1080 ,720))

background = pygame.image.load('image/background.png').convert()
background_defaite = pygame.image.load('image/bg_defeat.png').convert()
button_replay = pygame.image.load('image/replay.png').convert()
button_strat = pygame.image.load('image/strat.png').convert()
background_strat = pygame.image.load('image/background_start.png').convert()
backgroundXXL = pygame.image.load('image/backgroundXXL.png').convert()


game = Game(screen)
running = True
# pour faire bouger la map pas trop vite
counter = 0


backgroundXXL_rect = backgroundXXL.get_rect()
backgroundXXL_rect.x = 0
backgroundXXL_rect.y = -2160


button_replay_rect = button_replay.get_rect()
button_replay_rect.x = math.ceil(screen.get_width() / 2 - 120)
button_replay_rect.y = 550

button_strat_rect = button_strat.get_rect()
button_strat_rect.x = 100
button_strat_rect.y = 560




while running :

    if game.to_strat :
        screen.blit(background_strat, (0,0))
        screen.blit(button_strat, button_strat_rect)

    elif game.is_playing :
        # screen.blit(background, (0, 0))
        # tout les 5 tour de boucle la position Y de la map change
        counter += 1
        if counter == 5 :
            backgroundXXL_rect.y += 1
            counter = 0
        #Si j'arrive au bout de la map je repars a zéro    
        if backgroundXXL_rect.y == 0 :
            backgroundXXL_rect.y = -2160
        screen.blit(backgroundXXL, backgroundXXL_rect)
        game.update(screen)

    elif game.defeat :
        screen.blit(background_defaite, (0, 0))
        screen.blit(button_replay, button_replay_rect)
        game.score_defeat(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN and game.is_playing == False :

            if button_strat_rect.collidepoint(event.pos) and game.to_strat == True and game.is_playing == False :
                game.to_strat = False
                game.is_playing = True
            elif button_replay_rect.collidepoint(event.pos):
                game.game_replay()
                print("replay")



    pygame.display.flip()
        
