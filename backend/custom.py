import networkx as nx
import matplotlib.pyplot as plt


def custom(adjlist):

    G4= nx.Graph()
    

    for i in range(0,len(adjlist)):
        G4.add_node(i)

    for i in range(0,len(adjlist)):
        for j in range(0,len(adjlist[i])):
            if(adjlist[i][j]==1):
                G4.add_edge(i,j)

    G4.add_nodes_from(G4.nodes(), colour='never coloured')
    positions = nx.spring_layout(G4)
    nx.draw(G4, pos=positions,node_color='white')
    nx.draw_networkx_labels(G4, pos=positions)
    
    plt.savefig((str(len(adjlist))+"custom.png"), dpi=300)
    plt.show()

#adjlist=[[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
adjlist=[[0,1,1,0,1],[1,0,0,1,1],[1,0,0,1,1],[0,1,1,0,1],[1,1,1,1,0]]
custom(adjlist)
