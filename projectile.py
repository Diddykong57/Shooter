import pygame


class Projectile(pygame.sprite.Sprite):

    # Constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle -= 0.8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # if projectile collide monster
        for monster in self.player.game.check_collisions(self, self.player.game.all_monsters):
            self.remove()

            #deal dmg
            monster.damage(self.player.attack)


        # if projectile is not visible
        if self.rect.x > 1080:
            # destroy projectile
            self.remove()