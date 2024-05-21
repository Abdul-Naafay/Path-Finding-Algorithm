import osmnx as ox
from utils.visualize import visualize_road_network, visualize_path_folium
from utils.a_star import a_star
from utils.best_first_search import best_first_search
from utils.bfs import bfs
from utils.heuristics import euclidean_heuristic, manhattan_heuristic, haversine_heuristic

def main():
    location = "LUMS Lahore, Pakistan"
    distance = 500
    source = 810005319  # SSE
    destination = 11337034500  # SDSB

    G = ox.graph_from_address(location, network_type='walk', dist=distance)
    visualize_road_network(G, location, distance)

    # A* with different heuristics
    for heuristic in [euclidean_heuristic, manhattan_heuristic, haversine_heuristic]:
        path, dist = a_star(G, source, destination, heuristic)
        visualize_path_folium(G, path, location, source, [destination], dist)

    # Best-First Search
    path, dist = best_first_search(G, source, destination, euclidean_heuristic)
    visualize_path_folium(G, path, location, source, [destination], dist)

    # Informed BFS
    path, dist = bfs(G, source, destination, euclidean_heuristic)
    visualize_path_folium(G, path, location, source, [destination], dist)

if __name__ == "__main__":
    main()
