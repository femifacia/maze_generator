from .rectangle_maze import RectangleMaze

create_maze_map = {"rectangle":RectangleMaze}

def create_maze_objects_from_file(file : str) -> RectangleMaze:
    lines = list(filter(lambda x : x, file.split("\n")))
    return create_maze_map[lines[0]](file=lines)