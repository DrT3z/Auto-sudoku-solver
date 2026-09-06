grid = [
    [0, 7, 0, 0, 2, 0, 8, 0, 0],
    [6, 0, 0, 0, 3, 0, 0, 7, 0],
    [0, 4, 8, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 2, 0, 0, 0, 0, 9],
    [5, 0, 0, 0, 1, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 8, 0],
    [2, 0, 0, 5, 0, 0, 0, 1, 0],
    [4, 0, 5, 9, 0, 0, 6, 0, 0]
]
#an example grid

def boxes(grid):
    box = [[],[],[],[],[],[],[],[],[]]
    a = 0
    i = 1
    for x in grid:
        for b, y in enumerate(x):
            box[b//3+a*3].append(y)
        if i != 3:
            i += 1
        else:
            a += 1
            i = 1
    return box

def solve(grid):
    emptySquares = []
    col = 0
    for x in grid:
        row = 0
        for y in x:
            if y == 0:
                emptySquares.append([row,col])
            row += 1
        col += 1

    def finished():
        for x in grid:
            for y in x:
                if y == 0:
                    return False
        return True
    
    order = 0
    valid = True
    while True:
        for x in range(grid[emptySquares[order][1]][emptySquares[order][0]] if not valid else 1, 10):
            if check(x, emptySquares[order][1], emptySquares[order][0], grid):
                valid = True
                grid[emptySquares[order][1]][emptySquares[order][0]] = x
                order += 1
                break 
            else:
                valid = False

        if not valid:
            grid[emptySquares[order][1]][emptySquares[order][0]] = 0
            order -= 1
            grid[emptySquares[order][1]][emptySquares[order][0]] += 1
            
        if finished():
            return grid     
            
        
        
def check(number, row, col, grid):
    grid[row][col] = number
    rows = []
    for x in range(9):
        rows.append(grid[x][col])
    if grid[row].count(number) > 1:
        return False
    elif rows.count(number) > 1:
        return False
    elif boxes(grid)[(row//3) * 3 + (col//3)].count(number) > 1:
        return False
    else:
        return True


#for x in solve(grid):
#    print(x)
