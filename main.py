import pygame

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

D = 200
bordeau = (135,48,74)

def draw_x(posx,posy):
    posx = posx-D/2
    posy = posy-D/2
    pygame.draw.line(screen,(255,0,0),((posx,posy)),(posx+D,posy+D),5)
    pygame.draw.line(screen,(255,0,0),(posx,posy+D),(posx+D,posy),5)


def draw_o(posx,posy):
    pygame.draw.circle(screen,(0,0,255),((posx,posy)),D*0.5,5)

def draw_tab1(rects):
    rects.append(pygame.Rect(0,0,333,333))
    rects.append(pygame.Rect(0,0,333,666))
    rects.append(pygame.Rect(0,0,333,999))
    rects.append(pygame.Rect(0,0,666,333))
    rects.append(pygame.Rect(0,0,666,666))
    rects.append(pygame.Rect(0,0,666,999))
    rects.append(pygame.Rect(0,0,999,333))
    rects.append(pygame.Rect(0,0,999,666))
    rects.append(pygame.Rect(0,0,999,999))



run = True
turn = False
X = []
O = []
rects = []
while run:
    screen.fill((31,31,31))

    draw_tab1(rects)

    for x in X :
        draw_x(x[0],x[1])
    for o in O :
        draw_o(o[0],o[1])
    
    for rect in rects :
        pygame.draw.rect(screen,bordeau,rect,5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                for rect in rects :
                    if rect.collidepoint(pygame.mouse.get_pos()) :
                        if turn :
                            X.append(rect.center)
                            turn = False
                        else : 
                            O.append(rect.center)
                            turn = True

    pygame.display.flip()

pygame.quit()



