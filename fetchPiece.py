from graphics import sudoGame
board = [   [0, 7, 2, 0, 8, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 0, 0, 0, 8],
            [6, 0, 9, 0, 4, 0, 1, 0, 0],
            [2, 1, 3, 4, 0, 6, 0, 8, 9],
            [0, 0, 6, 0, 9, 8, 2, 1, 0],
            [7, 0, 0, 0, 2, 3, 0, 6, 0],
            [3, 0, 4, 0, 1, 0, 0, 9, 0],
            [0, 0, 7, 0, 0, 0, 0, 4, 0],
            [0, 0, 1, 0, 0, 0, 3, 0, 0]]

boxKey = []
for y in range(3):
    for x in range(3):
        boxKey.append(tuple([y,x]))


def printBoard(board):
    for y in range(9):
        for x in range(9):
            print(str(board[y][x]).ljust(3) , end='')
        print()
    print()


def getCol(board ,  x):
    col=[]
    for i in range(9):
        col.append(board[i][x])

    return(col)

def getRow(board , y):
    row=board[y]
    return(row)

def getBox(board , y , x):
    
    boxCorner_y = (y//3)*3
    boxCorner_x = (x//3)*3
    box=[]
    for yplace in range(boxCorner_y , boxCorner_y+3):
        for xplace in range(boxCorner_x , boxCorner_x + 3):
            box.append(board[yplace][xplace])
    return(box)

def replaceEmpty(passSet):
    for i in range(1,10):
        if not(i in passSet):
            return(i)

def checkGood(inarr):
    arr = inarr.copy()
    delArr=0
    for i in range(len(arr)):
        if arr[i]==0:
            delArr+=1
    for i in range(delArr):
        arr.remove(0)
    if(len(arr)==len(set(arr))):
        # print(len(arr))
        # print(len(set(arr)))
        # print(len(arr)==len(set(arr)))
        return True
    else:
        return False

def checkTable(board):
    for i in range(9):
        if(not checkGood(getRow(board , i))):
            # print(checkGood(getRow(board , i)))
            return False
        elif(not checkGood(getCol(board , i))):
            return False
    for i in range(3):
        for j in range(3):
            if(not checkGood(getBox(board , i*3 , j*3))):
                # print(checkGood(getRow(board , i)))
                return False
    # print('hi')
    return True

def findZero(board):
    trackZer = []
    for y in range(9):
        for x in range(9):
            if(board[y][x]==0):
                trackZer.append(tuple((y,x)))
    return trackZer


def  addOne(board , locations, mapIt):
    board[locations[mapIt][0]][locations[mapIt][0]]+=1
    return
def minusOne(board , locations, mapIt):
    board[locations[mapIt][0]][locations[mapIt][0]]-=1
    return

def fixIt(board , locations, mapIt):
    if(board[locations[mapIt][0]][locations[mapIt][0]])!=9:
        addOne(board , locations , mapIt)
        return(mapIt)
    else:

def increment(board , locations , game , map=0):
    print('hi')

    if(map+1==len(locations) and board[locations[map][1]][locations[map][1]]!=1 and checkTable(board)):
        print("here")
        return
    if(checkTable(board)):
        if(board[locations[map][1]][locations[map][0]]==9):
            map+=1
            game.drawBoard()
        board[locations[map][1]][locations[map][0]]+=1
        
            
    
    



