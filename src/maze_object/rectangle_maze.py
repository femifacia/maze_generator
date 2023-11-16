
import maze_generation_algorythm
import maze_solve_algorithm
import text

rectangle_generate = {"dfs_random":maze_generation_algorythm.dfs_random,
                      'femi_random':maze_generation_algorythm.dfs_random,
                      'backtracking_random':maze_generation_algorythm.dfs_random,
                      'full_obtsacle':maze_generation_algorythm.full_obstacle,
                      'full_space':maze_generation_algorythm.full_space}

rectangle_solve = {"bfs" : maze_solve_algorithm.bfs,
                   "dfs" : maze_solve_algorithm.dfs}
import pygame

class RectangleMaze:
    
    def solve(self, algo : str) -> None:
        self.graph = []
        for i in self.graph_origin:
            self.graph.append(i[:])
        self.size_path, self.iter =  rectangle_solve[algo](self.graph, self.start, self.end)
        
    
    def dup(self):
        #essaye de mettre le is_dup a 1
        elm = RectangleMaze(height=self.height, width=self.width, pos=self.pos,cell_size=self.cell_size)
        elm.graph = []
        for i in self.graph:
            elm.graph.append(i[:])
        elm.graph_origin = []
        for i in self.graph:
            elm.graph_origin.append(i[:])
        return elm
    
    def update(self, screen) -> None:
        pass
    
    def draw(self, scene) -> None:
        mouse_pos = pygame.mouse.get_pos()
        pos = list(self.pos)
        rect = pygame.Rect(5,5,5,5)
        free_rect = None if not "free_rect" in scene.graphical_elements_map else scene.graphical_elements_map["free_rect"] 
        obstacle_rect = None if not "obstacle_rect" in scene.graphical_elements_map else scene.graphical_elements_map["obstacle_rect"] 
        start_rect = scene.graphical_elements_map.get("start", None)
        end_rect = scene.graphical_elements_map.get("end", None)
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                color = "white" if self.graph[i][j] == " " else ("red" if self.graph[i][j] == '#' else "green")
                if self.graph[i][j] == "0":
                    color = 'green'
                if self.graph[i][j] == "x":
                    color = 'violet'
                rect.x, rect.y = pos[0], pos[1]
                if rect.collidepoint(mouse_pos):
                    pygame.draw.rect(scene.core.screen,self.color_hover, rect, border_radius=1)
                    if pygame.mouse.get_pressed()[0]:
                        if free_rect and free_rect.selected:
                            self.graph[i][j] = " "
                        if obstacle_rect and obstacle_rect.selected:
                            self.graph[i][j] = "#"
                        if start_rect and start_rect.selected:
                            self.start = (j,i)
                        if end_rect and end_rect.selected:
                            self.end = (j,i)
                else:
                    pygame.draw.rect(scene.core.screen,color, rect, border_radius=1)
                    if end_rect and (j,i) == self.end:
                        pygame.draw.rect(scene.core.screen,end_rect.color_normal, rect, border_radius=1)
                    if start_rect and (j,i) == self.start:
                        pygame.draw.rect(scene.core.screen,start_rect.color_normal, rect, border_radius=1)
                        
#                pygame.draw.rect(scene.core.screen,color, rect, border_radius=8)
                pos[0] += 5
            pos[0] = self.pos[0]
            pos[1] += 5
        if self.size_path != -1:
            string = " Size Path found : " + str(self.size_path) 
            textt = text.Text(text=string) 
            textt.draw(scene)
        if self.iter != -1:
            string = " Nbr iterations : " + str(self.iter) 
            textt = text.Text(pos=(10,25),text=string) 
            textt.draw(scene)
    def get_str(self) -> None:
        string = self.type + "\n"
        for i in self.graph:
            for j in i:
                string += j
            string += "\n"
        return string
    
    def init_from_file(self,lines : list,color_hover="yellow",cell_size=(5,5)):
        lines = lines[1:]
        self.size_path = -1
        self.graph = []
        for i in lines:
            tmp = list(i)
            tmp = tmp[:-1] if tmp[-1] == "\n" else tmp
            self.graph.append(tmp)
        if self.graph == []:
            self.graph = [[]]
        self.graph_origin = []
        for i in self.graph:
            self.graph_origin.append(i[:])
        if self.graph_origin == []:
            self.graph_origin = [[]]
        self.height = len(self.graph)
        self.width = len(self.graph[0])
        self.pos = (10, 140)
        self.type="rectangle"
        self.color_hover = color_hover
        self.cell_size = cell_size
        self.rect = pygame.Rect(self.pos, (cell_size[0] * self.width, cell_size[1] * self.height))
        pass
    
    def __init__(self, height = 10, width = 8, pos = (10, 140), algo="dfs_random", color_hover="yellow",cell_size=(5,5),file=None, is_dup=0) -> None:
        self.start = None
        self.size_path = -1
        self.iter = -1
        self.end = None
        if file:
            self.init_from_file(file)
            return
        self.graph = None
        if not is_dup:
            self.graph = rectangle_generate[algo](height,width)
            self.graph_origin = []
            for i in self.graph:
                self.graph_origin.append(i[:])
        self.pos = pos
        self.type="rectangle"
        self.color_hover = color_hover
        self.cell_size = cell_size
        self.rect = pygame.Rect(pos, (cell_size[0] * width, cell_size[1] * height))
        self.height = height
        self.width = width