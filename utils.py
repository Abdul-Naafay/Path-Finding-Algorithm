import osmnx as ox

def get_road_network(location, distance):
    G = ox.graph_from_address(location, network_type='walk', dist=distance)
    return G
