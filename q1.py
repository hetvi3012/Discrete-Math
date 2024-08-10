#importing all the necessary libraries
import pandas as pd
import networkx as nx
import random
import matplotlib.pyplot as plt


# Step 1: Read the CSV file
data = pd.read_csv('modified_impression_network.csv')

# Step 2: Create a directed graph
G = nx.DiGraph()
for index, row in data.iterrows():
    source = row.iloc[0]  # Assuming the first column is the source node
    targets = row.iloc[1:].dropna().tolist()  # Assuming the rest are target nodes
    G.add_node(source)  # Add source node if not already added
    for target in targets:
        G.add_edge(source, target)


# Step 3: Implement random walk with teleportation
def random_walk_with_teleportation(graph, num_steps=100000, teleport_prob=0.15):      #fixing teleportation probability to 15%
    node_visits = {node: 0 for node in graph.nodes()}                                 
    current_node = random.choice(list(graph.nodes()))
    for _ in range(num_steps):                #itrating number of step times
        if random.random() < teleport_prob:
            current_node = random.choice(list(graph.nodes()))
        else:
            neighbors = list(graph.neighbors(current_node))
            if neighbors:
                current_node = random.choice(neighbors)
            else:
                current_node = random.choice(list(graph.nodes()))
        node_visits[current_node] += 1
    return node_visits

node_visits = random_walk_with_teleportation(G)                                             

top_leaders_rw = sorted(node_visits.items(), key=lambda x: x[1], reverse=True)[:1]
print("Top Leader (Random Walk with Teleportation):")
for leader, visits in top_leaders_rw:
    print(f"Node: {leader}, Visits: {visits}")



# Show the graph
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True)
plt.show()
