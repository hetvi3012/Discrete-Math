import networkx as nx
import random

def add_edges(G, p):
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r = random.random()
                if r<=p:
                    G.add_edge(i,j)
                else:
                    continue
    return G

def initialize_points(G):
    points = [100 for i in range(G.number_of_nodes())]
    return points

def distribute_points(G,points):
    prev_points = points
    new_points = [0 for i in range(G.number_of_nodes())]

    for i in G.nodes():
        out = G.out_edges(i)
        if len(out) == 0:
            new_points[i]+=prev_points[i]
        else:
            share = prev_points[i]/len(out)



def main():
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G= add_edges(G,0.3)
    points = initialize_points(G)