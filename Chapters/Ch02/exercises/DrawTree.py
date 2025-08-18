def drawTree(row, left, right) :
	mid = (left + right) // 2
	if (left <= right and row<ROWS) :
		map[row][mid] = 1
		drawTree(row + 1, left, mid - 1)
		drawTree(row + 1, mid + 1, right)

def printTree() :
    for i in range(ROWS) :
        for j in range(COLS) :
            if map[i][j] == 0 : print('-',end='')
            else: print('X',end='')
        print()

ROWS = 6
COLS = 64

map = [[0 for x in range(COLS)] for x in range(ROWS)] 

drawTree(0, 0, COLS-1)
printTree()

