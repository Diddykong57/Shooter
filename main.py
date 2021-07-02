import pygame
from game import Game

pygame.init()

# Générer render
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# load image
background = pygame.image.load('assets/bg.jpg')

# load game
game = Game()

running = True

while running:

    # set background
    screen.blit(background, (0, -200))

    # set player image
    screen.blit(game.player.image, game.player.rect)

    # get projectiles of player
    for projectile in game.player.all_projectiles:
        projectile.move()

    # get monster
    for monster in game.all_monsters:
        monster.forward()

    # set Group_projectiles
    game.player.all_projectiles.draw(screen)

    # set Group_monster
    game.all_monsters.draw(screen)

    # check movement by keypress
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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