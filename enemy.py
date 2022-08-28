import arcade
import pygame.math

import entity
import random


RND_DST_T = 1
MOV_RAND_COEF = .3
assert 0 <= MOV_RAND_COEF <= 1


class Enemy(entity.BaseEntity):
    def __init__(self, x, y, hp, atk, vel, game):
        super().__init__(x, y, hp, atk, vel, game)
        self.dst = game.player.pos
        self.rnd_counter = 0
        self.sprite = arcade.Sprite('radi.png', 0.5)

    def move_rand(self):
        rand_vec = pygame.math.Vector2(
            random.uniform(-10, 10),
            random.uniform(-10, 10)
        ).normalize()
        target_vec = (self.game.player.pos - self.pos).normalize()
        total_vec = (rand_vec * MOV_RAND_COEF + target_vec * (1 - MOV_RAND_COEF)).normalize() * 1000
        self.dst = self.pos + total_vec

    def on_update(self, dt) -> None:
        self.rnd_counter += dt * random.gauss(1.1, 0.1)
        if self.rnd_counter >= RND_DST_T:
            self.rnd_counter = 0
            self.move_rand()
        if self.pos != self.dst:
            if self.movable():
                dist_to_dst = (self.pos - self.dst).length()
                move_len = self.base_vel * self.vel_mod * dt
                if move_len >= dist_to_dst:
                    self.pos = self.dst
                else:
                    self.pos += (self.dst - self.pos).normalize() * move_len
            else:
                pass

    def on_draw(self) -> None:
        self.sprite.set_position(self.pos.x, self.pos.y)
        self.sprite.draw()
