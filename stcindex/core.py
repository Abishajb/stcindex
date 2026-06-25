import networkx as nx

def stc_index(G, weight='weight'):
    """
    Calculate Spanning Tree Complexity Index using MST degree squares.
    
    STC(G) = (1 / (n-1)^2) * sum(deg_MST(v)^2 for all v)
    
    Parameters
    ----------
    G : NetworkX graph
        Undirected connected graph. If weighted, uses 'weight' attribute.
    weight : string, optional
        Edge attribute to use as weight for MST. Default 'weight'.
        
    Returns
    -------
    float
        Spanning Tree Complexity Index value
    
    """
    
    if not nx.is_connected(G):
        raise ValueError("Graph must be connected to compute MST")
    
    n = G.number_of_nodes()
    if n < 2:
        raise ValueError("Graph must have at least 2 nodes")

    # Get minimum spanning tree
    mst = nx.minimum_spanning_tree(G, weight=weight)
    
    # Sum of squared degrees in MST
    degree_squares_sum = sum(d**2 for _, d in mst.degree())
    
    # Apply formula: 1/(n-1)^2 * sum
    stc = degree_squares_sum / ((n - 1) ** 2)
    
    if n==2:
        return 2
    
    return float(stc)

calculate_stc = stc_index
spanning_tree_complexity = stc_index
def star_graph(n):
    """
    Create a star graph with n total nodes.
    
    Note: This differs from networkx.star_graph(), which uses n=number of leaves.
    Here n = total nodes in graph.
    
    Parameters
    ----------
    n : int
        Total number of nodes. Must be >= 2.
        
    Returns
    -------
    G : NetworkX Graph
        Star graph with 1 center and n-1 leaves.
        
    Examples
    --------
    >>> G = stcindex.star_graph(5)
    >>> G.number_of_nodes()
    5
    >>> stcindex.stc_index(G)
    1.25
    """
    if n < 2:
        raise ValueError("Star graph must have at least 2 nodes")
    return nx.star_graph(n-1)
        
       
def path_graph(n):
     """n=total nodes"""
     return nx.path_graph(n)
def cycle_graph(n):
     """n=total nodes"""
     if n<3:
      raise ValueError("Cycle graph needs atleast 3 nodes")
     return nx.cycle_graph(n)
def complete_graph(n):
     """n=total nodes"""
     return nx.complete_graph(n)
def wheel_graph(n):
     """n=total nodes"""
     if n<4:
      raise ValueError("Wheel graph needs atleast 4 nodes")
     return nx.wheel_graph(n)
def tree_graph(n, seed=None):
    return nx.random_tree(n,seed=seed)
def grid_graph(m,n):
    """m x n grid graph. Total nodes=m*n."""
    G=nx.grid_2d_graph(m,n)
    return nx.convert_node_labels_to_integers(G)
def ladder_graph(n):
    """2*n=total nodes"""
    return nx.ladder_graph(n)
def hypercube_graph(n):
     """2^n=total nodes"""
     return nx.hypercube_graph(n)

def complete_bipartite_graph(n1, n2):
    """Complete bipartite graph K_{n1,n2}. Total nodes = n1 + n2."""
    if n1 < 1 or n2 < 1:
        raise ValueError("Partitions must have at least 1 node each")
    return nx.complete_bipartite_graph(n1, n2)

def bistar_graph(n1, n2):
    """
    Bistar B_{n1,n2}: two star centers connected by an edge.
    Center1 has n1 leaves, Center2 has n2 leaves. 
    Total nodes = n1 + n2 + 2
    """
    if n1 < 0 or n2 < 0:
        raise ValueError("Leaf counts must be >= 0")
    # Build K_{1,n1} + K_{1,n2} then join centers
    G = nx.union(nx.star_graph(n1), nx.star_graph(n2), rename=('L-', 'R-'))
    G.add_edge('L-0', 'R-0')  # connect the two centers
    return nx.convert_node_labels_to_integers(G)

def barbell_graph(m1, m2):
    """
    Barbell graph: two complete graphs K_m1 connected by a path of m2 nodes.
    Total nodes = 2*m1 + m2
    """
    if m1 < 2:
        raise ValueError("Complete parts need at least 2 nodes")
    if m2 < 0:
        raise ValueError("Path length must be >= 0")
    return nx.barbell_graph(m1, m2)

def bipartite_graph(n1, n2, p=0.5, seed=None):
    """
    Random bipartite graph with partitions of size n1 and n2.
    Total nodes = n1 + n2.
    """
    if n1 < 1 or n2 < 1:
        raise ValueError("Partitions must have at least 1 node each")
    return nx.bipartite.random_graph(n1, n2, p, seed=seed)
def petersen_graph():
    """n=10 nodes"""
    return nx.petersen_graph()