import pygame

color_dict = {False:(255,255,255), True:(0,0,0)}

class Cell:
    def __init__(self, alive: bool, rect, screen, name=''):
        self.alive = alive
        self.nextState = False
        self.neighbors = []
        self.name= name
        self.rect = rect
        self.screen = screen

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def findNextState(self):
        count = 0
        for cell in self.neighbors:
            if cell.isAlive():
                count +=1

        if count == 3:
            self.nextState = True 
        if count == 2 and self.alive:
            self.nextState = True 

    def isAlive(self):
        return self.alive 

    def setState(self, newState: bool):
        changed = (self.alive != newState)
        self.alive = newState

        if changed:
            pygame.draw.rect(self.screen, color_dict[self.alive], self.rect)

    def update(self):
        changed = (self.alive != self.nextState)
        self.alive = self.nextState
        self.nextState = False

        if changed:
            pygame.draw.rect(self.screen, color_dict[self.alive], self.rect)

    def __str__(self):
        return f'{self.name} (Now: {int(self.alive)}, Next: {int(self.nextState)})'


def create_rect(x, y, size, xscale, yscale):
    width, height = size
    ret = pygame.Rect((int(x*width), int(y*height)), (int(xscale*width), int(yscale*height)))
    return ret

class Board:
    def __init__(self, width: int, height: int, screen):
        self.board = [ [Cell(False, create_rect(col/(width+2), row/(height+2), screen.get_size(), 1/(width+2), 1/(height+2)),
         screen, name=str(col)+str(row)) for col in range(width+2) ] for row in range(height+2) ] # gives us a board of dead cells, we need to buffer by 2 for the dead cells around the edge
        self.width = width+2
        self.height = height+2
        self.addNeighbors()

    def setBoard(self, board: list):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                self.board[row][col].setState(board[row][col])

        self.height = len(board)
        self.width = len(board[0])

    def addNeighbors(self):
        for i in range(1,self.height-1):
            for j in range(1, self.width-1):
                c = self.board[i][j]
                # now we need to go in an outline around i,j and add those cells as neighbors to our current cell
                for index in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                    a,b = index
                    c.addNeighbor(self.board[i+a][j+b])
    
    def findNextStates(self):
        for i in range(1,self.height-1):
            for j in range(1, self.width-1):
                c = self.board[i][j]
                c.findNextState()

    def updateStates(self):
        for i in range(1,self.height-1):
            for j in range(1, self.width-1):
                c = self.board[i][j]
                c.update()


    def __repr__(self):
        b = '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])
        return f'Width: {self.width}, Height: {self.height}\n{b}'

'''
b = Board(1,1)
print(b)

b.setBoard([[False, True, False], [True, False, False], [False, False, True]])
print(b)

b.findNextStates()
print(b)

b.updateStates()
print(b)
print(repr(b.board[0][0]))


c=Cell(False)
'''