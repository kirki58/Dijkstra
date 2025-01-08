import graph as g

graphHandler = g.GraphHandler("graph1")

distances, previous_nodes = graphHandler.dijkstra("A")

shortest_path = graphHandler.reconstruct_shortest_path(previous_nodes, "F")
print(shortest_path)

graphHandler.draw_shortest_path(shortest_path)


