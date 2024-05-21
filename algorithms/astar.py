import numpy as np
import queue

def euclidean_heuristic(node1, node2, G):
    x1, y1 = G.nodes[node1]['x'], G.nodes[node1]['y']
    x2, y2 = G.nodes[node2]['x'], G.nodes[node2]['y']
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def manhattan_heuristic(node1, node2, G):
    x1, y1 = G.nodes[node1]['x'], G.nodes[node1]['y']
    x2, y2 = G.nodes[node2]['x'], G.nodes[node2]['y']
    return abs(x2 - x1) + abs(y2 - y1)

def haversine_heuristic(node1, node2, G):
    lat1, lon1 = np.radians(G.nodes[node1]['y']), np.radians(G.nodes[node1]['x'])
    lat2, lon2 = np.radians(G.nodes[node2]['y']), np.radians(G.nodes[node2]['x'])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return 6371.0 * c

def a_star(G, start, goal, heuristic='euclidean'):
    heuristics = {
        'euclidean': euclidean_heuristic,
        'manhattan': manhattan_heuristic,
        'haversine': haversine_heuristic
    }
    heuristic_func = heuristics[heuristic]
    open_list = queue.PriorityQueue()
    open_list.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            break

        for neighbor in G.neighbors(current):
            new_cost = cost_so_far[current] + G[current][neighbor][0]['length']
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_func(neighbor, goal, G)
                open_list.put((priority, neighbor))
                came_from[neighbor] = current

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path, cost_so_far[goal]
