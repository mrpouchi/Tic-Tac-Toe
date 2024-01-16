import pygame
from text import Text
from random import randint
from win32api import GetSystemMetrics

pygame.init()


sw = int(GetSystemMetrics(0)/2)
sh = int(GetSystemMetrics(1)/1.2)

screen = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)

pygame.display.set_caption("Tic-Tac-Toe")

def randcol():
    return (randint(150, 255), randint(150, 255), randint(150, 255))

class Squares():
    big_grid = []
    def __init__(self,rect,color,grid_num,line_num):
        self.rect = rect
        self.color = color
        self.dark_color = (self.color[0]-100,self.color[1]-100,self.color[2]-100)
        self.darken = None
        self.x = None
        Squares.big_grid[grid_num][line_num].append(self)

    def xo_draw(self) :
        if self.x == 1 :
            draw_x(self.rect.center,self.dark_color if self.darken else self.color,50)
        if self.x == -1 :
            draw_o(self.rect.center,self.dark_color if self.darken else self.color,50)
        

def draw_x(pos,color,D):
    posx = pos[0]-D/2
    posy = pos[1]-D/2
    pygame.draw.line(screen,color,(posx,posy),(posx+D,posy+D),int(D/8))
    pygame.draw.line(screen,color,(posx,posy+D),(posx+D,posy),int(D/8))


def draw_o(pos,color,D):
    pygame.draw.circle(screen,color,pos,D*0.5,int(D/10))





def create_grid(sw, sh):
    global BIG_GRID
    BIG_GRID = [[[None, None, None] for _ in range(3)]]
    Squares.big_grid = [[[], [], []] for _ in range(9)]

    for grid_num in range(9):
        line = grid_num // 3
        col = grid_num % 3
        grid_x = col * sw // 3
        grid_y = line * sh // 3
        color = (randint(100, 255), randint(100, 255), randint(100, 255))

        for line_num in range(3):
            for col_num in range(3):
                square_x = grid_x + col_num * sw // 9
                square_y = grid_y + line_num * sh // 9
                rect = pygame.Rect(square_x, square_y, sw // 9, sh // 9)
                Squares(rect, color, grid_num, line_num)




def Main():
    global main,screen
    main = True
    turn = True
    sw , sh = pygame.display.get_surface().get_size()
    create_grid(sw,sh)

    while main:
        screen.fill((31,31,31))

        sw, sh = pygame.display.get_surface().get_size()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False

            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                create_grid(event.w, event.h)

            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1:
                    for grid in Squares.big_grid:
                        for line in grid :
                            for square in line :
                                if square.rect.collidepoint(event.pos) and square.x == None and square.darken != True :

                                    if turn :
                                        turn = not turn
                                        square.x = 1
                                        
                                    else : 
                                        turn = not turn
                                        square.x = -1





        for grid in Squares.big_grid:
            for line in grid :
                for square in line :
                    pygame.draw.rect(screen,square.dark_color if square.darken else square.color,square.rect,5)
                    square.xo_draw()

                    


        pygame.display.update()


Main()
pygame.quit()




