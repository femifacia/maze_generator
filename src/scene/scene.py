#!/usr/bin/env python3

import pygame

class Scene:
    
    def call_other_scene(self, name : str) -> None:
        self.core.scene_map[name].loop(None)
    def draw_button(self) -> None:
        for button in self.button_arr:
            button.update(self)
            button.draw(self.core.screen)
    
    def draw_elements(self) -> None:
        self.draw_button()
        for i in self.graphical_elements_arr:
            i.update(self)
            i.draw(self)
    
    def loop(self, args : list) -> None:
        if self.loop_ptr:
            self.loop_ptr(args)
            return
        self.is_running = 1
        while self.is_running and self.core.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    self.core.is_running = False
            self.core.screen.fill(self.background_color_rgb)
            self.draw_elements()
#            pygame.display.flip()
            pygame.display.update()

    def __init__(self, core, name="empty",loop_ptr  = None) -> None:
        self.loop_ptr = loop_ptr
        self.button_arr = []
        self.core = core
        self.background_color_rgb = (10,55,100)
        self.is_running = True
        self.name = name
        self.graphical_elements_arr = []
        self.graphical_elements_map = {}
    
    def add_graphical_element(self, element, key=""):
        if key:
            self.graphical_elements_map[key]=element
        self.graphical_elements_arr.append(element)
    
    def add_button(self, button) -> None:
        self.button_arr.append(button)