from random import choice
import pygame
pygame.init()
class TicTacToe:
    def __init__(self):
        self.Board=[]
    
    def make_board(self):
        for i in range(3):
            li=[]
            for j in range(3):
                li.append('-')
            self.Board.append(li)
        print(self.Board)
            

    def load_img(self):
        whiteimage=pygame.image.load('white_img.jpeg')
        self.whiteimage=pygame.transform.scale(whiteimage,(95,95))
        self.ximg=pygame.transform.scale(pygame.image.load('x_img.png'),(95,95))
        self.Oimg=pygame.transform.scale(pygame.image.load('Zero_img.jpeg'),(95,95))
        font=pygame.font.Font(size=30)
        self.xwin=font.render("X Wins",True,'White','Black')
        self.xrect=self.xwin.get_rect()
    
    def check_filled(self,row,col):
        filled=False
        if self.Board[row][col]!='-':
            filled=True
        return filled   
    
    def update_rectangles(self):
        for i in range(3):
            for j in range(3):
                
                if(self.Board[i][j] =='x'):
                    self.main.blit(self.ximg,pygame.Rect(100+100*j,50+100*i,100,100))
                elif(self.Board[i][j]=='o'):
                    self.main.blit(self.Oimg,pygame.Rect(100+100*j,50+100*i,100,100))
                else:
                    self.main.blit(self.whiteimage,pygame.Rect(100+100*j,50+100*i,100,100))
    
    def check_winning(self,player):
        n=len(self.Board)
    
        for i in range(n):
            win=True
            for j in range(n):
                if self.Board[i][j]!=player:
                    win=False
                    break
            if win:
               return win
        
        for i in range(n):
            win=True
            for j in range(n):
                if self.Board[j][i]!=player:
                    win=False
                    break
            if win:
                return win
                
        win=True        
        for i in range(n):
            if self.Board[i][i]!=player:
                win=False
                break
        if win:
          return win
            
        win = True
        for i in range(n):
            if self.Board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def isvalid(self,row,col):
        if row>=0 and row<=2 and col>=0 and col<=2:
            return True
        else:
            return False

    def computer_turn(self):
        best_score=1000
        moves=[]
        for i in range(3):
            for j in range(3):
                if self.Board[i][j] == '-':
                    self.Board[i][j]='o'
                    score=self.minimax(True)
                    if score < best_score:
                        best_score=score
                        moves.clear()
                    if score==best_score:
                        moves.append([i,j])
                    self.Board[i][j] = '-'
                    print(moves,i,j,best_score,score)
        
        next_move=choice(moves)
        print(next_move)
        return next_move[0],next_move[1]
        
    def make_move(self,row,col):
        if not self.isvalid(row,col):
            return False
        elif self.check_filled(row,col):
            return False
        self.Board[row][col]= self.player
        
        if self.check_winning('x'):
            return False
        if self.is_board_filled():
            return False
        return True
        
    def computer_move(self):
        row,col=self.computer_turn()
        print(row,col)
        self.Board[row][col]= 'o'
        print(self.Board)
    
    def start(self):   
        self.main=pygame.display.set_mode((500,500))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption("Tic Tac Toe")
        self.main.fill("Black")
        self.load_img()
        # pygame.draw.rect(main,(255,0,0),pygame.Rect(10,50,100,100))
        self.make_board()
        self.player='x'
        while True:
            self.clock.tick(60)
            self.update_rectangles()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x=(pos[0]-100)//100
                    y=(pos[1]-50)//100
                    print(y,x)
                    if self.make_move(y,x):
                        pygame.display.update()
                        self.computer_move()
            if self.check_winning('o'):
                self.main.blit(self.xwin,self.xrect)
            elif self.check_winning('o'):
                pass
            
            if self.is_board_filled():
                pass
            pygame.display.update()
    
    def is_board_filled(self):
        for row in self.Board:
            for item in row:
                if item=='-':
                    return False
        return True 
    
    def minimax(self,ismax):
        if self.check_winning('x'):
            return 300
        if self.check_winning('o'):
            return -300
        if self.is_board_filled():
            return 0
        
        if not ismax:
            best_score=1000        
            for i in range(3):
                for j in range(3):
                    if self.Board[i][j] == '-':
                        self.Board[i][j]='o'
                        score=self.minimax(True)
                        if score < best_score:
                            best_score=score
                        self.Board[i][j]= '-'
        
        else:
            best_score=-1000
            for i in range(3):
                for j in range(3):
                    if self.Board[i][j] == '-':
                        self.Board[i][j]='x'
                        score=self.minimax(False)
                        if score > best_score:
                            best_score=score
                        self.Board[i][j]= '-'
        
        return best_score
    
    
if __name__=="__main__":
    ttt=TicTacToe()
    ttt.start()