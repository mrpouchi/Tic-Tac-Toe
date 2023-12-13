import pygame
from random import randint

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

class Squares():
    big_grid = [[[],[],[]]for i in range(9)]
    def __init__(self,rect,color,grid_num,line_num):
        self.rect = rect
        self.color = color
        self.dark_color = (self.color[0]-70,self.color[1]-70,self.color[2]-70)
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



def manage_grid(grid,somme):
    if somme == 3 or somme == -3 or all(el.x != None for line in grid for el in line):
        for line in grid :
            for square in line :
                square.darken = True
                square.x = 0 if square.x == None else square.x

    if somme == 3:
        draw_x(grid[1][1].rect.center,grid[1][1].color,200)

    if somme == -3:
        draw_o(grid[1][1].rect.center,grid[1][1].color,200)


def check_grid():
    for grid in Squares.big_grid :
        somme1 = 0
        somme2 = 0
        for i in range(0,3):
            somme = 0
            for el in grid[i]:
                somme += el.x if el.x != None else 0
                manage_grid(grid,somme)

            somme = 0
            for el in grid:
                somme += el[i].x if el[i].x != None else 0
                manage_grid(grid,somme)

            somme1 += grid[i][i].x if grid[i][i].x != None else 0
            somme2 += grid[len(grid)-1-i][i].x if grid[len(grid)-1-i][i].x != None else 0
        manage_grid(grid,somme1)
        manage_grid(grid,somme2)
   

def main():
    run = True
    turn = True
    grid_num = -1
    line_num = -1
    for H in range(0, 999, 333):
        for W in range(0, 999, 333):
            color = (randint(100, 255), randint(100, 255), randint(100, 255))
            grid_num += 1
            for h in range(H, H + 333, 111):
                line_num += 1
                if line_num == 2:
                    line_num = -1
                for w in range(W, W + 333, 111):
                    Squares(pygame.Rect(w, h, 111, 111), color, grid_num, line_num)
    while run:
        screen.fill((31,31,31))


        for grid in Squares.big_grid:
            for line in grid :
                for square in line :
                    pygame.draw.rect(screen,square.dark_color if square.darken else square.color,square.rect,5)
                    square.xo_draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1:
                    for grid in Squares.big_grid:
                        for line in grid :
                            for square in line :
                                if square.rect.collidepoint(event.pos) and square.x == None:
                                    if turn :
                                        turn = not turn
                                        square.x = 1
                                        
                                    else : 
                                        turn = not turn
                                        square.x = -1

        check_grid()
        pygame.display.update()

main()
pygame.quit()



