# GENERAL IMPORTS
from typing import *
import random
import arcade
import pygame

# LOCAL IMPORTS
import player
import enemy
import settings as stg
import sys


Vec = pygame.math.Vector2





class Game(arcade.Window):
    def __init__(self):
        super().__init__(stg.WINDOW_WIDTH, stg.WINDOW_HEIGHT, stg.WINDOW_TITLE)
        self.set_fullscreen()
        self.set_update_rate(1/60)
        self.EXIT = False

        # Entities
        self.player = player.Player(self)
        self.enemies: List[enemy.Enemy] = []
        self.enemy_spawn_cool_down = 0.1
        self.enemy_spawn_t_counter = 0

    def setup(self):
        print("chuj")

    def on_update(self, dt: float):
        if self.EXIT:
            sys.exit(0)

        # Spawning enemies randomly
        self.enemy_spawn_t_counter += dt * random.gauss(1.1, 0.1)
        if self.enemy_spawn_t_counter >= self.enemy_spawn_cool_down:
            self.enemy_spawn_t_counter = 0
            pos = Vec(
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            ).normalize() * stg.WINDOW_R + Vec(stg.WINDOW_WIDTH//2, stg.WINDOW_HEIGHT//2)
            self.enemies.append(
                enemy.Enemy(
                    x=pos.x, y=pos.y,
                    hp=100, atk=100, vel=2000,
                    game=self)
            )

        self.player.on_update(dt)
        for enemy_i in self.enemies:
            enemy_i.on_update(dt)

    def on_draw(self):
        self.clear(arcade.color.BLACK)
        self.player.on_draw()
        for enemy_i in self.enemies:
            enemy_i.on_draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.EXIT = True

        self.player.on_key_press(symbol, modifiers)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.player.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        self.player.on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.on_mouse_motion(x, y, dx, dy)


def main():
    window = Game()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
