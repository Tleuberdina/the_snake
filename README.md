### the_snake - классическая игра «Змейка».

### Возможности игры
Игрок управляет змейкой, которая движется по игровому полю в одном из четырех направлении (вверх, вниз, вправо, влево). Змейка не может останавливаться или двигаться назад. При столкновении змейки с границей игрового поля – змейка появляется с противоположной стороны игрового поля. На экран в случайных координатах появляется яблоко, при встрече с яблоком - змейка увеличивается на одну ячейку. При столкновении змейки с собой – игра начинается сначала. 

### Технологии:
* Python
* Pygame
* ООП

### Шаги запуска игры:
* Клонируйте репозиторий: git clone git@github.com:Tleuberdina/the_snake.git
cd the_snake
* разверните и активируйте виртуальное окружение
* Команда для Windows:
python -m venv venv
source venv/Scripts/activate
* Команда для Linux и macOS:
python3 -m venv venv
source venv/bin/activate
* Установите зависимости проекта: pip install -r requirements.txt
* запуск игры: python the_snake.py
