import pygame
import math
from game import Game

pygame.init()

# Générer render
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# load image
background = pygame.image.load('assets/bg.jpg')

# load banner
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#load btn_start
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# load game
game = Game()

running = True

while running:

    # set background
    screen.blit(background, (0, -200))

    # if game started
    if game.is_playing:
        game.update(screen)

    #if game doesn't start
    else:
        #screen welcome
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # update screen
    pygame.display.flip()

    # Close on click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # press key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # if space => projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                #game start
                game.start()