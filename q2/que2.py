import numpy as np
import pandas as pd
import networkx as nx

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

nodes = list(G.nodes())     #preparing list of nodes

def predict_missing_edges(adj_matrix):      #algorithm to find missing links
    predicted_weights = np.zeros_like(adj_matrix, dtype=float)  
    missing_links = []  # Initialize array for predicted weights

    for i in range(adj_matrix.shape[0]):#itrating through whole list
        for j in range(adj_matrix.shape[1]):
            if adj_matrix[i, j] == 0:            #checking if cell is 0 or not
                predicted_edge_weight = predict_missing_edge(adj_matrix, i, j)       #calling predict function
                if predicted_edge_weight > 0.5:          #using threshold
                    missing_links.append((nodes[i], nodes[j]))            #appending node to missing link
                    # Add edge if predicted weight is greater than 0.5
                    G.add_edge(i, j)                      #if missing link found add an edge in the graph
                predicted_weights[i, j] = predicted_edge_weight
            else:
                predicted_weights[i, j] = adj_matrix[i, j]

    return predicted_weights, missing_links


def predict_missing_edge(adj_matrix, missing_edge_row, missing_edge_col):
    # Remove the corresponding row and column
    reduced_matrix = np.delete(np.delete(adj_matrix, missing_edge_row, axis=0), missing_edge_col, axis=1)

    # Extract the removed column
    removed_column = adj_matrix[:, missing_edge_col]
    removed_column = np.delete(removed_column, missing_edge_row, axis=0)

    # Append a column of ones to the reduced matrix
    reduced_matrix_with_ones = np.column_stack((reduced_matrix, np.ones(reduced_matrix.shape[0])))

    # Perform least squares approximation
    coefficients = np.linalg.lstsq(reduced_matrix_with_ones, removed_column, rcond=None)[0]

    # Predict the missing edge weight
    predicted_edge_weight = np.dot((adj_matrix[missing_edge_row, :]), coefficients)

    return predicted_edge_weight

# Example adjacency matrix
adjacency_matrix = nx.adjacency_matrix(G).todense()

predicted_weights, missing_links = predict_missing_edges(adjacency_matrix)
pagerank_scores = nx.pagerank(G)

# Find the top 10 leaders using PageRank
top_leaders_pagerank = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:1]
print("\nTop 10 Leaders (PageRank):")
for leader, score in top_leaders_pagerank:
    print(f"Node: {leader}, PageRank Score: {score}")

num_missing_links = len(missing_links)
print(f"\nNumber of Missing Links: {num_missing_links}")

# Print missing links
print("\nMissing Links:")
for link in missing_links:
    print(f"Missing Link: {link}")

