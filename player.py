import arcade
import entity
import settings as stg
from pygame.math import Vector2 as Vec

import skill
import skills
from typing import *


class Player(entity.BaseEntity):
    def __init__(self, game):
        super().__init__(stg.WINDOW_HEIGHT // 2, stg.WINDOW_WIDTH // 2, 100, 1, stg.BASE_VEL, game)
        self.dst = Vec(stg.WINDOW_HEIGHT // 2, stg.WINDOW_WIDTH // 2)
        self.change_dst = False
        self.sprite = arcade.sprite.Sprite('based.png')
        self.skills: List[skill.BaseSkill] = [
            skills.SkillQ(self)
        ]

    def update_dst(self, x, y) -> None:
        self.dst = Vec(x, y)

    def on_update(self, dt: float) -> None:
        # move
        for s in self.skills:
            s.on_update(dt)

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
        for i in range(len(self.skills)):
            self.skills[i].on_draw(i)
        # arcade.draw_rectangle_filled(self.pos.x, self.pos.y, 25, 25, arcade.color.LIME)

    def on_mouse_press(self, x, y, button, modifiers) -> None:
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.update_dst(x, y)
            self.change_dst = True

    def on_mouse_release(self, x, y, button, modifiers) -> None:
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.change_dst = False

    def on_mouse_motion(self, x, y, dx, dy):
        if self.change_dst:
            self.update_dst(x, y)

    def on_key_press(self, key, modifier) -> None:
        keys = [
            arcade.key.Q,
            arcade.key.W,
            arcade.key.E,
            arcade.key.R,
        ]
        if key in keys:
            try:
                self.skills[keys.index(key)].use(
                    self.game._mouse_x,
                    self.game._mouse_y
                )
            except KeyError:
                pass
