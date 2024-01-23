import networkx as nx
import pandas as pd
import time

print("⏳ Reading csv ...")
# read data file
df = pd.read_csv("musae_git_edges.csv")

print("⏳ Converting dataframe to networkx graph ...")
# Convert to NX
G = nx.from_pandas_edgelist(df, source="id_1", target="id_2")
print("✅ Created graph object")

# Print information about the network
print(f"🧮 The graph has {len(G):,} nodes and {G.number_of_edges():,} edges.")

t1 = time.time()
nx.eigenvector_centrality(G)
print(f"✅ Calculating eigenvector_centrality took {(time.time() - t1):.2f} seconds.")

t2 = time.time()
nx.average_clustering(G)
print(f"✅ Calculating average_clustering took {(time.time() - t2):.2f} seconds.")

t3 = time.time()
nx.betweenness_centrality(G, k=100)
print(f"✅ Calculating betweenness_centrality took {(time.time() - t3):.2f} seconds.")
