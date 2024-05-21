import queue

def a_star(graph, start, goal, heuristic_func):
    total_cost = {start: 0}
    parent = {start: None}
    open_list = queue.PriorityQueue()
    open_list.put((0, start))
    closed_set = set()

    while not open_list.empty():
        _, current_node = open_list.get()

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, total_cost[goal]

        closed_set.add(current_node)

        for neighbor in graph.neighbors(current_node):
            tentative_cost = total_cost[current_node]
            for u, v, data in graph.edges(current_node, data=True):
                if v == neighbor:
                    tentative_cost += data.get('length', 0)
                    break
            
            if neighbor not in total_cost or tentative_cost < total_cost[neighbor]:
                total_cost[neighbor] = tentative_cost
                parent[neighbor] = current_node
                heuristic_value = heuristic_func(graph, neighbor, goal)
                f_score = tentative_cost + heuristic_value
                open_list.put((f_score, neighbor))
    return None, None
