import pygame
from player import Player
from monster import Monster


# create game
class Game:

    def __init__(self):
        # generate player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        # generate group of monsters
        self.all_monsters = pygame.sprite.Group()

        self.pressed = {}
        self.spawn_monster()

    def check_collisions(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)