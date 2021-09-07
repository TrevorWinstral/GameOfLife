import pygame
from cell import Cell, Board
import random
pygame.init()

clock = pygame.time.Clock()
size = width, height = 1400, 1400


screen = pygame.display.set_mode(size)
pygame.display.set_caption('THE GAME OF LIFE')

screen.fill((255, 255, 255))

def random_board(x, y):
    initial_board = [[bool(random.choice([0,1])) for j in range(boardx+2)] for i in range(boardy+2)]
    initial_board = [[bool(random.choice([0,1,])) for j in range(boardx+2)] for i in range(boardy+2)]
    for i in range(boardy+2):
        initial_board[i][0] = False
        initial_board[i][-1] = False
    for j in range(boardy+2):
        initial_board[0][j] = False
        initial_board[-1][j] = False
    return initial_board

boardx, boardy = 9*20, 9*20
rectSizex, rectSizey = (width / (boardx+1)), (height/ (boardy+1))

b = Board(boardx, boardy, screen)
init_board = random_board(boardx, boardy)
print(len(init_board), len(init_board[0]))
b.setBoard(init_board)
# Initiate empty board

tracing=False
pause = False
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            px, py = event.pos
            rectx, recty = int(px // rectSizex)+1, int(py // rectSizey)+1
            print(px,py, rectx, recty)
            try:
                if (rectx != 0) and (recty !=0):
                    b.board[recty][rectx].setState(True)
            except Exception as e:
                print(e)
                pass
            tracing=True

            if event.button == 3:
                tracing = False

        if event.type == pygame.MOUSEMOTION and tracing == True:
            px, py = event.pos
            rectx, recty = int(px // rectSizex), int(py // rectSizey)
            try:
                if (rectx != 0) and (recty !=0):
                    b.board[recty][rectx].setState(True)
            except:
                pass

        if event.type == pygame.MOUSEBUTTONUP and tracing == True:
            tracing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_RIGHT or event.key == pygame.K_f:
                b.findNextStates()
                b.updateStates()
                
    if not tracing and not pause:
        b.findNextStates()
        b.updateStates()

    pygame.display.update()
    clock.tick()
    #clock.tick(1000)

