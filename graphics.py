import pygame



def quitGame():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return False
    return True
class sudoGame():
    def __init__(self , width , height , fontSize , board , screen):
        self.screen = screen
        self.board = board
        self.width = width
        self.height = height
        self.sec_w = self.width//9
        self.sec_h = self.height//9
        self.fontSize = fontSize
        self.font_dist_x = self.sec_h/3
        self.font_dist_y = self.sec_h/3
        self.gameFont = pygame.font.SysFont("COmic Sans MS" , fontSize)
        


    def drawBoard(self):
        self.screen.fill((0,255,255))
        for x in range(9):
            for y in range(9):
                pygame.draw.rect(self.screen , (0,0,0) , (x*self.sec_w,y*self.sec_h,self.sec_w , self.sec_h) , 1)
                if(self.board[y][x]!=0):
                    numpic = self.gameFont.render(str(self.board[y][x]) , False , (0,0,0))
                    self.screen.blit(numpic , (x*self.sec_w+35, y*self.sec_h+35))
        for x in range(3):
            for y in range(3):
                pygame.draw.rect(self.screen , (0,0,0) , (x*self.sec_w*3 , y*self.sec_h*3 ,self.sec_w*3 , self.sec_h*3) , 5)
        pygame.display.update()

    


