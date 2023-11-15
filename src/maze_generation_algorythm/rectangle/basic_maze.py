

def full_obstacle(height : int, width : int) -> list:
    graph = [["#" for i in range(width)] for j in range(height)]
    return graph

def full_space(height : int, width : int) -> list:
    graph = [[" " for i in range(width)] for j in range(height)]
    return graph