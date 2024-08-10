import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def walk(n, p):
    start = random.randint(0, n - 1)
    G = nx.erdos_renyi_graph(n, p)
    S = set([])
    v = start
    count = 0
    while len(S) < n:
        Nbr = list(nx.neighbors(G, v))
        if not Nbr:  # Check if Nbr is empty
            print("No neighbors for node", v)
            break
        v = random.choice(Nbr)
        S.add(v)
        count += 1
    return count

l = []
for i in range(20, 300):
    z = []
    for j in range(10):
        z.append(walk(i, 0.3))
    l.append(np.average(z))
    print(i, "--->", np.average(z))
plt.plot(l)
plt.show()
