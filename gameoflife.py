import random
import time
import os
import matplotlib
from matplotlib import pyplot as plt

class GameofLife:

    def initGrid(self, cols, rows, array):

        """
        Initialize the grid randomly with alive and dead cells.
        """

        for i in range(rows):
            arrayRow = []
            for j in range(cols):
                if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                    arrayRow += [-1]
                else:
                    ran = random.randint(0,3)
                    if ran == 0:
                        arrayRow += [1]
                    else:
                        arrayRow += [0]
            array += [arrayRow]

    
    def drawGrid(self, cols, rows, array, genNo):

        """
        Display the grid.
        """
        
        os.system("cls")
        print("Game of Life")
        print("Gen --> " + str(genNo))

        for i in range(rows):
            for j in range(cols):
                if array[i][j] == -1:
                    print(" # ", end=" ")
                elif array[i][j] == 1:
                    print(" " + chr(9632) + " ", end=" ")
                else:
                    print(" " + chr(9633) + " ", end=" ")
            print("\n")

    def get_neighbours(self, x, y, array):

        """
        Fetch the neigbours of a cell and apply the rules.
        """

        nCount = 0
        for j in range(y-1,y+2):
            for i in range(x-1,x+2):
                if not(i == x and j == y):
                    if array[i][j] != -1:
                        nCount += array[i][j]
        if array[x][y] == 1 and nCount < 2:         #Rule 1
            return 0
        if array[x][y] == 1 and nCount > 3:         #Rule 3
            return 0
        if array[x][y] == 0 and nCount == 3:        #Rule 4
            return 1
        else:
            return array[x][y]

    def updateGrid(self,cols, rows, cur, nxt):
        
        """
        Update the grid with the new state after applying the rules.
        """

        for i in range(1,rows-1):
            for j in range(1,cols-1):
                nxt[i][j] = grid.get_neighbours(i, j, cur)
                

if __name__ == "__main__":
    
    while True:
        try:

            ROWS = int(input("Enter the no. of rows: "))
            COLS = int(input("Enter the no. of columns: "))
        except ValueError:
            print("---- Enter a valid input-----")
            continue
        else:
            break

    DELAY = 1

    currentState = []
    nextState = []
        

    grid = GameofLife()
    grid.initGrid(rows = ROWS, cols = COLS, array = currentState)
    grid.initGrid(rows = ROWS, cols = COLS, array = nextState)
    gens=0

    fig, (ax1) = plt.subplots()
        
    while(nextState != currentState): 

        """
        The game will continue until the states are not repeating or all the cells in the grid are not dead.
        """

        grid.drawGrid(COLS, ROWS, currentState, gens)
        grid.updateGrid(COLS, ROWS, currentState, nextState)
        time.sleep(DELAY)
            
        colormap = plt.cm.Spectral
        normalize = plt.Normalize(vmin=0, vmax=1)
        plt.pcolor(currentState, edgecolors='k', linewidths=1, norm = normalize, cmap=colormap)
        plt.tick_params(axis='both', which='both', bottom=False,   
                        left=False, labelbottom=False, labelleft=False) 

        currentState, nextState = nextState, currentState
        gens=gens+1

        title = "GENERATION: "+str (gens)
        ax1.set_title(title)
        fig.tight_layout()
        plt.pause(0.05)

    print("Game Over! We Survived: " + str(gens) +" GENERATIONS")
    label= "Game Over! We Colony Survived: " + str(gens) +" GENERATIONS"
    plt.xlabel(label)
    plt.show()

