# Conways Game Of Life

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated". Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.

## Approach

The game starts with a randomly assigned grid of alive and dead cells based on the number of rows and columns given by the user. 
We can call this as our current state then check for the neighbours of the cell and then apply the above rules.
Now we have obtained a new state of the grid, we check if it is same as the current state, if not we go ahead with the next generation. 
The game continues until the states are not repeating or all the cells in the grid are not dead. 

I initially displayed the grid using a simple function to see the action using special characters to spice it up but there was something missing. 
So for a better visualization, I have experimented with the matplotlib library with my favourite colors as opposed to black and white to give a more game vibe!

## Requirements

* Python 3
* Matplotlib 
```pip install matplotlib ```

## Run the Game ##

``` python gameoflife.py ```

### Corner Case

An interesting case occurs when the current state and the next state continue to toggle between each other and this creates an infinite loop.

![Infinite State1](https://github.com/palakraman17/GameOfLife/blob/main/infinite_state_1.png )
![Infinite State2](https://github.com/palakraman17/GameOfLife/blob/main/infinite_state_2.png )

