import pygame
from random import randint

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

D = 50
bordeau = (135,48,74)
cyan = (48, 120, 127)
orange = (208, 92, 52)

def draw_x(posx,posy):
    posx = posx-D/2
    posy = posy-D/2
    pygame.draw.line(screen,cyan,((posx,posy)),(posx+D,posy+D),8)
    pygame.draw.line(screen,cyan,(posx,posy+D),(posx+D,posy),8)


def draw_o(posx,posy):
    pygame.draw.circle(screen,orange,((posx,posy)),D*0.5,5)

def draw_tab1():
    return [[pygame.Rect(w,h,111,111),True,None]for H in range(0,1000,333)for W in range(0,1000,333)for h in range(H,H+333,111)for w in range(W,W+333,111)]



        





run = True
turn = True
X = []
O = []
rects = draw_tab1()
counter = 0
color = bordeau

for rect in rects :
    if counter != 9 :
        counter += 1
    else :
        counter = 0
        rect[2] = (randint(0,255),randint(0,255),randint(0,255))

while run:
    screen.fill((31,31,31))

    for x in X :
        draw_x(x[0],x[1])
    for o in O :
        draw_o(o[0],o[1])
    
    
    for rect in rects:
        pygame.draw.rect(screen,rect[2],rect[0],5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                for rect in rects :
                    if rect[0].collidepoint(event.pos) and rect[1]:
                        if turn :
                            X.append(rect[0].center)
                            turn = not turn
                            rect[1] = False
                            print(X)
                            
                        else : 
                            O.append(rect[0].center)
                            turn = True
                            rect[1] = not turn
                            print(O)

    pygame.display.update()

pygame.quit()



