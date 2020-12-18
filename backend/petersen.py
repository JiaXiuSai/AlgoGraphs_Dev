
import networkx as nx
import matplotlib.pyplot as plt

Graph = nx.petersen_graph()
nx.draw_shell(Graph, nlist=[range(5, 10), range(5)],  font_weight='bold',node_color='grey')

plt.savefig("petersen.png"), dpi=800)
plt.show()
