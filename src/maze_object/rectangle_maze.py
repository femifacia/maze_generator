
import maze_generation_algorythm

rectangle_generate = {"dfs_random":maze_generation_algorythm.dfs_random}
import pygame

class RectangleMaze:
    
    def update(self, screen) -> None:
        pass
    
    def draw(self, scene) -> None:
        pos = list(self.pos)
        rect = pygame.Rect(5,5,5,5)
        for i in self.graph:
            for j in i:
                color = "white" if j == " " else ("red" if j == '#' else "green")
                rect.x, rect.y = pos[0], pos[1]
                pygame.draw.rect(scene.core.screen,color, rect, border_radius=8)
                pos[0] += 5
            pos[0] = self.pos[0]
            pos[1] += 5
            
    
    def __init__(self, height = 10, width = 8, pos = (100, 300), algo="dfs_random") -> None:
        self.graph = rectangle_generate[algo](height,width)
        self.pos = pos