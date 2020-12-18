import networkx as nx
import matplotlib.pyplot as plt
import random
def complete(numNodes):

    G4= nx.Graph()
    
    if numNodes == 1:
        G4.add_node(1)

    elif numNodes > 1:
        G4.add_node(1)
        for i in range(2,numNodes+1):
            G4.add_node(i)

            for j in range(1,i):
                G4.add_edge(j,i)

        
    G4.add_nodes_from(G4.nodes(), colour='never coloured')
    positions = nx.spring_layout(G4)
    nx.draw(G4, pos=positions,node_color='grey')
    nx.draw_networkx_labels(G4, pos=positions)
    plt.savefig((str(numNodes)+"complete.png"), dpi=300)
    plt.show()


complete(3)
complete(4)
