def bfs(graph, start, goal, heuristic_func=euclidean_heuristic):
    # Initialization
    queue = []
    visited = set()
    path_cost = {start: (0, None)}
    queue.append(start)
    visited.add(start)

    while queue:
        
        current_node = queue.pop(0)

        if current_node == goal: 
            shortest_path = []
            while current_node is not None:
                shortest_path.append(current_node)
                current_node = path_cost[current_node][1]
            shortest_path.reverse()
            # for node, (cost, _) in path_cost.items():
            #     print(f"Cost to reach node {node}: {cost}")
            return shortest_path, path_cost[goal][0]

        # Explore neighbors
        for neighbor in graph.neighbors(current_node):
            # Calculate the cost to reach the neighbor
            neighbor_cost = path_cost[current_node][0]
            for u, v, data in graph.edges(current_node, data=True):
                if v == neighbor:
                    neighbor_cost += data.get('length', 0)
                    break
            # print(current_node, "->",neighbor)
            # print(neighbor_cost)
            # If the neighbor has not been visited before
            if neighbor not in visited:
                visited.add(neighbor)
                # Update path cost to the neighbor
                path_cost[neighbor] = (neighbor_cost, current_node)
                queue.append(neighbor)

    return None, None
