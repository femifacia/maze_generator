import pygame
import time
import button

def next_function(info : list):
    scene = info[0]
    scene.graphical_elements_map["caroussel"].next()


def prev_function(info : list):
    scene = info[0]
    scene.graphical_elements_map["caroussel"].prev()

class Caroussel:
    
    def update(self, scene) -> None:
        self.button_next.update(scene)
        self.button_prev.update(scene)
        
    def draw(self, scene) -> None:
        rect_title = self.get_current_rect_title()
        rect_legend = self.get_current_rect_legend()
        screen = scene.core.screen
        if rect_title:
            rect = rect_title.get_rect()
            rect.left, rect.top = self.pos[0], self.pos[1]
            pygame.draw.rect(screen,self.color_title_background, rect, border_radius=self.radius_title)
            screen.blit(rect_title, self.pos)
        if rect_legend:
            rect = rect_legend.get_rect()
            rect.left, rect.top = self.pos[0] + self.legend_shift[0], self.pos[1] + self.legend_shift[1]
            pygame.draw.rect(screen,self.color_title_background, rect, border_radius=self.radius_legend)
            screen.blit(rect_legend,( self.pos[0] + self.legend_shift[0], self.pos[1] + self.legend_shift[1]) )

        self.button_prev.update_pos((self.pos[0], self.pos[1] + 50))
        self.button_next.update_pos((self.pos[0] + rect.width - self.button_next.rect_sprite_selected.width, self.pos[1] + 50))
        self.button_next.draw(scene.core.screen)
        self.button_prev.draw(scene.core.screen)
    
    def next(self) -> None:
        self.index += 1
        if self.index >= self.size:
            self.index = 0
    
    def prev(self) -> None:
        self.index -= 1
        if self.index < 0:
            self.index = self.size - 1
    
    def create_rect(self, text:str, foreground : str, background : str) -> pygame.Rect:
        while len(text) < self.char_max:
            text += " "
            text = " " + text
        rect = self.font.render(text, 1, foreground)
        return rect
    
    def add_title(self, name : str, legend="time : ") -> None:
        self.arr.append(name)
        self.size += 1
        rect  = self.create_rect(name,self.color_title_foreground, self.color_title_background)
        self.rect_title_map[name] = rect
        if legend:
            self.add_legend(name, legend)
    
    def add_legend(self, title : str, legend : str) -> None:
        self.legend_map[title] = legend
        rect  = self.create_rect(legend,self.color_legend_foreground, self.color_legend_background)
        self.rect_legend_map[title] = rect        
    def get_legend(self, title : str) -> str:
        return self.legend_map.get(title, None)

    def get_current_title(self) -> str:
        return self.arr[self.index]
    
    def get_maze(self, title : str) -> str:
        return self.maze_map.get(title, None)
    
    def get_current_maze(self) -> list:
        return self.get_maze(self.get_current_title())
    
    def get_current_rect_title(self) -> pygame.Rect:
        return self.rect_title_map.get(self.get_current_title(), None)
    
    def get_current_rect_legend(self) -> pygame.Rect:
        return self.rect_legend_map.get(self.get_current_title(), None)
    
    def add_maze_current(self, maze : list) -> None:
        self.maze_map[self.get_current_title()] = maze
    
    def __init__(self, pos = (200,10), prev_shift = (0,20), next_shift=(10,20), legend_shift=(0,25), prev_text="<-", next_text="->",
                 title_color="white$black", legend_color="white$black", font_size=16, font_path="",
                 font_system="Arial", color_next_prev="black$cyan", radius_title=8, radius_legend=8,
                 char_max=22) -> None:
        self.pos = pos
        self.prev_shift = prev_shift
        self.next_shift = next_shift
        self.legend_shift = legend_shift
        self.index = 0
        self.arr = []
        self.legend_map = {}
        self.maze_map = {}
        self.size = 0
        self.time = time.time()
        self.font = None
        if font_system:
            self.font = pygame.font.SysFont(font_system, font_size)
        self.color_next_prev_foreground, self.color_next_prev_background = color_next_prev.split('$')
        self.rect_prev = self.font.render(prev_text,1, self.color_next_prev_foreground, self.color_next_prev_background)
        self.rect_next = self.font.render(next_text,1, self.color_next_prev_foreground, self.color_next_prev_background)
        self.color_title_foreground, self.color_title_background = title_color.split("$")
        self.color_legend_foreground, self.color_legend_background = legend_color.split("$")
        self.rect_title_map = {}
        self.rect_legend_map = {}
        self.button_next = button.TextButton(10,40, " -> "," -> ",ptr_bound=next_function)
        self.button_prev = button.TextButton(60,40," <- "," <- ",ptr_bound=prev_function)
        self.char_max=char_max
        self.radius_title = radius_title
        self.radius_legend = radius_legend