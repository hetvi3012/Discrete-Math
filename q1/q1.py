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
    node_visits = {node: 0 for node in graph.nodes()}                                 #creating dictionary assigning 0to all
    current_node = random.choice(list(graph.nodes()))
    for _ in range(num_steps):                #itrating number of step times
        if random.random() < teleport_prob:           #by random.random checking probability and checking weather to teleport or not
            current_node = random.choice(list(graph.nodes()))
        else:
            neighbors = list(graph.neighbors(current_node))
            if neighbors:
                current_node = random.choice(neighbors)
            else:
                current_node = random.choice(list(graph.nodes()))
        node_visits[current_node] += 1                    #increasing count of current node visit by 1
    return node_visits

node_visits = random_walk_with_teleportation(G)                                             #calling the function
top_leaders_rw = sorted(node_visits.items(), key=lambda x: x[1], reverse=True)[:1]      #reversing the list to get the leader
print("Top Leader (Random Walk with Teleportation):")           
for leader, visits in top_leaders_rw:                          #printing the leader
    print(f"Node: {leader}, Visits: {visits}")



#showing the graph of the network
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True)
plt.show()
