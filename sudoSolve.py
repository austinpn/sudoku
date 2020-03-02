from sudoFun import boardSolve , printBoard
from graphics import sudoGame , quitGame
import pygame
from time import sleep
from fetchBoard import fetchBoard


board = fetchBoard()

width = 810
height = 810
pygame.font.init()
gameFont = pygame.font.SysFont("Comic Sans MS" , 50)
screen = pygame.display.set_mode((width , height))

board = fetchBoard()
# board = [[5, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 5, 0, 0, 8, 0], [4, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 1, 8, 0, 0, 0, 0], [0, 9, 0, 0, 2, 4, 5, 0, 0], [0, 3, 0, 0, 0, 5, 0, 0, 2], [0, 0, 2, 0, 1, 0, 8, 0, 6], [0, 8, 0, 0, 6, 2, 0, 3, 0]]

# print(board)

# board = [   [0, 7, 2, 0, 8, 0, 0, 0, 0],
#             [0, 3, 0, 0, 0, 0, 0, 0, 8],
#             [6, 0, 9, 0, 4, 0, 1, 0, 0],
#             [2, 1, 3, 4, 0, 6, 0, 8, 9],
#             [0, 0, 6, 0, 9, 8, 2, 1, 0],
#             [7, 0, 0, 0, 2, 3, 0, 6, 0],
#             [3, 0, 4, 0, 1, 0, 0, 9, 0],
#             [0, 0, 7, 0, 0, 0, 0, 4, 0],
#             [0, 0, 1, 0, 0, 0, 3, 0, 0]]

# board=[[0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 4, 0, 0, 0, 0, 0, 0], [0, 6, 0, 0, 0, 7, 0, 0, 0], [7, 9, 8, 1, 0, 0, 3, 5, 6], [0, 0, 0, 0, 0, 2, 9, 0, 0], [6, 4, 2, 9, 0, 0, 0, 0, 0], [0, 8, 7, 0, 0, 0, 4, 6, 2]]

# board = [[9,0,0,7,0,0,1,0,0],[0,2,3,0,8,0,0,0,0],[0,0,0,1,0,0,0,8,0],[0,0,4,3,0,6,0,0,8],[3,0,0,4,0,8,0,1,6],[0,8,0,2,0,7,3,4,5],[0,3,1,8,6,0,0,7,0],[7,0,0,0,0,0,0,6,0],[0,4,6,0,0,0,0,0,0]]
# board= [   [3,8,0,0,7,0,9,0,1],
#             [1,0,0,3,6,9,0,7,0],
#             [0,0,9,1,4,0,0,0,5],
#             [0,0,0,0,0,0,7,8,0],
#             [0,0,0,0,0,1,0,2,0],
#             [8,9,6,0,2,3,0,0,0],
#             [0,3,1,0,8,0,6,0,7],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,6,3,7,5,1,0]]

with open("boardCatalogue.txt" , "a") as bc:
    bc.write(str(board)+"\n")


copyBoard = board.copy()
gameBoard = boardSolve(copyBoard)
gameBoard.findZero()
# print(gameBoard.trackZer)

graphBoard = sudoGame(810 , 810 , 50 , gameBoard.board , screen)
# print(graphBoard.zeroPlace)


runWindow = True

graphBoard.drawBoard()
# sleep(.05)
a = True
count = 0
while(runWindow):
    if not gameBoard.solved:
        # for i in range(100):
            # if not gameBoard.solved:
            #     count+=1
            #     gameBoard.moreFastIncrement()
                # gameBoard.runIncrement()
                # gameBoard.runSetIncrement()
        # count+=1
        for i in range(500):
            if not gameBoard.solved:
                gameBoard.moreFastIncrement()
                count+=1
        # sleep(.1)
        # input()
        # gameBoard.runIncrement()
        # gameBoard.runSetIncrement()
        if count<5000:
            sleep(.05)
        graphBoard.drawBoard()
    else:
        # graphBoard.drawBoard()
        if a:
            a=False
            print("{:,d}".format(count))
    # if a:
    #     a=False
    #     for i in range(150):
    #         # print(gameBoard.mapper)
    #         # graphBoard.drawBoard()
    #         # gameBoard.moreFastIncrement()
    #         # print(gameBoard.store)
    #         # print(gameBoard.changes)
    #         # print(gameBoard.checkTable())
    #         # print()
            
    runWindow= quitGame()
    


        
    