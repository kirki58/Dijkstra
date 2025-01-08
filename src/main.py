import graph as g

# Create a graph handler with specified graph in graph.json
graph_handler = g.GraphHandler("graph1")

# Draw plain graph
# graph_handler.draw_graph()

# get the shortest distances and previous nodes from the specified start node
distances, previous_nodes = graph_handler.dijkstra("A")

# reconstruct the shortest path from start to end
# shortest_path = graph_handler.reconstruct_shortest_path(previous_nodes, "F")

# draw shortest path
# graph_handler.draw_shortest_path(shortest_path)

# get dijkstra table
# table = graph_handler.get_dijkstra_table(distances, previous_nodes)

# draw dijkstra table
# graph_handler.draw_dijkstra_table(distances, previous_nodes)