import random

class Game:
    def __init__(self, size=4):
        self.size = size
        self.score = 0
        self.grid = [[0] * size for _ in range(size)]
        self.game_over = False
        self.add_random_tile()
        self.add_random_tile()

    def reset(self):
        self.score = 0
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.game_over = False
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 0]
        if empty:
            i, j = random.choice(empty)
            self.grid[i][j] = 4 if random.random() < 0.1 else 2

    def move(self, direction):
        if self.game_over:
            return
        moved = False
        if direction == 'up':
            moved = self._move_up()
        elif direction == 'down':
            moved = self._move_down()
        elif direction == 'left':
            moved = self._move_left()
        elif direction == 'right':
            moved = self._move_right()
        if moved:
            self.add_random_tile()
        self.game_over = not self.can_move()

    def _move_up(self):
        moved = False
        for j in range(self.size):
            merged = [False] * self.size
            for i in range(1, self.size):
                if self.grid[i][j] != 0:
                    row = i
                    while row > 0 and self.grid[row - 1][j] == 0:
                        self.grid[row - 1][j] = self.grid[row][j]
                        self.grid[row][j] = 0
                        row -= 1
                        moved = True
                    if row > 0 and self.grid[row - 1][j] == self.grid[row][j] and not merged[row - 1]:
                        self.grid[row - 1][j] *= 2
                        self.score += self.grid[row - 1][j]
                        self.grid[row][j] = 0
                        merged[row - 1] = True
                        moved = True
        return moved

    def _move_down(self):
        moved = False
        for j in range(self.size):
            merged = [False] * self.size
            for i in range(self.size - 2, -1, -1):
                if self.grid[i][j] != 0:
                    row = i
                    while row < self.size - 1 and self.grid[row + 1][j] == 0:
                        self.grid[row + 1][j] = self.grid[row][j]
                        self.grid[row][j] = 0
                        row += 1
                        moved = True
                    if row < self.size - 1 and self.grid[row + 1][j] == self.grid[row][j] and not merged[row + 1]:
                        self.grid[row + 1][j] *= 2
                        self.score += self.grid[row + 1][j]
                        self.grid[row][j] = 0
                        merged[row + 1] = True
                        moved = True
        return moved

    def _move_left(self):
        moved = False
        for i in range(self.size):
            merged = [False] * self.size
            for j in range(1, self.size):
                if self.grid[i][j] != 0:
                    col = j
                    while col > 0 and self.grid[i][col - 1] == 0:
                        self.grid[i][col - 1] = self.grid[i][col]
                        self.grid[i][col] = 0
                        col -= 1
                        moved = True
                    if col > 0 and self.grid[i][col - 1] == self.grid[i][col] and not merged[col - 1]:
                        self.grid[i][col - 1] *= 2
                        self.score += self.grid[i][col - 1]
                        self.grid[i][col] = 0
                        merged[col - 1] = True
                        moved = True
        return moved

    def _move_right(self):
        moved = False
        for i in range(self.size):
            merged = [False] * self.size
            for j in range(self.size - 2, -1, -1):
                if self.grid[i][j] != 0:
                    col = j
                    while col < self.size - 1 and self.grid[i][col + 1] == 0:
                        self.grid[i][col + 1] = self.grid[i][col]
                        self.grid[i][col] = 0
                        col += 1
                        moved = True
                    if col < self.size - 1 and self.grid[i][col + 1] == self.grid[i][col] and not merged[col + 1]:
                        self.grid[i][col + 1] *= 2
                        self.score += self.grid[i][col + 1]
                        self.grid[i][col] = 0
                        merged[col + 1] = True
                        moved = True
        return moved

    def can_move(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return True
                for d in [(0, 1), (1, 0)]:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < self.size and 0 <= nj < self.size and self.grid[i][j] == self.grid[ni][nj]:
                        return True
        return False