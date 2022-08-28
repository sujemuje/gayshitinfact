import arcade


class BaseSkill:
    def __init__(self, player, cd, icon_file_name, *a, **kw):
        self.player = player
        self.cd = cd
        self.icon = arcade.Sprite(icon_file_name, *a, **kw)
        self.icon.set_position(100, 100)
        self.last_cast_time = 0

    def available(self) -> bool:
        return self.cd <= self.last_cast_time

    def on_update(self, dt) -> None:
        self.last_cast_time += dt

    def on_draw(self, i) -> None:
        self.icon.draw()
        # if not self.available():
        arcade.draw_arc_filled(100, 100, 100, 100, (0x00, 0x00, 0x00, 0x80),
                               min(360,
                                   360 * (self.last_cast_time / self.cd)
                                   ) + 90
                               , 360 + 90, num_segments=100)

    def use(self, *a, **kw):
        if self.available():
            self.cast(*a, **kw)
            self.last_cast_time = 0

    def cast(self, mouse_x, mouse_y) -> None:
        raise NotImplementedError()
