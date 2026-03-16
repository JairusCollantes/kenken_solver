size = int(input("Enter the size of the grid: "))

class Group:
    def __init__(self, cel , target, op):
        self.cel = cel
        self.target = target
        self.op = op

def solve(cells, size):
    # This function will contain the logic to solve the KenKen puzzle
    pass

cells =[]
# cages = int(input("Enter the number of cages: "))
# for i in range(1,cages + 1):
#     cell =input("Enter the cell coordinates (row colomn): ")
#     coor = list(map(int, cell.split()))
#     target = int(input("Enter the target number: "))
#     op = input("Enter the operation (+, -, *, /): ")
#     cells.append(Group(coor, target, op))

solution = [[0] * size for _ in range(size)]
for r in solution:
    print(r)