import tkinter as tk
from tkinter import messagebox, simpledialog

size = 4 #int(input("Enter the size of the grid: "))

class Group:
    def __init__(self, cel , target, op):
        self.cel = cel
        self.target = target
        self.op = op

def is_valid(grid, r, col, num):
    if num in grid[r]:
        return False
    for i in range(size):
        if grid[i][col] == num:
            return False
    return True
    
def grid_solver(grid, cells):
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

# cells =[]
# cages = int(input("Enter the number of cages: "))
# for i in range(1,cages + 1):
#     cell =input("Enter the cell coordinates (row colomn): ")
#     coor = list(map(int, cell.split()))
#     target = int(input("Enter the target number: "))
#     op = input("Enter the operation (+, -, *, /): ")
#     cells.append(Group(coor, target, op))

sample = [
    Group([(0,0), (1,0),(2,0)], 24, '*'), 
    Group([(0,1), (0,2)], 3, '+'), 
    Group([(1,1), (1,2)], 7, '+'), 
    Group([(2,1), (2,2)], 5, '+'), 
    Group([(0,3), (1,3),(2,3)], 6, '+'), 
    Group([(3,0), (3,1)], 2, '-'), 
    Group([(3,2), (3,3)], 2, '/'), 
]
solution = [[0] * size for _ in range(size)]
for r in solution:
    print(r)
if solve(solution, sample):
    print("Solution found:")
    for r in solution:
        print(r)
        
root = tk.Tk()
root.title("KenKen Solver")
for i in range(size):
    for c in range(size):
        b = tk.Button(root, width=6 , height=3, text= str(solution[i][c]))
        b.grid(row=i, column=c)
tk.Button(root, text="Solve", command=lambda: solve(solution, sample)).grid(row=size, column=0, columnspan=size)
root.mainloop()
