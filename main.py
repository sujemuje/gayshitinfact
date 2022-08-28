import arcade
import pygame
# MY IMPORTS
import player
import enemy
import settings as stg
import sys


Vec = pygame.math.Vector2


class Game(arcade.Window):
    def __init__(self):
        super().__init__(stg.WINDOW_WIDTH, stg.WINDOW_HEIGHT, stg.WINDOW_TITLE)
        self.player = player.Player()
        self.set_vsync(True)
        self.EXIT = False

    def setup(self):
        pass

    def on_draw(self):
        self.clear(arcade.color.BLACK)
        self.player.on_draw()

    def on_update(self, delta_time: float):
        if self.EXIT:
            sys.exit(0)

        self.player.on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.EXIT = True

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
