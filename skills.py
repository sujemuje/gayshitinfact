import skill
import particle
import arcade
from pygame.math import Vector2 as Vec


class FireballProjectile(particle.BaseParticle):
    def __init__(self, pos: Vec, trajectory: Vec):
        self.pos = pos
        self.speed = 1
        self.sprite = arcade.sprite.Sprite('holy shit.png')
        self.trajectory = trajectory

    def on_update(self, dt) -> None:
        self.pos += self.trajectory * dt

    def on_draw(self) -> None:
        self.sprite.set_position(self.pos.x, self.pos.y)
        self.sprite.draw()

    def removable(self) -> bool:
        return True


class SkillQ(skill.BaseSkill):
    def __init__(self, player):
        super().__init__(player, 2, 'radi.png', .3)
        self.projectiles: list[FireballProjectile] = []

    def on_update(self, dt) -> None:
        super().on_update(dt)  # UI interface management in BaseSkill class
        for projectile in self.projectiles:
            projectile.on_update(dt)

    def on_draw(self, i) -> None:
        super().on_draw(i)  # UI interface management in BaseSkill class
        for projectile in self.projectiles:
            projectile.on_draw()

    def cast(self, mouse_x, mouse_y) -> None:
        v = Vec(mouse_x, mouse_y) - self.player.pos
        if v == Vec(0, 0): v = Vec(1, 0)
        else: v = v.normalize()
        self.projectiles.append(FireballProjectile(self.player.pos, v))
