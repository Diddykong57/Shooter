import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #if nb_comet == 0
        if len(self.comet_event.all_comets) == 0:
            print("end_event")
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()


    def fall(self):
        self.rect.y += self.velocity

        # doesn't fall on floor
        if self.rect.y >= 550:
            self.remove()

            # no more fireball
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_move = False

        # fireball hit player
        if self.comet_event.game.check_collisions(
            self, self.comet_event.game.all_players
        ):
            self.remove()
            self.comet_event.game.player.damage(20)
