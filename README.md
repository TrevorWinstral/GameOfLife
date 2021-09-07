# Simple Pygame implementation of Conway's Game of Life
Resolution and amount of cells can be set in gol.py. There is a buffer of permanently dead cells around the border.
Once ran space pauses the simulation, at which point the you can press 'f' to step forward 1 generation, space once again resumes the simulation. By left clicking and tracing a path, cells will be brought to life along that path until left-click is released. On the other hand right resurrects the cell under the pointer.

Only gol.py needs to be ran, cell.py simply hosts the code to manage the board and cells.
