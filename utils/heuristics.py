import numpy as np

def euclidean_heuristic(G, node1, node2):
    x1, y1 = G.nodes[node1]['x'], G.nodes[node1]['y']
    x2, y2 = G.nodes[node2]['x'], G.nodes[node2]['y']
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def manhattan_heuristic(G, node1, node2):
    x1, y1 = G.nodes[node1]['x'], G.nodes[node1]['y']
    x2, y2 = G.nodes[node2]['x'], G.nodes[node2]['y']
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

def haversine_heuristic(G, node1, node2):
    lat1, lon1 = np.radians(G.nodes[node1]['y']), np.radians(G.nodes[node1]['x'])
    lat2, lon2 = np.radians(G.nodes[node2]['y']), np.radians(G.nodes[node2]['x'])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = 6371.0 * c
    return distance
