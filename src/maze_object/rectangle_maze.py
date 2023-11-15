
import maze_generation_algorythm

rectangle_generate = {"dfs_random":maze_generation_algorythm.dfs_random,
                      'femi_random':maze_generation_algorythm.dfs_random,
                      'backtracking_random':maze_generation_algorythm.dfs_random,
                      'full_obtsacle':maze_generation_algorythm.full_obstacle,
                      'full_space':maze_generation_algorythm.full_space}
import pygame

class RectangleMaze:
    
    def update(self, screen) -> None:
        pass
    
    def draw(self, scene) -> None:
        mouse_pos = pygame.mouse.get_pos()
        pos = list(self.pos)
        rect = pygame.Rect(5,5,5,5)
        free_rect = None if not "free_rect" in scene.graphical_elements_map else scene.graphical_elements_map["free_rect"] 
        obstacle_rect = None if not "obstacle_rect" in scene.graphical_elements_map else scene.graphical_elements_map["obstacle_rect"] 
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                color = "white" if self.graph[i][j] == " " else ("red" if self.graph[i][j] == '#' else "green")
                rect.x, rect.y = pos[0], pos[1]
                if rect.collidepoint(mouse_pos):
                    pygame.draw.rect(scene.core.screen,self.color_hover, rect, border_radius=1)
                    if pygame.mouse.get_pressed()[0]:
                        if free_rect and free_rect.selected:
                            self.graph[i][j] = " "
                        if obstacle_rect and obstacle_rect.selected:
                            self.graph[i][j] = "#"
                else:
                    pygame.draw.rect(scene.core.screen,color, rect, border_radius=1)
#                pygame.draw.rect(scene.core.screen,color, rect, border_radius=8)
                pos[0] += 5
            pos[0] = self.pos[0]
            pos[1] += 5
            
    def get_str(self) -> None:
        string = self.type + "\n"
        for i in self.graph:
            for j in i:
                string += j
            string += "\n"
        return string
    
    def __init__(self, height = 10, width = 8, pos = (100, 300), algo="dfs_random", color_hover="yellow",cell_size=(5,5)) -> None:
        self.graph = rectangle_generate[algo](height,width)
        self.pos = pos
        self.type="rectangle"
        self.color_hover = color_hover
        self.cell_size = cell_size
        self.rect = pygame.Rect(pos, (cell_size[0] * width, cell_size[1] * height))