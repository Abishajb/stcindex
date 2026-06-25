# stcindex

Spanning Tree Complexity Index for graphs.

## Install
```bash
pip install stcindex
```
## Quick start
```python
import stcindex
import networkx as nx

G = nx.star_graph(4)
print(stcindex.stc_index(G))  
print(stcindex.summary(G))
```
## Citation
  Manuscript in preparation. Code available at: https://github.com/Abishajb/stcindex
