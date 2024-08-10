# Visualize the network
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=300, alpha=0.5)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
plt.title("Social Network with Key Intermediaries Highlighted")
plt.axis("off")
plt.show()