class BaseParticle:
    def on_draw(self) -> None:
        raise NotImplementedError()

    def on_update(self, dt) -> None:
        raise NotImplementedError()

    def removable(self) -> bool:
        raise NotImplementedError()
