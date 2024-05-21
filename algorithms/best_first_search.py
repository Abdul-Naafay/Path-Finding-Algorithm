import queue

def best_first_search(G, start, goal, heuristic_func=euclidean_heuristic):
    open_list = queue.PriorityQueue()
    open_list.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set()

    while not open_list.empty():
        _, current = open_list.get()
        visited.add(current)

        if current == goal:
            break

        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                cost_so_far[neighbor] = cost_so_far[current] + G[current][neighbor][0]['length']
                priority = heuristic_func(neighbor, goal, G)
                open_list.put((priority, neighbor))
                came_from[neighbor] = current

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path, cost_so_far[goal]
