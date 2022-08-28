import random

import arcade
import pygame
# MY IMPORTS
import player
import enemy
import settings
import settings as stg
import sys


from typing import *


Vec = pygame.math.Vector2


enemy_spawn_cool_down = 1


class Game(arcade.Window):
    def __init__(self):
        super().__init__(stg.WINDOW_WIDTH, stg.WINDOW_HEIGHT, stg.WINDOW_TITLE)
        self.player = player.Player(self)
        self.set_vsync(True)
        self.EXIT = False
        self.enemies: List[enemy.Enemy] = []
        self.enemy_spawn_t_counter = 0

    def setup(self):
        # for _ in range(5):
        #     self.enemies.append(
        #         enemy.Enemy(0, 0, 100, 100, 200, self)
        #     )
        pass

    def on_draw(self):
        self.clear(arcade.color.BLACK)
        self.player.on_draw()
        for enemy_i in self.enemies:
            enemy_i.on_draw()

    def on_update(self, delta_time: float):
        self.enemy_spawn_t_counter += delta_time * random.gauss(1.1, 0.1)
        if self.enemy_spawn_t_counter >= enemy_spawn_cool_down:
            self.enemy_spawn_t_counter = 0
            pos = Vec(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * settings.WINDOW_R
            self.enemies.append(
                enemy.Enemy(pos.x, pos.y, 100, 100, 200, self)
            )

        if self.EXIT:
            sys.exit(0)

        self.player.on_update(delta_time)
        for enemy_i in self.enemies:
            enemy_i.on_update(delta_time)

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
    window.set_fullscreen()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
