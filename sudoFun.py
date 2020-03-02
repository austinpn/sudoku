class ReachEnd(Exception):
    pass

def firstGreat(value , sortls):
    for i in sortls:
        if i>value:
            return i
    return(-1)

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

def printBoard(board):
    for y in range(9):
        for x in range(9):
            print(str(board[y][x]).ljust(3) , end='')
        print()
    print()

class boardSolve():
    def __init__(self, board):
        self.board = board
        self.keepGoing = True
        self.solved=False
    
    def getCol(self ,  x):
        col=[]
        for i in range(9):
            col.append(self.board[i][x])

        return(col)
    
    def getRow(self , y):
        row=self.board[y]
        return(row)
    
    def getBox(self , y , x):
    
        boxCorner_y = (y//3)*3
        boxCorner_x = (x//3)*3
        box=[]
        for yplace in range(boxCorner_y , boxCorner_y+3):
            for xplace in range(boxCorner_x , boxCorner_x + 3):
                box.append(self.board[yplace][xplace])
        return(box)
    
    def cellSet(self , y , x):
        currentSet =  set(self.getRow(y)).union(set(self.getCol(x))).union(set(self.getBox(y,x)))
        reverseSet = set()
        for i in range(10):
            if i not in currentSet:
               reverseSet.add(i)
        reverseSet.add(0)
        return reverseSet 
    
    def findZero(self):
        self.mapper = 0
        self.trackZer = []
        self.trackSet = []
        for y in range(9):
            for x in range(9):
                if(self.board[y][x]==0):
                    self.trackSet.append(sorted(list(self.cellSet(y , x))))
                    self.trackZer.append(tuple((y,x)))
        self.changes = [0]*len(self.trackZer)
        self.store = self.changes.copy()
        # print(self.changes)
    
    def checkGood(self , inarr):
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
    
    def checkTable(self):
        for i in range(9):
            if(not checkGood(self.getRow(i))):
                # print(checkGood(getRow(board , i)))
                return False
            elif(not checkGood(self.getCol(i))):
                # print(checkGood(self.getCol(i)))
                # print(i)
                # print(self.getCol(i))
                return False
        for i in range(3):
            for j in range(3):
                if(not checkGood(self.getBox(i*3 , j*3))):
                    # print(checkGood(getRow(board , i)))
                    return False
        # print('hi')
        return True

    
    def matchChange(self):
        for i in range(len(self.trackZer)):
            self.board[self.trackZer[i][0]][self.trackZer[i][1]] = self.changes[i]

    
    def runIncrement(self):
        # print(self.checkTable())
        # print(self.changes)
        # print(self.mapper)
        # print()
        # print(self.mapper)
        
        if self.checkTable():
            if(self.mapper==len(self.changes)):
                self.solved=True
            elif self.changes[self.mapper]!=9:
                self.changes[self.mapper]+=1
                if(self.mapper<(len(self.changes))):
                    self.mapper+=1
            else:
                self.changes[self.mapper] = 0
                self.mapper-=1
        else:
            self.mapper-=1 #reset map positioning
        
            if self.changes[self.mapper]!=9:
                self.changes[self.mapper]+=1
                self.mapper+=1
            else:
                self.changes[self.mapper]=0
                self.mapper-=1
            
        self.matchChange()

            # else:
            #     if(self.changes[len(self.changes)-1]!=9):
            #         self.changes[len(self.changes)-1]+=1
            # else:
            #     pass

        # printBoard(self.board)    
        # print(self.trackZer)
    
    def matchSet(self):
        for i in range(len(self.trackZer)):
            self.board[self.trackZer[i][0]][self.trackZer[i][1]] = self.trackSet[i][self.changes[i]]
    
    def runSetIncrement(self):
        # print(self.trackSet[self.mapper][self.changes[self.mapper]])
        # print(self.changes)
        # print(self.mapper)
        # print(self.checkTable())
        if self.checkTable():
            if(self.mapper==len(self.changes)):
                self.solved=True
            elif self.changes[self.mapper]!=len(self.trackSet[self.mapper])-1:
                # print(len(self.trackSet[self.mapper]))
                self.changes[self.mapper]+=1
                if(self.mapper<(len(self.changes))):
                    self.mapper+=1
            else:
                self.changes[self.mapper] = 0
                self.mapper-=1
        else:
            self.mapper-=1 #reset map positioning
        
            if self.changes[self.mapper]!=len(self.trackSet[self.mapper])-1:
                self.changes[self.mapper]+=1
                self.mapper+=1
            else:
                self.changes[self.mapper]=0
                self.mapper-=1
        self.matchSet()

    def moreFastIncrement(self):
        if self.mapper<len(self.changes):#is in range of indexing, and is not solved
            tempSet = sorted(list(self.cellSet(self.trackZer[self.mapper][0] , self.trackZer[self.mapper][1])))
            tempCheck = firstGreat(self.changes[self.mapper] , tempSet[1:])
            if tempCheck!=-1:
                self.changes[self.mapper] = tempCheck
                self.mapper+=1
            else:
                self.changes[self.mapper] = 0
                self.mapper-=1
        else:
            self.solved = True

            
        
        self.matchChange()
            

    
