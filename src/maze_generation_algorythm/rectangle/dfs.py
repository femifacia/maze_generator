import random

def dfs_random(height : int, width : int) -> list[list[str]]:
    graph = [["E" for i in range(width)] for j in range(height)]
    to_start = (random.randint(0,height-1),random.randint(0,width-1))
    to_see = [to_start]
    graph[to_start[0]][to_start[1]] = " " if not random.randint(0,1) else "#"
    while (to_see):
        current = to_see.pop()
        y = current[0]
        x = current[1]
        for i,j in [(y + 1,x), (y-1,x), (y, x + 1),(y, x - 1)]:
            if 0 <= i < height and 0 <= j < width:
                if graph[i][j] == 'E':
                    graph[i][j] = " " if not random.randint(0,1) else "#"
                    to_see.append((i,j))
    return graph