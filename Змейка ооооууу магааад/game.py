import os
import sys
import time
import random
import threading

WIDTH, HEIGHT = 10, 20

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

class Tetris:
    def __init__(self):
        self.field = [[0]*WIDTH for _ in range(HEIGHT)]
        self.score = 0
        self.new_piece()
        self.game_over = False
        self.lock = threading.Lock()
        self.last_input = None

    def new_piece(self):
        self.shape = random.choice(SHAPES)
        self.x = WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def collide(self, x, y, shape):
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    if x + j < 0 or x + j >= WIDTH or y + i >= HEIGHT:
                        return True
                    if y + i >= 0 and self.field[y + i][x + j]:
                        return True
        return False

    def freeze(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.field[self.y + i][self.x + j] = 1
        self.clear_lines()
        self.new_piece()
        if self.collide(self.x, self.y, self.shape):
            self.game_over = True

    def clear_lines(self):
        new_field = [row for row in self.field if any(cell == 0 for cell in row)]
        lines_cleared = HEIGHT - len(new_field)
        self.score += lines_cleared
        while len(new_field) < HEIGHT:
            new_field.insert(0, [0]*WIDTH)
        self.field = new_field

    def move(self, dx, dy):
        if not self.collide(self.x + dx, self.y + dy, self.shape):
            self.x += dx
            self.y += dy

    def rotate_piece(self):
        new_shape = rotate(self.shape)
        if not self.collide(self.x, self.y, new_shape):
            self.shape = new_shape

    def drop(self):
        while not self.collide(self.x, self.y + 1, self.shape):
            self.y += 1
        self.freeze()

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        temp_field = [row[:] for row in self.field]
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell and 0 <= self.y + i < HEIGHT and 0 <= self.x + j < WIDTH:
                    temp_field[self.y + i][self.x + j] = 2
        print("Счёт:", self.score)
        for row in temp_field:
            print('|' + ''.join('█' if cell else ' ' for cell in row) + '|')
        print('-' * (WIDTH + 2))
        print("Управление: a-влево d-вправо s-вниз w-поворот q-выход")

    def input_thread(self):
        while not self.game_over:
            key = sys.stdin.read(1)
            with self.lock:
                self.last_input = key

    def run(self):
        threading.Thread(target=self.input_thread, daemon=True).start()
        while not self.game_over:
            self.draw()
            time.sleep(0.3)
            with self.lock:
                key = self.last_input
                self.last_input = None
            if key == 'a':
                self.move(-1, 0)
            elif key == 'd':
                self.move(1, 0)
            elif key == 's':
                if not self.collide(self.x, self.y + 1, self.shape):
                    self.y += 1
                else:
                    self.freeze()
            elif key == 'w':
                self.rotate_piece()
            elif key == 'q':
                break
            else:
                if not self.collide(self.x, self.y + 1, self.shape):
                    self.y += 1
                else:
                    self.freeze()
        self.draw()
        print("Игра окончена!")

if __name__ == "__main__":
    print("Запуск Тетриса в терминале. Нажмите любую клавишу для старта.")
    input()
    game = Tetris()
    game.run()