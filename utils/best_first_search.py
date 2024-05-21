def best_first_search(graph, start, goal, heuristic_func=euclidean_heuristic):
    #initialization
    open_list = queue.PriorityQueue()
    visited = set()
    path = {}
    path_cost = {start: (0, None)}  #both parent and cost here. 0 cost, none parent.
    open_list.put((heuristic_func(start, goal), start))
    visited.add(start)
    
    path[start] = None

    while not open_list.empty():
        # Pop node with the lowest priority
        _, current_node = open_list.get()

        if current_node == goal:
            shortest_path = []
            while current_node is not None:
                shortest_path.append(current_node)
                current_node = path[current_node]
            shortest_path.reverse()
            return shortest_path, path_cost[goal][0]

        # Explore neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            if neighbor not in zz:
                visited.add(neighbor)
                # Add neighbor to the open list with priority based on heuristic estimate
                open_list.put((heuristic_func(neighbor, goal), neighbor))
                path[neighbor] = current_node
                # Update path cost to neighbour
                neighbor_cost = path_cost[current_node][0]  
                for u, v, data in graph.edges(current_node, data=True):
                    if v == neighbor:
                        neighbor_cost += data.get('length', 0)
                        break
                path_cost[neighbor] = (neighbor_cost, current_node)
                
    return None, None
