import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent


# create game
class Game:

    def __init__(self):
        # game status
        self.is_playing = False

        # generate player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        # generate event
        self.comet_event = CometFallEvent(self)

        # generate group of monsters
        self.all_monsters = pygame.sprite.Group()

        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #restart all game + game_await
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        # set player image
        screen.blit(self.player.image, self.player.rect)

        # update hp player
        self.player.update_health_bar(screen)

        # update bar_event
        self.comet_event.update_bar(screen)

        # get projectiles of player
        for projectile in self.player.all_projectiles:
            projectile.move()

        # get monster
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # get comet
        for comet in self.comet_event.all_comets:
            comet.fall()

        # set Group_projectiles
        self.player.all_projectiles.draw(screen)

        # set Group_monster
        self.all_monsters.draw(screen)

        #set Group_comet
        self.comet_event.all_comets.draw(screen)

        # check movement by keypress
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collisions(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)