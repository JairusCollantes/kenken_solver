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
    
def grid_solver(cages): #This is to solve the values of the grouped cells
    values = []
    for r, c  in cages[0]:
        v = grid[r][c]
        if v == 0:
            return True
        values.append(v)
    target, op = cages[1], cages[2]
    
    if op == '+':
        return sum(values) == target if len(values) == len(cages[0]) else sum(values) <= target
    elif op == '-':
        a, b = values
        return abs(a - b) == target
    elif op == '*':
        product = 1
        for v in values:
            product *= v
        return product == target if len(values) == len(cages[0]) else product <= target
    elif op == '/':
        a,b = values
        return (max(a,b) / min(a,b)) == target

def select(r,c):
    if (r,c) in selected_cells:
        selected_cells.remove((r,c))
        cells[(r,c)].config(bg="white")
    else:
        selected_cells.append((r,c))
        cells[(r,c)].config(bg="pink")
        
def create_cage():
    if not selected_cells:
        messagebox.showerror("Error", "No cells selected for the cage.")
        return
    target = simpledialog.askinteger("Input", "Enter the target number:")
    op = simpledialog.askstring("Input", "Enter the operation (+, -, *, /):")
    if op not in ['+', '-', '*', '/'] or target is None:
        messagebox.showerror("Error", "Invalid operation or target.")
        return
    cages.append((selected_cells.copy(), target, op))
    for r, c in selected_cells:
        cells[(r,c)].config(bg="lightblue", text = f"{target}{op}")
    selected_cells.clear()
    
def solve():
    # This function will contain the logic to solve the KenKen puzzle
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                for num in range(1, size + 1):
                    if is_valid(i, j, num):
                        grid[i][j] = num
                        if all(grid_solver(cg) for cg in cages):
                            if solve():
                                return True
                        grid[i][j] = 0
                return False
    return True

def solve_button():
    global grid
    grid = [[0] * size for _ in range(size)]
    if solve():
        for i in range(size):
            for j in range(size):
                cells[(i,j)].config(text=str(grid[i][j]))
    else:
        messagebox.showinfo("Result", "No solution found.")
solution = None
sample = None
root = tk.Tk()
root.title("KenKen Solver")
for i in range(size):
    for c in range(size):
        b = tk.Button(root, width=6 , command = lambda r=i ,c=c: select(r,c), height=3, text="", bg = "white")
        b.grid(row=i, column=c)
        b.grid(row=i, column=c)
        cells[(i,c)] = b
tk.Button(root,text="Create Cage",command=  create_cage).grid(row=size,column=0,columnspan=2)
tk.Button(root,text="Solve Puzzle",command= solve_button).grid(row=size,column=2,columnspan=2)
root.mainloop()