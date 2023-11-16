from collections import deque

def filling_right_path(graph : list, end, prev):
    curr = (end[0], end[1])
    while (prev.get(curr, None)):
        graph[curr[1]][curr[0]] = '0'
        curr = prev[curr]
    graph[curr[1]][curr[0]] = "0"

def bfs(graph : list, start : tuple, end : tuple) -> int:
    if start == end:
        graph[end[1][0]] = "0"
        return 0,0
    size = 0
    count = 0
    prev = {}
    to_see = deque([start + (0,)])
    height = len(graph)
    width = len(graph[0])
    graph[start[1]][start[0]] = "x"
    while to_see:
        count+=1
        current = to_see.popleft()
        x,y = current[0],current[1]
        for i,j in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if 0 <= i < height and 0 <= j < width:
                if (j,i) == end:
                    prev[(j,i)] = (x,y)
                    filling_right_path(graph, end, prev)
                    return (current[2] + 1, count)
                elif graph[i][j] == " ":
                    graph[i][j] = "x"
                    prev[(j,i)] = (x,y)
                    to_see.append((j,i,current[2] + 1))
    return -1, count

#graph = [["#","#"," "],
#         ["#","#"," "],
#         ["#","#"," "]]

#[print(i) for i in graph]
#print('after')
#print(bfs(graph,(0,1),(2,2)))
#[print(i) for i in graph]
