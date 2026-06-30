import stcindex
import networkx as nx

G1 = nx.Graph()
G1.add_edges_from([(1,2),(2,6),(2,7),(3,5),(3,6),(4,5),(4,7),(5,6),(7,8)])
print(f"G1: n={G1.number_of_nodes()}, STC={stcindex.stc_index(G1):.6f}")

G2 = nx.Graph() 
G2.add_edges_from([(1,2),(2,5),(2,8),(3,7),(3,8), 
                   (4,6),(4,8),(5,6),(7,8)]) 
print(f"G2: n={G2.number_of_nodes()}, STC={stcindex.stc_index(G2):.6f}")