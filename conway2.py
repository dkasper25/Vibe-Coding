

import tkinter as tk

CELL_SIZE = 12
GRID_SIZE = 50
DEAD_COLOR = "white"
ALIVE_COLOR = "black"
UPDATE_DELAY = 200  # milliseconds

class GameOfLife:
    def __init__(self, master):
        self.master = master
        self.running = False
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.rects = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        self.canvas = tk.Canvas(master, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, bg="gray")
        self.canvas.pack()

        self.start_button = tk.Button(master, text="Start", command=self.toggle_running)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.clear_button = tk.Button(master, text="Clear", command=self.clear)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.draw_grid()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def draw_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=DEAD_COLOR, outline="lightgray")
                self.rects[i][j] = rect

    def on_canvas_click(self, event):
        if self.running:
            return
        row = event.y // CELL_SIZE
        col = event.x // CELL_SIZE
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            self.grid[row][col] ^= 1
            color = ALIVE_COLOR if self.grid[row][col] else DEAD_COLOR
            self.canvas.itemconfig(self.rects[row][col], fill=color)

    def toggle_running(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="Pause")
            self.run_simulation()
        else:
            self.start_button.config(text="Start")

    def run_simulation(self):
        if not self.running:
            return
        new_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i][j]:
                    new_grid[i][j] = 1 if neighbors in (2, 3) else 0
                else:
                    new_grid[i][j] = 1 if neighbors == 3 else 0
        self.grid = new_grid
        self.update_canvas()
        self.master.after(UPDATE_DELAY, self.run_simulation)

    def count_neighbors(self, row, col):
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r = (row + dr) % GRID_SIZE
                c = (col + dc) % GRID_SIZE
                count += self.grid[r][c]
        return count
    def update_canvas(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                color = ALIVE_COLOR if self.grid[i][j] else DEAD_COLOR
                self.canvas.itemconfig(self.rects[i][j], fill=color)

    def clear(self):
        self.running = False
        self.start_button.config(text="Start")
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.update_canvas()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conway's Game of Life")
    game = GameOfLife(root)
    root.mainloop()