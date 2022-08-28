import arcade
import entity
import settings as stg
from pygame.math import Vector2 as Vec


class Player(entity.BaseEntity):
    def __init__(self):
        super().__init__(stg.WINDOW_HEIGHT // 2, stg.WINDOW_WIDTH // 2, 100, 1, stg.BASE_VEL)
        self.dst = Vec(stg.WINDOW_HEIGHT // 2, stg.WINDOW_WIDTH // 2)
        self.change_dst = False

    def update_dst(self, x, y) -> None:
        self.dst = Vec(x, y)

    def on_update(self, dt: float) -> None:
        # move
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

    def on_mouse_press(self, x, y, button, modifiers) -> None:
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.update_dst(x, y)
            self.change_dst = True

    def on_mouse_release(self, x, y, button, modifiers) -> None:
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.change_dst = False

    def on_draw(self) -> None:
        arcade.draw_rectangle_filled(self.pos.x, self.pos.y, 25, 25, arcade.color.LIME)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.change_dst:
            self.update_dst(x, y)

