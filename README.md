# Set up your virtual environment (`venv`)

**Linux/MacOS**
```bash
python3 -m venv venv  # Create the virtual environment
source venv/bin/activate  # Activate virtual environment
pip install -r requirements.txt  # Install dependencies
python3 src/main.py # Run the application
```

**Windows**
```bash
python -m venv venv  # Create the virtual environment
venv\Scripts\activate # Activate virtual environment
pip install -r requirements.txt  # Install dependencies
python src/main.py # Run the application
```

# Using It

All test case graphs are in `graphs.json` Add your own graph if you desire, otherwise you can use one of the 5 default graphs by navigating to `main.py` and changing the parameter `graph1`

```python
graph_handler = g.GraphHandler("your-json-graph-name-here")
```

Then uncomment the related operations you want to perform in `main.py`. Note that some of the functions need to be executed subsequently in order for them to work.

** Example: Draw the shortest path between node "A" and "F" in graph1: **
`main.py`:

```python
import graph as g

# Create a graph handler with specified graph in graph.json
graph_handler = g.GraphHandler("graph1")

# Draw plain graph
# graph_handler.draw_graph()

# get the shortest distances and previous nodes from the specified start node
distances, previous_nodes = graph_handler.dijkstra("A")

# reconstruct the shortest path from start to end
shortest_path = graph_handler.reconstruct_shortest_path(previous_nodes, "F")

# draw shortest path
graph_handler.draw_shortest_path(shortest_path)

# get dijkstra table
# table = graph_handler.get_dijkstra_table(distances, previous_nodes)

# draw dijkstra table
# graph_handler.draw_dijkstra_table(distances, previous_nodes)
```