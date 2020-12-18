import networkx as nx
import matplotlib.pyplot as plt
import random
def tree(numNodes):

    G4= nx.Graph()
    
    if numNodes == 1:
        G4.add_node(1)

    elif numNodes > 1:
        G4.add_node(1)
        for i in range(2,numNodes+1):
            G4.add_node(i)

            prob = random.uniform(0,1)

            if prob>0.5:
                randy = random.randint(1,i-1)
                G4.add_edge(randy,i)

            else:
                G4.add_edge(i,i-1)
        
    G4.add_nodes_from(G4.nodes(), colour='never coloured')
    positions = nx.spring_layout(G4)
    nx.draw(G4, pos=positions,node_color='grey')
    nx.draw_networkx_labels(G4, pos=positions)
    plt.savefig((str(numNodes)+"tree.png"), dpi=300)
    plt.show()


tree(19)
tree(10)
tree(10)
tree(10)
tree(12)
tree(16)
tree(10)
tree(10)
tree(10)
tree(20)
tree(22)
tree(16)
