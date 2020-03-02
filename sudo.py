import fetchPiece
from graphics import sudoGame , quitGame
import pygame
import pygame.locals
from time import sleep

pygame.font.init()

gameFont = pygame.font.SysFont("COmic Sans MS" , 50)

width = 810
height = 810
sec_w = width//9
sec_h = height//9
fontSize = 30
font_dist_x = width/3
font_dist_y = height/3

screen = pygame.display.set_mode((width , height))



board = [   [0, 7, 2, 0, 8, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 0, 0, 0, 8],
            [6, 0, 9, 0, 4, 0, 1, 0, 0],
            [2, 1, 3, 4, 0, 6, 0, 8, 9],
            [0, 0, 6, 0, 9, 8, 2, 1, 0],
            [7, 0, 0, 0, 2, 3, 0, 6, 0],
            [3, 0, 4, 0, 1, 0, 0, 9, 0],
            [0, 0, 7, 0, 0, 0, 0, 4, 0],
            [0, 0, 1, 0, 0, 0, 3, 0, 0]]

setBoard=[[],[],[],[],[],[],[],[],[]]
copyBoard = board.copy()

gameBoard = sudoGame(810 , 810 , 50 , copyBoard , screen)


keepRun = True
runWindow = True
# screen.fill((0,255,255))



# for x in range(9):
#     for y in range(9):
#         pygame.draw.rect(screen , (0,0,0) , (x*sec_w,y*sec_h,sec_w , sec_h) , 1)
#         numpic = gameFont.render(str(board[y][x]) , False , (0,0,0))
#         screen.blit(numpic , (x*sec_w+35, y*sec_h+35))

gameBoard.drawBoard()

# for x in range(3):
#     for y in range(3):
#         pygame.draw.rect(screen , (0,0,0) , (x*sec_w*3 , y*sec_h*3 ,sec_w*3 , sec_h*3) , 5)

trackChange = []

while(runWindow):
    runWindow= quitGame()

    # screen.fill((0,255,255))
    # for x in range(9):
    #     for y in range(9):
    #         pygame.draw.rect(screen , (0,0,0) , (x*sec_w,y*sec_h,sec_w , sec_h) , 1)
    # for x in range(3):
    #     for y in range(3):
    #         pygame.draw.rect(screen , (0,0,0) , (x*sec_w*3 , y*sec_h*3 ,sec_w*3 , sec_h*3) , 5)
    
    pygame.display.update()
    while(keepRun):
        keepRun = False
        for row in range(0,9):
            for(col) in range(0,9):
                currentSet = set(fetchPiece.getRow(board , row))
                currentSet = currentSet.union(fetchPiece.getCol(board , col))
                currentSet = currentSet.union(fetchPiece.getBox(board, row , col))
                setBoard[row].insert(col , len(currentSet))
                if(not(0 in currentSet)):
                    currentSet.add(0)
                # if (len(currentSet)==9 and copyBoard[row][col]==0):
                #     copyBoard[row][col] = fetchPiece.replaceEmpty(currentSet)
                if(len(currentSet)==9 and copyBoard[row][col]==0):
                    keepRun = True
                    # print(copyBoard[row][col])
                    copyBoard[row][col] = fetchPiece.replaceEmpty(currentSet)
                    # print(copyBoard[row][col])
                    # print(fetchPiece.replaceEmpty(currentSet))
                    
                
                # fetchPiece.printBoard(copyBoard)
                gameBoard.board = copyBoard
                gameBoard.drawBoard()
                # pygame.display.update()
        zeros = fetchPiece.findZero(copyBoard)
        print(zeros)
        runWindow = quitGame()
        fetchPiece.increment(copyBoard , zeros , gameBoard)
        if not runWindow:
            keepRun = False




    # print(fetchPiece.checkTable(copyBoard))
    
    

