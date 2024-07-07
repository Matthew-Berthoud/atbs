# conway's game of life

import random, time, copy
WIDTH = 60
HEIGHT = 20

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        # if random.randint(0, 1) == 0:
        if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column)

while True:
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells)

    # print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # print the # or the space
        print()

    # calculate next step's cells based on current step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # count living neighbors
            numNeighbors = 0

            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

    time.sleep(1)
