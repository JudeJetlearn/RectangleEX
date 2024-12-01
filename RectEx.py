import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))

red = (255,0,0)
pygame.display.update()


class Rect():
    def __init__(self,color,top_left,side_lenght):
        self.rect_color = color
        self.rect_top_left = top_left
        self.rect_side_lenght = side_lenght
        self.rect_surface = screen

    def draw(self):
        self.draw_Rect = pygame.draw.rect(self.rect_surface, self.rect_color, (self.rect_top_left[0], self.rect_top_left[1]), self.rect_side_lenght, self.rect_side_lenght) 


    def grow(self,r):
        self.rect_side_lenght = self.rect_side_lenght+r
        self.draw_Rect = pygame.draw.rect(self.rect_surface, self.rect_color, (self.rect_top_left[0], self.rect_top_left[1]), self.rect_side_lenght, self.rect_side_lenght) 

rect = Rect(red,(300,300),25)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            rect.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            rect.grow(20)
            pygame.display.update()
