import osmnx as ox
import folium
from IPython.display import display

def visualize_road_network(G, location, distance):
    lat, lng = ox.geocode(location)
    map_center = [lat, lng]
    map_osm = folium.Map(location=map_center, zoom_start=12)
    ox.plot_graph_folium(G, graph_map=map_osm, popup_attribute='name', node_labels=True, edge_width=20)
    for node, data in G.nodes(data=True):
        folium.Marker(location=[data['y'], data['x']], popup=f"Node: {node}").add_to(map_osm)
    display(map_osm)

def visualize_path_folium(G, shortest_path, location, source_node, target_nodes, distance):
    lat, lng = ox.geocode(location)
    map_center = [lat, lng]
    map_osm = folium.Map(location=map_center, zoom_start=12)
    ox.plot_graph_folium(G, graph_map=map_osm, node_labels=True, edge_width=20)
    folium.Marker(location=(G.nodes[source_node]['y'], G.nodes[source_node]['x']), icon=folium.Icon(color='green'), popup=f'Source<br>Distance: {distance:.2f} meters').add_to(map_osm)
    for target_node in target_nodes:
        folium.Marker(location=(G.nodes[target_node]['y'], G.nodes[target_node]['x']), icon=folium.Icon(color='red'), popup='Destination').add_to(map_osm)
    gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
    shortest_path_coords = []
    for i in range(len(shortest_path)-1):
        edge = (shortest_path[i], shortest_path[i+1], 0)
        edge_coords = gdf_edges.loc[edge]['geometry']
        shortest_path_coords.extend([(point[1], point[0]) for point in edge_coords.coords])
    folium.PolyLine(locations=shortest_path_coords, color='blue', weight=5).add_to(map_osm)
    display(map_osm)
