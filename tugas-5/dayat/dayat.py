# Since graph is unweighted, a BFS is enough, fwiw might be slower, idrk.
n, _ = map(int, input().split())
maze = [list(input()) for _ in range(n)]


# Maze to a graph that we can *ACTUALLY USE* :C
def mtg(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] != "#":
                node = (i, j)
                graph[node] = []

                # Check neighboring cells (up, down, right, left)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] != "#":
                        neighbor = (ni, nj)
                        graph[node].append(neighbor)

    start_point = None
    end_point = None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                start_point = (i, j)
            elif maze[i][j] == "E":
                end_point = (i, j)

    return (graph, start_point, end_point)


def reconstruct(start, target, parents, path=None):
    if path is None:
        path = []

    if target != start:
        path.insert(0, target)
        target = parents[target]
        return reconstruct(start, target, parents, path)

    path.insert(0, start)
    return path


def rappend(target, stuff):
    if stuff:
        target.append(stuff.pop(0))
        return rappend(target, stuff)
    return target


def rassign(target, keyvals):
    if keyvals:
        to_assign = keyvals.pop(0)
        target[to_assign[0]] = to_assign[1]
        return rassign(target, keyvals)
    return target


def bfs(graph, source, target, parents=None, visited=None, queue=None):
    if visited is None:
        visited = []

    if queue is None:
        queue = [source]

    if parents is None:
        parents = {}

    current = queue.pop()
    visited.append(current)

    if current == target:
        return reconstruct(source, target, parents)

    neighbors = graph[current]
    elig_neighbors = list(filter(lambda x: x not in visited, neighbors))

    queue = rappend(queue, elig_neighbors.copy())
    visited = rappend(visited, elig_neighbors.copy())
    parents = rassign(
        parents, list(zip(elig_neighbors.copy(), [current] * len(elig_neighbors)))
    )

    if queue:
        return bfs(graph, source, target, parents, visited, queue)

    return None


graph = mtg(maze)
if list(filter(lambda x: x is None, graph)):
    print("tempat mulai atau tempat tujuan tak tergambar")
    exit(1)
# print(graph[1], graph[2])

res = bfs(graph[0], graph[1], graph[2])
res.pop(0)
res.pop()
# print(res)


def modify_maze(maze, modifications):
    if not modifications:
        return maze
    mod = modifications.pop()
    maze[mod[0]][mod[1]] = "x"
    return modify_maze(maze, modifications)


print("\n".join(["".join(r) for r in modify_maze(maze.copy(), res.copy())]))
