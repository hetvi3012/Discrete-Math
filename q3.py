import networkx as nx
import matplotlib.pyplot as plt
import csv

# Sample social network data (replace with your actual data)
impressions = {}
with open("modified_impression_network.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        node = row[0]
        if node not in impressions:
            impressions[node] = []
        for i in row[1:]:
            if i:
                impressions[node].append(i)

# Create directed graph
G = nx.DiGraph()

# Add edges based on impressions
for person, impressed_by in impressions.items():
    for impressed in impressed_by:
        G.add_edge(impressed, person)

# Calculate node betweenness centrality manually
def calculate_betweenness_centrality(graph):
    betweenness_centrality = {}
    for node in graph.nodes():
        betweenness = 0
        for source in graph.nodes():
            for target in graph.nodes():
                if source != target and source != node and target != node:
                    try:
                        num_shortest_paths = len(list(nx.all_shortest_paths(graph, source=source, target=target)))
                        num_shortest_paths_through_node = len([path for path in nx.all_shortest_paths(graph, source=source, target=target) if node not in path])
                        if num_shortest_paths != 0:
                            betweenness += num_shortest_paths_through_node / num_shortest_paths
                    except nx.NetworkXNoPath:
                        continue
        betweenness_centrality[node] = betweenness
    return betweenness_centrality

betweenness_centrality = calculate_betweenness_centrality(G)

# Sort nodes by betweenness centrality
sorted_nodes = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)

# Print top 5 key intermediaries
print("Top 5 Key Intermediaries:")
for node, centrality_score in sorted_nodes[:5]:
    print(f"{node}: {centrality_score}")

# Visualize the network
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=300, alpha=0.5)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
plt.title("Social Network with Key Intermediaries Highlighted")
plt.axis("off")
plt.show()