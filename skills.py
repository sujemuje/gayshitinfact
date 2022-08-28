import copy
import settings
import skill
import particle
import arcade
from pygame.math import Vector2 as Vec


class FireballProjectile(particle.BaseParticle):
    def __init__(self, player, pos: Vec, trajectory: Vec):
        self.player = player
        self.pos = pos
        self.speed = 1000
        self.sprite = arcade.sprite.Sprite('holy shit.png', scale=.2)
        self.trajectory = trajectory
        self.rm = False

    def on_update(self, dt) -> None:
        self.pos += self.trajectory * dt * self.speed
        if -500 > self.pos.x or self.pos.x > settings.WINDOW_WIDTH + 500:
            self.rm = True
        if -500 > self.pos.y or self.pos.y > settings.WINDOW_HEIGHT + 500:
            self.rm = True
        for enemy in self.player.game.enemies:
            if self.sprite.collides_with_sprite(enemy.sprite):
                self.player.game.enemies.remove(enemy)

    def on_draw(self) -> None:
        self.sprite.set_position(self.pos.x, self.pos.y)
        self.sprite.draw()

    def removable(self) -> bool:
        return self.rm


class SkillQ(skill.BaseSkill):
    def __init__(self, player):
        super().__init__(player, 2, 'radi.png', .3)
        self.projectiles: list[FireballProjectile] = []

    def on_update(self, dt) -> None:
        super().on_update(dt)  # UI interface management in BaseSkill class
        for projectile in self.projectiles:
            projectile.on_update(dt)
            if projectile.removable():
                self.projectiles.remove(projectile)

    def on_draw(self, i) -> None:
        super().on_draw(i)  # UI interface management in BaseSkill class
        for projectile in self.projectiles:
            projectile.on_draw()

    def cast(self, mouse_x, mouse_y) -> None:
        player_pos = Vec(self.player.pos.x, self.player.pos.y)
        v = Vec(mouse_x, mouse_y) - player_pos
        if v == Vec(0, 0):
            v = Vec(1, 0)
        else:
            v = v.normalize()
        self.projectiles.append(FireballProjectile(self.player, player_pos, v))
