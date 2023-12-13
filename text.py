import pygame

class Text:
    def __init__(self, text, font, col, x, y, window, col2=None):
        self.text = text
        self.font = font
        self.window = window
        self.col = col
        self.x = x
        self.y = y
        self.col2 = col2 if col2 is not None else col
        self.action = False

    def draw(self,bg_col=None,bg_border=None):
        words = str(self.text).split()
        lignes = []
        ligne = []

        for word in words:
            test_line = ligne + [word] if ligne else [word]
            test_text = ' '.join(test_line)
            test_size = self.font.size(test_text)

            if test_size[0] <= 1200:
                ligne = test_line
            else:
                lignes.append(ligne)
                ligne = [word]

        if ligne:
            lignes.append(ligne)

        y_offset = 0
        rect = None
        for ligne in lignes:
            line_text = ' '.join(ligne)
            img = self.font.render(line_text, True, self.col)
            rect = img.get_rect(topleft=(self.x, self.y + y_offset))
            
            if bg_border :
                pygame.draw.rect(self.window, bg_border, rect.inflate(38,38),border_radius=40)
            if bg_col:
                pygame.draw.rect(self.window, bg_col, rect.inflate(33,33),border_radius=40)


            if rect.collidepoint(pygame.mouse.get_pos()):
                img = self.font.render(line_text, True, self.col2)
                self.action = True

            self.window.blit(img, (self.x, self.y + y_offset))
            y_offset += img.get_height()

        return self.action