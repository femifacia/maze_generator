#!/usr/bin/env python3


import pygame

class TextButton(pygame.sprite.Sprite):

    def exec_button(self, scene) -> None:
        pygame.time.delay(100)
        if not self.scene_name_bound and self.ptr_bound:
            self.ptr_bound([scene])
        elif self.scene_name_bound:
            scene.call_other_scene(self.scene_name_bound)

    def draw(self, screen : pygame.Surface) -> None:
        pygame.draw.rect(screen,self.color_background_selected, self.rect_sprite_selected, border_radius=8)
        screen.blit(self.sprite_selected, self.pos)
#        screen.blit()
#        pygame.draw.(screen, self.sprite_normal, 100,100)
#        self.rect_sprite_normal.d
#        self.sprite_normal.draw(screen)
    
    def update(self, scene) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_sprite_selected.collidepoint(mouse_pos):
            self.sprite_selected = self.sprite_hover
            self.rect_sprite_selected = self.rect_sprite_hover
            self.color_background_selected = self.color_background_hover
            if pygame.mouse.get_pressed()[0] and self.is_pressed == 0:
                self.exec_button(scene)
                self.is_pressed = 1
            if pygame.mouse.get_pressed()[0] == 0:
                self.is_pressed = 0
        else:
            self.sprite_selected = self.sprite_normal
            self.rect_sprite_selected = self.rect_sprite_normal
            self.color_background_selected = self.color_background_normal
        

    def __init__(self, x = 100, y = 100, text_normal="Hello",text_hover='Hello', font_size=16, font_system="Arial",
                 font_path = "", scene_name_bound="", ptr_bound=None, color_normal="blue$white",
                 color_hover='red$white') -> None:
        super().__init__()
        self.surface = None
        self.font = None
        if font_system:
            self.font = pygame.font.SysFont(font_system, font_size)
        
        self.color_background_normal, self.color_foreground_normal = color_normal.split("$")
        self.color_background_hover, self.color_foreground_hover = color_hover.split("$")
        self.sprite_normal = self.font.render(text_normal, 1, self.color_foreground_normal)
        self.rect_sprite_normal = self.sprite_normal.get_rect()
        self.rect_sprite_normal.x, self.rect_sprite_normal.y = x,y
        self.sprite_hover = self.font.render(text_hover, 1, self.color_foreground_hover)
        self.rect_sprite_hover = self.sprite_hover.get_rect()
        self.rect_sprite_hover.x, self.rect_sprite_hover.y = x,y
        self.sprite_selected = self.sprite_normal
        self.rect_sprite_selected = self.rect_sprite_normal
        self.color_background_selected = self.color_background_normal
        self.color_foreground_selected = self.color_foreground_normal
        self.scene_name_bound = scene_name_bound
        self.ptr_bound = ptr_bound
        self.pos = (x,y)
        self.is_pressed = 0

        
