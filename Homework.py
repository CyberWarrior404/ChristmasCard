import pygame

pygame.init()

screen = pygame.display.set_mode([600, 350])
screen.fill("purple")

class Rectangle():
    def __init__(self, position, color, width, height):
        self.pos = position
        self.width = width
        self.height = height
        self.clr = color
    
    def draw(self):
        pygame.draw.rect(screen, self.clr, (*self.pos, self.width, self.height))
 #self.Draw_Rect = pygame.draw.rect(self.rect_surface, self.rect_color, pygame.Rect(self.rect_pos, self.rect_size), self.rect_width)     
    def grow(self, dw, dh):
        self.width += dw
        self.height += dh
        pygame.draw.rect(screen, self.clr, (*self.pos, self.width, self.height))

object = Rectangle((250, 150), "black", 100, 50)
object1 = Rectangle((250, 150), "gray", 80, 30)
object2= Rectangle((250, 150), "white", 50, 20)
obj=[object, object1, object2]
object.clr="orange"
while True:
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            print("clicked")
            for i in obj:
                i.draw()
        elif e.type == pygame.MOUSEBUTTONUP:
            for i in obj:
                i.grow(10, 5)
            print("released")
        elif e.type == pygame.MOUSEMOTION:
            print("moving mouse")
            o= Rectangle(pygame.mouse.get_pos(), "Orange", 10, 10)
            o.draw()
        
    pygame.display.update()