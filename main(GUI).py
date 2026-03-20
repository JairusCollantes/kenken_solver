import tkinter as tk
from tkinter import messagebox, simpledialog

size = 4 #int(input("Enter the size of the grid: "))

cells = {}
selected_cells = []
cages = []
grid = [[0] * size for _ in range(size)]

def is_valid( r, col, num): #this checks if it is allowed to place the number in the cell
    if num in grid[r]:
        return False
    for i in range(size):
        if grid[i][col] == num:
            return False
    return True
    
def grid_solver(grid): #This is to solve the values of the grouped cells
    values = []
    for r, c  in cells.cel:
        v = grid[r][c]
        if v == 0:
            return True
        values.append(v)
    
    if cells.op == '+':
        return sum(values) == cells.target
    elif cells.op == '-':
        a, b = values
        return abs(a - b) == cells.target
    elif cells.op == '*':
        product = 1
        for v in values:
            product *= v
        return product == cells.target
    elif cells.op == '/':
        return (max(values) / min(values)) == cells.target
    return False
    
def solve(grid, cells):
    # This function will contain the logic to solve the KenKen puzzle
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                for num in range(1, size + 1):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if all(grid_solver(grid, cg) for cg in cells):
                            if solve(grid, cells):
                                return True
                        grid[i][j] = 0
                return False
    return True
solution = None
sample = None
root = tk.Tk()
root.title("KenKen Solver")
for i in range(size):
    for c in range(size):
        b = tk.Button(root, width=6 , height=3, text="")
        b.grid(row=i, column=c)
tk.Button(root,text="Create Cage",command= None).grid(row=size,column=0,columnspan=2)
tk.Button(root,text="Solve Puzzle",command=None).grid(row=size,column=2,columnspan=2)
root.mainloop()