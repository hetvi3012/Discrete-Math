"""
# Social Network Analysis and Link Prediction

## Overview

This project focuses on analyzing and optimizing a social network using algorithms like Random Walk with Teleportation, PageRank, and Betweenness Centrality. The project also involves predicting missing links in the network using the method of least squares. The aim is to identify key leaders, predict potential connections, and optimize information propagation within a social network graph.

## Tech Stack

- **Python**
- **NetworkX**: For graph creation and analysis.
- **Pandas**: For data manipulation and processing.
- **NumPy**: For numerical operations and implementing the least squares method.

## Project Structure

1. **Random Walk with Teleportation**
   - **Objective:** Identify key leaders within an impression network.
   - **Algorithm:** 
     - Start at a random node in the graph.
     - With a specified probability, teleport to a random node; otherwise, move to a random neighboring node.
     - Track the number of visits to each node.
   - **Outcome:** Identification of nodes that are frequently visited, indicating their importance as leaders.

2. **Link Prediction Using Least Squares**
   - **Objective:** Predict missing links in the social network graph.
   - **Algorithm:** 
     - Construct an adjacency matrix from the graph.
     - For each missing link (represented as a `0` in the matrix), predict its likelihood using the method of least squares.
     - Reconstruct the graph by adding links that exceed a certain prediction threshold.
   - **Outcome:** Enhanced network connectivity by identifying and adding potential missing links.

3. **Optimization of Information Propagation**
   - **Objective:** Optimize how information spreads through the network of influencers.
   - **Algorithm:** 
     - Calculate Betweenness Centrality for each node, identifying nodes that act as critical intermediaries in the network.
     - Use these nodes to optimize the flow of information.
   - **Outcome:** Identification of key influencers who can significantly impact information dissemination.

## Implementation Details

### Random Walk with Teleportation

- **Step 1:** Initialize the random walk by selecting a random starting node.
- **Step 2:** At each step, either teleport to a random node with probability `α` or move to a random neighbor.
- **Step 3:** Track the frequency of visits to each node.
- **Step 4:** Nodes with the highest visit frequency are considered key leaders.

### Link Prediction Using Least Squares

- **Step 1:** Create an adjacency matrix representing the social network.
- **Step 2:** For each cell with a value of `0`, remove the corresponding row and column.
- **Step 3:** Perform a least squares regression to predict the missing link.
- **Step 4:** If the predicted value exceeds a threshold, add the link to the graph.

### Betweenness Centrality Calculation

- **Step 1:** Construct a directed graph using NetworkX.
- **Step 2:** Calculate Betweenness Centrality for each node.
- **Step 3:** Identify nodes with the highest centrality scores as key influencers.
- **Step 4:** Utilize these nodes to enhance information propagation strategies.

## Results

- **Leaders Identification:** The random walk algorithm successfully identified key nodes within the impression network.
- **Link Prediction:** The least squares method effectively predicted and filled missing links, improving the network's structure.
- **Influencer Analysis:** Betweenness centrality pinpointed critical influencers, optimizing the spread of information.

## How to Run

1. Clone this repository.
2. Install the necessary Python packages using `pip install -r requirements.txt`.
3. Run the Python scripts to execute the different parts of the project:
   - `random_walk.py` for Random Walk with Teleportation.
   - `link_prediction.py` for predicting missing links.
   - `betweenness_centrality.py` for optimizing information propagation.

## Conclusion

This project demonstrates the application of graph theory and network analysis to social networks. By identifying key leaders, predicting missing links, and optimizing information propagation, the project provides valuable insights into the structure and dynamics of social networks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""
