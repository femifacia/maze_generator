#!/usr/bin/env python3

import pygame
import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame_gui.elements.ui_button import UIButton

import scene
import button
import maze_object
import integer_box
import rect_select

def generate_rectangle_maze_function(info : list) -> None:
    scene = info[0]
    height = scene.graphical_elements_map["height"].get_val()
    width = scene.graphical_elements_map["width"].get_val()
    if not 'maze' in scene.graphical_elements_map:
        graph = maze_object.RectangleMaze(height,width,(10,140))
        scene.graphical_elements_map['maze'] = graph
#        scene.graphical_elements_arr.append(graph)
    else:
#        elm = scene.graphical_elements_map['maze']
#        scene.graphical_elements_arr.pop(scene.graphical_elements_arr.index(elm))
#        del elm
        graph = maze_object.RectangleMaze(height,width,(10,140))
        scene.graphical_elements_map['maze'] = graph
#        scene.graphical_elements_arr.append(graph)
        
def save_maze_function(info : list) -> None:
    scene = info[0]
    manager = pygame_gui.UIManager((700, 700))
    clock = pygame.time.Clock()
    background = pygame.Surface((700, 700))
    background.fill(pygame.Color('#000000'))

    file_selection_button = UIButton(relative_rect=pygame.Rect(150, 250, 150, 150),
                                    manager=manager, text='Select File')
    back_button = UIButton(relative_rect=pygame.Rect(50, 50, 150, 150),
                                    manager=manager, text='<-')
    is_ok = 1
    file_selection = None

    while is_ok:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        is_ok = 0
                    if event.ui_element == file_selection_button:
                        file_selection = UIFileDialog(rect=pygame.Rect(0, 0, 300, 300), manager=manager, allow_picking_directories=True)

                    if file_selection and event.ui_element == file_selection.ok_button:
                        path = file_selection.current_file_path
                        try:
                            fd = open(path, 'w')
                            string = "" if  (not "maze" in scene.graphical_elements_map or not scene.graphical_elements_map["maze"]) else scene.graphical_elements_map["maze"].get_str() 
                            fd.write(string)
                            fd.close()
                            is_ok = 0
                        except:
                            print("Can't save your maze at", path)
                            is_ok = 0

            manager.process_events(event)

        manager.update(time_delta)
        scene.core.screen.blit(background, (0, 0))
        manager.draw_ui(scene.core.screen)

        pygame.display.update()
def generate_rectangle_maze(core) -> scene.Scene:
    elm = scene.Scene(core, "generate_rectangle_maze")
    generate_button = button.TextButton(text_normal="      GENERATE       ", text_hover="      GENERATE       ", ptr_bound=generate_rectangle_maze_function)
    save_button = button.TextButton(x = 250, text_normal="      SAVE       ", text_hover="      SAVE       ", ptr_bound=save_maze_function)
    elm.add_button(save_button)
    elm.add_button(generate_button)
    elm.add_graphical_element(integer_box.IntegerBox(), "height")
    elm.add_graphical_element(integer_box.IntegerBox((80,10),legend=" width "), "width")
    elm.add_graphical_element(rect_select.RectSelect((390,10),legend=" space ",shift=(-10,20)), "free_rect" )
    elm.add_graphical_element(rect_select.RectSelect((450,10),legend=" obstacle ",shift=(-10,20),color="red$green",content="#"), "obstacle_rect" )
    return elm

def select_type_maze_generate_scene(core) -> scene.Scene:
    elm = scene.Scene(core,"select_type_maze_generate")
    rectangle_button = button.TextButton(text_normal="      RECTANGLE       ", text_hover="      RECTANGLE       ", scene_name_bound="generate_rectangle_maze")
    elm.add_button(rectangle_button)    
    return elm

def main_scene(core) -> scene.Scene:
    elm = scene.Scene(core,'main')
    generate_button = button.TextButton(text_normal="      GENERATE MAZE       ", text_hover="      GENERATE MAZE       ", scene_name_bound="select_type_maze_generate")
    quit_button = button.TextButton(y=150,text_normal="      QUIT       ", text_hover="      QUIT       ", scene_name_bound="quit")
    elm.add_button(quit_button)
    elm.add_button(generate_button)
    
    return elm

def quit_scene(core) -> scene.Scene:
    elm = scene.Scene(core,'quit')
    yes_button = button.TextButton(50,text_normal="      YES       ", text_hover="      YES       ",ptr_bound=quit_function)
    non_button = button.TextButton(150,text_normal="      NO LET's MAZEEEE       ", text_hover="      NO LET's MAZEEEE       ", ptr_bound=back_function)
    elm.add_button(yes_button)
    elm.add_button(non_button)
    
    return elm

def back_function(infos : list) -> None:
    infos[0].is_running = 0

def quit_function(infos : list) -> None:
    infos[0].core.is_running = 0