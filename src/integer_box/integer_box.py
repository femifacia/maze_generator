import pygame

class IntegerBox:

    def draw(self, scene) -> None:
        screen = scene.core.screen
        pygame.draw.rect(screen,self.color_background_input, self.rect_input, border_radius=8)
        screen.blit(self.text_render, (self.pos[0] + 2, self.pos[1] + 2))
        screen.blit(self.legend_text, (self.pos[0] + self.shift[0], self.pos[1] + self.shift[1]))
    
    def update(self, info):
        pass
    
    def __init__(self, pos = (10,10), val_min = 1, val_max = 1000, legend=" height ",
                 radius=1,color="black$white$green", color_legend="black$cyan",font_size=16, font_path="", 
                 font_system="arial", shift=(10,30)) -> None:
        self.pos = pos
        self.shift = shift
        self.font=None
        if font_system:
            self.font = pygame.font.SysFont(font_system, font_size)
        self.color_background_input,self.color_foreground_input,self.color_selected_input = color.split('$')
        self.color_foreground_legend, self.color_background_legend = color_legend.split("$")
        self.rect_input= pygame.Rect(pos[0], pos[1], len(str(val_max))*font_size,font_size + 4)
        self.selected=0
        self.val = '1'
        self.text_render = self.font.render(self.val,1,self.color_foreground_input)
        self.legend_text = self.font.render(legend,1, self.color_foreground_legend, self.color_background_legend)
#        self.text
        pass