import pandas as pd
import networkx as nx


data = pd.read_csv('modified_impression_network.csv')

# Step 2: Create a directed graph
G = nx.DiGraph()
for index, row in data.iterrows():
    source = row.iloc[0]  # Assuming the first column is the source node
    targets = row.iloc[1:].dropna().tolist()  # Assuming the rest are target nodes
    G.add_node(source)  # Add source node if not already added
    for target in targets:
        G.add_edge(source, target)
 
# Calculate node betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Sort nodes by betweenness centrality
sorted_nodes = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)

# Print top 5 key intermediaries
print("Top 5 Key Intermediaries:")
for node, centrality_score in sorted_nodes[:5]:
    print(f"{node}: {centrality_score}")