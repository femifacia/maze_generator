import pygame
import time

class IntegerBox:
    
    def get_val(self) -> None:
        try:
            val = int(self.val)
            assert val > self.val_min
            if self.val_max < val:
                self.val = str(self.val_max)
        except:
            self.val = str(self.val_min)
        self.text_render = self.font.render(self.val,1,self.color_foreground_input)
        return int(self.val)
        

    def draw(self, scene) -> None:
        screen = scene.core.screen
        if self.hover or self.selected:
            rect = pygame.Rect(self.rect_input)
            rect.width = 100
            pygame.draw.rect(screen,self.color_selected_input, self.rect_input_selected, 4,border_radius=8)
            
        pygame.draw.rect(screen,self.color_background_input, self.rect_input, border_radius=8)
        screen.blit(self.text_render, (self.pos[0] + 2, self.pos[1] + 2))
        screen.blit(self.legend_text, (self.pos[0] + self.shift[0], self.pos[1] + self.shift[1]))
    
    def update(self, scene):
        pos = pygame.mouse.get_pos()
        if self.rect_input.collidepoint(pos):
            self.hover = 1
            if pygame.mouse.get_pressed()[0]:
                self.selected = 1
        elif  pygame.mouse.get_pressed()[0]:
            self.selected = 0
            self.hover = 0
        else:
            self.hover = 0
        if self.selected:
            if scene.last_event and scene.last_event.type == pygame.KEYDOWN:
                if len(self.val) and scene.last_event.key == pygame.K_BACKSPACE:
                    if (time.time() - self.backspace_time >= self.backspace_delay):
                        if len(self.val) == 1:
                            self.val = " "
                        else:
                            self.val = self.val[:-1]
                        self.backspace_time = time.time()
#                    pygame.time.delay(300)
                    
                elif len(self.val) < self.max_digit:
                    if self.val == " ":
                        self.val = ""
                    self.val += scene.last_event.unicode
                self.text_render = self.font.render(self.val,1,self.color_foreground_input)
#                print(scene.last_event.unicode)
            
#            key = pygame.key.get_pressed()
#            print(key)
    
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
        self.rect_input_selected = pygame.Rect(self.rect_input)
        self.rect_input_selected.width += 5
        self.rect_input_selected.height += 5
        self.rect_input_selected.top -=3
        self.rect_input_selected.left -=3
        self.selected=0
        self.hover = 0
        self.val = '1'
        self.text_render = self.font.render(self.val,1,self.color_foreground_input)
        self.legend_text = self.font.render(legend,1, self.color_foreground_legend, self.color_background_legend)
        self.backspace_time = time.time()
        self.backspace_delay = 0.2
        self.max_digit = 6
        self.val_max = val_max
        self.val_min = val_min
#        self.text
        pass