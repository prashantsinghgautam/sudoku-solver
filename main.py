import numpy as np
sudoko = []
print("Please use '0' in place of blank spaces")
for i in range(9):
    row = list(input("Enter the elements of row {} without any ',' ' ': ".format(i+1)))
    row = [int(i) for i in row]
    sudoko.append(row)
print(np.matrix(sudoko))

def possible(y,x,n):
    global sudoko
    for i in range(0,9):
        if sudoko[y][i] == n:
            return False
    for i in range(0,9):
        if sudoko[i][x] == n:
            return False
    b_y = (y//3)*3
    b_x = (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoko[b_y+i][b_x+j]==n:
                return False
    return True
def solve():
    for y in range(0,9):
        for x in range(0,9):
            if sudoko[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        sudoko[y][x] = n
                        solve()
                        sudoko[y][x] = 0
                return
    print(np.matrix(sudoko))
   
solve()
