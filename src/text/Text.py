import pygame

class Text:
    
    def update(self, info):
        pass
    
    def change_text(self, text):
        self.sprite = self.font.render(text,1, self.color_foreground, self.color_background)    
    
    def draw(self, scene):
        screen = scene.core.screen
        screen.blit(self.sprite, self.pos)
        
    
    def __init__(self, pos=(10,10), text="hello", font_size=16, color="white$black", font_system="Arial") -> None:
        self.font = pygame.font.SysFont(font_system, font_size)
        self.pos = pos
        self.color_foreground , self.color_background = color.split('$')
        self.sprite = self.font.render(text,1, self.color_foreground, self.color_background)