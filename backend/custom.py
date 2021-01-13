import networkx as nx
import matplotlib.pyplot as plt


def custom(adj):

    G4= nx.Graph()
    

    for i in range(0,len(adj)):
        G4.add_node(i)

    for i in range(0,len(adj)):
        for j in range(0,len(adj[i])):
            if(adj[i][j]==1):
                G4.add_edge(i,j)

    G4.add_nodes_from(G4.nodes(), colour='never coloured')
    positions = nx.spring_layout(G4)
    nx.draw(G4, pos=positions,node_color='white')
    nx.draw_networkx_labels(G4, pos=positions)
    
    plt.savefig((str(len(adj))+"custom.png"), dpi=300)
    plt.show()

#adj=[[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]

    
adj=[[0,1,1,0,1],
     [1,0,0,1,1],
     [1,0,0,1,1],
     [0,1,1,0,1],
     [1,1,1,1,0]]

custom(adj)



