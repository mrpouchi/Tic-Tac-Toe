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

def draw_tab1():
    return [(pygame.Rect(0,0,w,h),True)for h in range(0,1000,333)for w in range(0,1000,333) ]






run = True
turn = False
X = []
O = []
while run:
    screen.fill((31,31,31))

    rects = draw_tab1()

    for x in X :
        draw_x(x[0],x[1])
    for o in O :
        draw_o(o[0],o[1])
    
    for rect in rects :
        pygame.draw.rect(screen,bordeau,rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                for rect in rects :
                    if rect[0].collidepoint(pygame.mouse.get_pos()) and rect[1]:
                        if turn :
                            X.append(rect[0].center)
                            turn = False
                            rect[1] = False
                        else : 
                            O.append(rect[0].center)
                            turn = True
                            rect[1] = False

    pygame.display.update()

pygame.quit()



