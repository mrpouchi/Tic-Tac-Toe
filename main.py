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



def manage_grid(grid,somme,small):
    global main

    if small and (somme == 3 or somme == -3):
            for line in grid :
                for square in line :
                    square.darken = True
                    square.x = 0 if square.x == None else square.x

    if somme == 3:
        if small :
            draw_x(grid[1][1].rect.center,grid[1][1].color,sw//5)
            BIG_GRID[0][Squares.big_grid.index(grid) // 3][Squares.big_grid.index(grid) % 3] = 1
        else :
            main = False
            Retry("X")

    elif somme == -3:
        if small :
            draw_o(grid[1][1].rect.center,grid[1][1].color,sw//5)
            BIG_GRID[0][Squares.big_grid.index(grid) // 3][Squares.big_grid.index(grid) % 3] = -1
        else :
            main = False
            Retry("O")

    elif small and all(el.x  != None  for line in grid for el in line) and BIG_GRID[0][Squares.big_grid.index(grid) // 3][Squares.big_grid.index(grid) % 3] == None:
        for line in grid :
            for square in line :
                square.darken = True
                square.x = 0 if square.x == None else square.x
                BIG_GRID[0][Squares.big_grid.index(grid) // 3][Squares.big_grid.index(grid) % 3] = 0

    elif  all(el != None for line in grid for el in line) and not small: #que dans le grand quadrillage
        SOMME = 0
        for line in grid :
            for el in line :
                SOMME += el
        if SOMME > 0 :
            main = False
            Retry("X")
        elif SOMME < 0 :
            main = False
            Retry("O")
        else :
            main = False
            Retry("Draw !")


def check_grid(GRID,small):
    for grid in GRID :
        somme1 = 0
        somme2 = 0
        for i in range(0,3):
            somme = 0
            for el in grid[i]:
                somme += (el.x if el.x != None else 0)if small else (el if el != None else 0)
                manage_grid(grid,somme,small)

            somme = 0
            for el in grid:
                somme += (el[i].x if el[i].x != None else 0)if small else (el[i] if el[i] != None else 0)
                manage_grid(grid,somme,small)

            somme1 += (grid[i][i].x if grid[i][i].x != None else 0)if small else (grid[i][i] if grid[i][i] != None else 0)
            somme2 += (grid[len(grid)-1-i][i].x if grid[len(grid)-1-i][i].x != None else 0)if small else (grid[len(grid)-1-i][i] if grid[len(grid)-1-i][i] != None else 0)
        manage_grid(grid,somme1,small)
        manage_grid(grid,somme2,small)

def create_grid(sw, sh, colors):
    global BIG_GRID
    BIG_GRID = [[[None, None, None] for _ in range(3)]]
    Squares.big_grid = [[[], [], []] for _ in range(9)]

    for grid_num in range(9):
        line = grid_num // 3
        col = grid_num % 3
        grid_x = col * sw // 3
        grid_y = line * sh // 3

        for line_num in range(3):
            for col_num in range(3):
                square_x = grid_x + col_num * sw // 9
                square_y = grid_y + line_num * sh // 9
                rect = pygame.Rect(square_x, square_y, sw // 9, sh // 9)
                Squares(rect, colors[grid_num], grid_num, line_num)




def Main(classical):
    global main,screen
    main = True
    turn = True
    sw , sh = pygame.display.get_surface().get_size()
    colors = [(randint(100, 255), randint(100, 255), randint(100, 255))for _ in range(9)]
    create_grid(sw,sh,colors)

    while main:
        screen.fill((31,31,31))

        sw, sh = pygame.display.get_surface().get_size()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False

            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                create_grid(event.w, event.h, colors)

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

                                    if not classical :
                                        for grid2 in Squares.big_grid:
                                            if Squares.big_grid.index(grid2) != grid.index(line)*3+line.index(square) :
                                                for line2 in grid2 :
                                                    for square2 in line2 :
                                                        square2.darken = True
                                            else :
                                                for line2 in grid2 :
                                                    for square2 in line2 :
                                                        square2.darken = False



        for grid in Squares.big_grid:
            for line in grid :
                for square in line :
                    pygame.draw.rect(screen,square.dark_color if square.darken else square.color,square.rect,5)
                    square.xo_draw()

                    
        check_grid(Squares.big_grid,True)                               
        check_grid(BIG_GRID,False)

        pygame.display.update()


def Retry(winner):
    main = False
    retry = True
    while retry:
        screen.fill((31, 31, 31))

        if winner == "Draw !" :
            Text(winner, pygame.font.Font("Postino.otf", 80), (78, 201, 164), sw * 0.2,sh*0.3, screen).draw()

        else :
            Text(f"The {winner}'s won !", pygame.font.Font("Postino.otf", 80), (78, 201, 164), sw * 0.2,sh*0.3, screen).draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                retry = False

        if Text("Recommencer", pygame.font.Font("Postino.otf", 65), (78, 201, 164), sw * 0.2,sh / 2, screen,(108, 251, 194)).draw():
            if pygame.mouse.get_pressed()[0]: 
                start()
                retry = False

        pygame.display.update()

clock = pygame.time.Clock()
def start():
    start = True
    gamemode = False
    while start:
        screen.fill((31, 31, 31))

        screen_width, screen_height = pygame.display.get_surface().get_size()

        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        if Text("Start", pygame.font.Font("Postino.otf", 65), randcol(), screen_width * 0.38,screen_height*0.72, screen, (108, 251, 194)).draw((31,31,31),(108, 251, 194)):
            if pygame.mouse.get_pressed()[0]: 
                gamemode = not gamemode
        
        if gamemode :
            if Text("Advanced", pygame.font.Font("Postino.otf", 50), randcol(), screen_width * 0.6,screen_height*0.85, screen, (108, 251, 194)).draw((31,31,31),(108, 251, 194)):
                if pygame.mouse.get_pressed()[0]:
                    Main(False)
                    start = False

            if Text("Classical", pygame.font.Font("Postino.otf", 50), randcol(), screen_width * 0.1,screen_height*0.85, screen, (108, 251, 194)).draw((31,31,31),(108, 251, 194)):
                if pygame.mouse.get_pressed()[0]:
                    Main(True)
                    start = False

        Text("Multi", pygame.font.Font("Postino.otf", 150),randcol(), screen_width * 0.25,screen_height*0.1, screen).draw()
        Text("Tic", pygame.font.Font("Postino.otf", 150),randcol(), screen_width * 0.35,screen_height*0.25, screen).draw()
        Text("Tac", pygame.font.Font("Postino.otf", 150),randcol(), screen_width * 0.35,screen_height*0.37, screen).draw()
        Text("Toe", pygame.font.Font("Postino.otf", 150),randcol(), screen_width * 0.35,screen_height*0.49, screen).draw()


        pygame.display.update()

start()
pygame.quit()




