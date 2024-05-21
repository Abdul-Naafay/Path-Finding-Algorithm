
### 3. `main.py`
The main script to run the pathfinding algorithms and visualize the results.

```python
from utils import get_road_network
from visualization.visualize import visualize_road_network, visualize_path_folium
from algorithms.astar import a_star
from algorithms.best_first_search import best_first_search
from algorithms.bfs import bfs

def main():
    location = "LUMS Lahore, Pakistan"
    distance = 500
    source = 643257622
    destination = 766933484

    G = get_road_network(location, distance)

    visualize_road_network(G, location, distance)

    # A* with Euclidean heuristic
    path_euclidean, cost_euclidean = a_star(G, source, destination, 'euclidean')
    visualize_path_folium(G, path_euclidean, location, source, [destination], cost_euclidean)

    # Best-First Search with Euclidean heuristic
    path_best_first, cost_best_first = best_first_search(G, source, destination)
    visualize_path_folium(G, path_best_first, location, source, [destination], cost_best_first)

    # Informed BFS with Euclidean heuristic
    path_bfs, cost_bfs = bfs(G, source, destination)
    visualize_path_folium(G, path_bfs, location, source, [destination], cost_bfs)

if __name__ == "__main__":
    main()
