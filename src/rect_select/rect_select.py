import pygame

class RectSelect:
        

    def draw(self, scene) -> None:
        screen = scene.core.screen
        if self.hover or self.selected:
            pygame.draw.rect(screen,self.color_selected, self.rect_selected, 4)
            
        pygame.draw.rect(screen,self.color_normal, self.rect)
#        screen.blit(self.text_render, (self.pos[0] + 2, self.pos[1] + 2))
        screen.blit(self.legend_text, (self.pos[0] + self.shift[0], self.pos[1] + self.shift[1]))
    
    def update(self, scene):
        pos = pygame.mouse.get_pos()
        rect_maze = None if not scene.graphical_elements_map.get('maze',None) else scene.graphical_elements_map["maze"].rect
        if self.rect.collidepoint(pos):
            self.hover = 1
            if pygame.mouse.get_pressed()[0]:
                self.selected = 1
        elif  pygame.mouse.get_pressed()[0] and (not rect_maze or not rect_maze.collidepoint(pos)):
            self.selected = 0
            self.hover = 0
        else:
            self.hover = 0
        
#                print(scene.last_event.unicode)
            
#            key = pygame.key.get_pressed()
#            print(key)
    
    def __init__(self, pos = (10,10), dimension=(10,10), legend=" height ",
                 radius=0,color="white$green", color_legend="black$cyan",font_size=16, font_path="", 
                 font_system="arial", shift=(10,30),content=" ") -> None:
        self.pos = pos
        self.shift = shift
        self.font=None
        if font_system:
            self.font = pygame.font.SysFont(font_system, font_size)
        self.color_normal, self.color_selected = color.split('$')
        self.color_foreground_legend, self.color_background_legend = color_legend.split("$")
        self.rect= pygame.Rect(pos[0], pos[1], dimension[0], dimension[1])
        self.rect_selected = pygame.Rect(self.rect)
        self.rect_selected.width += 5
        self.rect_selected.height += 5
        self.rect_selected.top -=3
        self.rect_selected.left -=3
        self.selected=0
        self.hover = 0
        self.content = content
        self.legend_text = self.font.render(legend,1, self.color_foreground_legend, self.color_background_legend)
#        self.text
        pass