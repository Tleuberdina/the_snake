"""Объявляем родительский класс."""


class GameObject:
    """Инициализация."""

    def __init__(self):
        """Инициализация."""
        self.position = None
        self.body_color = None

    def draw(self):
        """Отрисовка."""
        pass
