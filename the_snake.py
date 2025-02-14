from random import choice, randint

import pygame as pg

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
CENTER_SCREEN = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pg.display.set_caption('Змейка')

# Настройка времени:
clock = pg.time.Clock()


"""Объявляем родительский класс."""


class GameObject:
    """Инициализация."""

    def __init__(self, body_color=None):
        """Параментры родительского класса."""
        self.body_color = body_color
        self.position = CENTER_SCREEN

    def draw_cell(self):
        """Общая отрисовка ячейки объектов"""
        rect = pg.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, self.body_color, rect)
        pg.draw.rect(screen, BORDER_COLOR, rect, 1)

    def draw(self):
        """Отрисовка."""
        raise NotImplementedError('Ожидаем уточнение в дочерних классах')


"""Объявляем дочерние классы на базе
родительского класса GameObject."""


class Apple(GameObject):
    """Объявляем дочерний класс"""

    def __init__(self, body_color=APPLE_COLOR, center_position=CENTER_SCREEN):
        """Инициализация."""
        self.body_color = body_color
        self.center_position = center_position
        super().__init__(body_color)
        self.randomize_position()

    def randomize_position(self):
        """Устанавливаем случайное положение яблока."""
        while True:
            x = randint(0, GRID_WIDTH - 1)
            y = randint(0, GRID_HEIGHT - 1)
            self.position = (x * GRID_SIZE), (y * GRID_SIZE)
            if self.position not in self.center_position:
                break

    def draw(self):
        """Отрисовываем яблоко."""
        self.draw_cell()


class Snake(GameObject):
    """Объявляем дочерний класс"""

    def __init__(self, body_color=SNAKE_COLOR, next_direction=None):
        """Инициализация."""
        self.length = 1
        self.positions = CENTER_SCREEN
        self.body_color = body_color
        self.direction = RIGHT
        self.next_direction = next_direction
        self.position = None

    def update_direction(self):
        """Обновляем напавление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновняем позицию зиейки."""
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        new_x = head_x + dx * GRID_SIZE
        new_y = head_y + dy * GRID_SIZE
        new_head = (new_x % SCREEN_WIDTH, new_y % SCREEN_HEIGHT)
        self.last = self.positions[-1]
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self):
        """Отрисовка змейки."""
        for self.position in self.positions[:-1]:
            self.draw_cell()
        """Отрисовка головы змейки."""
        head_rect = pg.Rect(self.get_head_position(), (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, self.body_color, head_rect)
        pg.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        if self.last:
            """Затирание последнего сегмента."""
            last_rect = pg.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pg.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывание змейки в первоначальное состояние."""
        self.length = 1
        self.positions = CENTER_SCREEN
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None


def handle_keys(game_object):
    """Сбрасывает нажатие клавиш, чтобы изменить направление змейки."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pg.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pg.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pg.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основной цикл игры."""
    pg.init()
    apple = Apple()
    snake = Snake()
    while True:
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        # проверяем встречу змейки с яблоком
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
        # проверяем встречу змейки со своим хвостом
        elif snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            apple.randomize_position()
        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        pg.display.update()
        clock.tick(SPEED)
        pg.time.delay(200)


if __name__ == '__main__':
    main()
