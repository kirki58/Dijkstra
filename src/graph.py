import networkx as nx
import matplotlib.pyplot as plt
import json
from config import graphs_path
import heapq

class GraphHandler:
    def __init__(self, graphName):
        self.graph = nx.Graph()
        self.edges = []
        # Load graph from JSON file
        with open(graphs_path) as file:
            data = json.load(file)
            
            try:
                requestedGraph = data[graphName]
            except KeyError:
                print(f"{graphName} not found in graphs.json")
                return
            
            try:
                self.edges = requestedGraph["Edges"]
            except KeyError:
                print(f"Edges not found in graph, Make sure {graphName} in graphs.json has a valid structure")
                return

            for edge in self.edges:
                self.graph.add_edge(edge[0], edge[1], weight=edge[2]),

            # positions for all nodes "seed" is used to make sure the layout is the same every time the graph is drawn "7" doesnt have a special meaning its just a random number
            self.pos = nx.spring_layout(self.graph, seed=7)


    def draw_graph(self, node_size = 700, edge_width = 6, label_font_size = 20):
        nx.draw_networkx_nodes(self.graph, self.pos, node_size=node_size) # Draw nodes
        nx.draw_networkx_edges(self.graph, self.pos, edgelist=self.edges, width=edge_width) # Draw edges
        nx.draw_networkx_labels(self.graph, self.pos, font_size=label_font_size, font_family="sans-serif") # Draw node labels

        # Draw edge labels
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels)

        # Plot the graph
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def dijkstra(self, start_node):
        # Self-Implemented Dijkstra Algorithm (although networkx has an internal one)

        # Distance dictionary: maps node to its shortest distance from the start node
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start_node] = 0 # Each node initially has infinite distance to start_node except for the start_node itself whose distance is set to 0

        # Previous node dictionary: map node to it's previous node in it's shortest path from start_node to itself.
        previous_nodes = {node: None for node in self.graph.nodes}
        
        # min-heap priority queue to hold current shortest path distance from start_node during processing (as tuples)

        pq = [(0,start_node)] # The initial entry to the queue is (0, "start_node") as distance from start_node to start_node is already determined and is 0
        
        # Loop ends when queue is empty meaning all nodes are visited.
        while(pq):
            # Get node with smallest distance to start_node to process it and it's neighbors
            current_distance, current_node = heapq.heappop(pq) # Pops the item with smallest distance (most prioritized) from the queue at start this would be (0, start_node)

            # Skip if a shorter distance is already calculated for current_node
            if current_distance > distances[current_node]:
                continue
            
            # Explore neigbor nodes of the current_node
            neighbors = list(self.graph.neighbors(current_node))
            for neighbor in neighbors:
                weight = self.graph.get_edge_data(current_node, neighbor)["weight"]
                distance = current_distance + weight

                # If a shorter path is found update the distance and previous node
                if(distance < distances[neighbor]):
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, previous_nodes

    def reconstruct_shortest_path(self, previous_nodes, end):
        path = []
        current_node = end

        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        
        path.reverse() # reverse the path to get from start to end

        return path
    
    def get_dijkstra_table(self, distances, previous_nodes):
        table = []
        for node in self.graph.nodes:
            table.append([node, distances[node], previous_nodes[node]])

        return table
    
    def draw_dijkstra_table(self, distances, previous_nodes):
        # Create a figure and axis
        fig, ax = plt.subplots()

        # Hide the axes
        ax.xaxis.set_visible(False) 
        ax.yaxis.set_visible(False)
        ax.set_frame_on(False)

        # Create the table
        table_data = [["Node", "Distance", "Previous Node"]]
        for node in distances:
            table_data.append([node, distances[node], previous_nodes[node]])

        table_plot = ax.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center')

        # Adjust layout
        table_plot.auto_set_font_size(False)
        table_plot.set_fontsize(10)
        table_plot.scale(1.2, 1.2)

        # Show the plot
        plt.show()
    
    def draw_shortest_path(self, shortest_path ,node_size = 700, edge_width = 6, label_font_size = 20):
        start_node = shortest_path[0]
        end_node = shortest_path[-1]

        node_colors = []
        for node in self.graph.nodes:
            if node == start_node:
                node_colors.append("green")
            elif node == end_node:
                node_colors.append("red")
            else:
                node_colors.append("blue")
        
        nx.draw_networkx_nodes(self.graph, self.pos, node_size=node_size, node_color=node_colors) # Draw nodes

        edge_colors = []
        for edge in self.edges:
            if edge[0] in shortest_path and edge[1] in shortest_path:
                edge_colors.append("red")
            else:
                edge_colors.append("black")
        
        nx.draw_networkx_edges(self.graph, self.pos, edgelist=self.edges, width=edge_width, edge_color=edge_colors) # Draw edges

        nx.draw_networkx_labels(self.graph, self.pos, font_size=label_font_size, font_family="sans-serif")

        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels)

        # Plot the graph
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()