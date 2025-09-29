import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk

def update_board(board):
    rows, cols = len(board), len(board[0])
    new_board = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            live_neighbors = sum(
                board[i][j]
                for i in range(r-1, r+2)
                for j in range(c-1, c+2)
                if (0 <= i < rows and 0 <= j < cols and (i != r or j != c))
            )
            
            if board[r][c] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[r][c] = 0
                else:
                    new_board[r][c] = 1
            else:
                if live_neighbors == 3:
                    new_board[r][c] = 1
                    
    return new_board


def conway(board, steps, disp=False):
    if disp:
        fig, ax = plt.subplots()
        img = ax.imshow(board, cmap='binary')
        
        def animate(i):
            nonlocal board
            board = update_board(board)
            img.set_array(board)
            return [img]
        
        ani = animation.FuncAnimation(fig, animate, frames=steps, interval=200, blit=True)
        plt.show()
    else:
        for _ in range(steps):
            board = update_board(board)
        return board

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]

conway(board, 50, disp=True)
