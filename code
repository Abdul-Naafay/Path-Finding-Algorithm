############################
# starter.py
# Name: Abdul Naafay
############################
import osmnx as ox
from IPython.display import IFrame
import networkx as nx
import folium
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import queue

# Get the road network data from OpenStreetMap
def get_road_network(location, distance):
    G = ox.graph_from_address(location, network_type='walk', dist=distance)
    return G
# Function to visualize the road network using Folium
def visualize_road_network(G, location, distance):
    """
        G: Graph object representing the road network
        location: location for which the road network is to be visualized
        distance: distance (in meters) around the specified location to be visualized
    """
    # Get the center (latitude and longitude) coordinates of the location
    lat, lng = ox.geocode(location)

    # Create a folium map centered at the location with an initial zoom level of 12
    map_center = [lat, lng]
    map_osm = folium.Map(location=map_center, zoom_start=12)

    # Add the road network graph (represented by "G") to the folium map
    # This overlays the road network onto the map, showing roads, intersections, and other features
    ox.plot_graph_folium(G, graph_map=map_osm, popup_attribute='name', node_labels=True, edge_width=20)

    # Add customized markers for nodes to view node IDs etc upon click
    for node, data in G.nodes(data=True):
        folium.Marker(location=[data['y'], data['x']], popup=f"Node: {node}").add_to(map_osm)

    # Display the folium map inline
    display(map_osm)
  # Function to visualize the shortest path on the map
def visualize_path_folium(G, shortest_path, location, source_node, target_nodes, distance):
    """
        G: Graph object representing the road network
        shortest_path:  A list of node IDs representing the shortest path between the source and target nodes
        location: location around which the map is centered
        source_node:  ID of the source node
        target_nodes: list of ID(s) of target nodes
        distance: distance (in meters) between the source and target nodes
    """

    # Get the center (latitude and longitude) coordinates of the location
    lat, lng = ox.geocode(location)

    # Create a folium map centered at the location
    map_center = [lat, lng]
    map_osm = folium.Map(location=map_center, zoom_start=12)

    # Add the road network graph to the folium map
    ox.plot_graph_folium(G, graph_map=map_osm, node_labels=True, edge_width=20)

    # Add markers for the source and destination nodes (source node is marked in green, destination node is marked in red)
    folium.Marker(location=(G.nodes[source_node]['y'], G.nodes[source_node]['x']), icon=folium.Icon(color='green'), popup=f'Source<br>Distance: {distance:.2f} meters').add_to(map_osm)


    for target_node in target_nodes:
      folium.Marker(location=(G.nodes[target_node]['y'], G.nodes[target_node]['x']), icon=folium.Icon(color='red'), popup='Destination').add_to(map_osm)

    gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

    # Get the coordinates of the shortest path
    shortest_path_coords = []
    for i in range(len(shortest_path)-1):
        edge = (shortest_path[i], shortest_path[i+1], 0)
        edge_coords = gdf_edges.loc[edge]['geometry']
        shortest_path_coords.extend([(point[1], point[0]) for point in edge_coords.coords])

    # Add the shortest path to the map as a PolyLine
    folium.PolyLine(locations=shortest_path_coords, color='blue', weight=5).add_to(map_osm)

    # Display the folium map inline
    display(map_osm)
loc = "..." #insert relevant details
dist = ...

G = get_road_network(loc, dist)

# Print nodes information
for node, data in G.nodes(data=True):
    print(f"Node {node}: Latitude - {data['y']}, Longitude - {data['x']}")

# Print edges information
for u, v, data in G.edges(data=True):
    print(f"Edge ({u}, {v}): Length - {data['length']}")

# heuristic functions
def euclidean_heuristic(node1, node2):

    x1, y1 = G.nodes[node1]['x'], G.nodes[node1]['y']
    x2, y2 = G.nodes[node2]['x'], G.nodes[node2]['y']
    
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def manhattan_heuristic(node1, node2):
    
    x1, y1 = G.nodes[node1]['x'], G.nodes[node1]['y']
    x2, y2 = G.nodes[node2]['x'], G.nodes[node2]['y']
    
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

def haversine_heuristic(node1, node2):

    lat1, lon1 = np.radians(G.nodes[node1]['y']), np.radians(G.nodes[node1]['x'])
    lat2, lon2 = np.radians(G.nodes[node2]['y']), np.radians(G.nodes[node2]['x'])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = 6371.0 * c
    # print("haversine",distance)
    return distance
