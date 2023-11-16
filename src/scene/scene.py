#!/usr/bin/env python3

import pygame

class Scene:
    
    def call_other_scene(self, name : str) -> None:
        """Call a scene from another

        Args:
            name (str): target
        """
        self.core.scene_map[name].loop(None)
    
    def get_scene(self, name : str):
        """Get a scene from name

        Args:
            name (str): scene target

        Returns:
            Scene: scene target
        """
        return self.core.scene_map[name]

    def draw_button(self) -> None:
        """Draw each buttons
        """
        for button in self.button_arr:
            button.update(self)
            button.draw(self.core.screen)
    
    def draw_elements(self) -> None:
        """draw each graphical element
        """
        self.draw_button()
        for i in self.graphical_elements_arr:
            i.update(self)
            i.draw(self)
        car = self.graphical_elements_map.get("caroussel", None)
        if not car:
            return
        self.graphical_elements_map["maze"] = car.get_current_maze()
        if "maze" in self.graphical_elements_map and self.graphical_elements_map["maze"]:
            self.graphical_elements_map["maze"].update(self)
            self.graphical_elements_map["maze"].draw(self)
    
    def loop(self, args : list) -> None:
        """scene loop

        Args:
            args (list): some arguments likes scene or other infos
        """
        if self.loop_ptr:
            self.loop_ptr(args)
            return
        self.is_running = 1
        while self.is_running and self.core.is_running:
            self.last_event = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    self.core.is_running = False
                self.last_event = event
                for i in self.graphical_elements_arr:
                    i.update(self)
            self.core.screen.fill(self.background_color_rgb)
            self.draw_elements()
            pygame.display.flip()
            pygame.display.update()

    def __init__(self, core, name="empty",loop_ptr  = None) -> None:
        """constructor

        Args:
            core (core): the Core
            name (str, optional): _description_. Defaults to "empty".
            loop_ptr (_type_, optional): a function pointer. Defaults to None.
        """
        self.loop_ptr = loop_ptr
        self.button_arr = []
        self.core = core
        self.background_color_rgb = (10,55,100)
        self.is_running = True
        self.name = name
        self.graphical_elements_arr = []
        self.graphical_elements_map = {}
    
    def add_graphical_element(self, element, key=""):
        """add graphical element

        Args:
            element (_type_): element
            key (str, optional): the key. Defaults to "".
        """
        if key:
            self.graphical_elements_map[key]=element
        self.graphical_elements_arr.append(element)
    
    def add_button(self, button) -> None:
        """Add a button

        Args:
            button (_type_): the button
        """
        self.button_arr.append(button)