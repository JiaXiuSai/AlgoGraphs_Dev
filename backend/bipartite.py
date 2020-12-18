import networkx as nx
import matplotlib.pyplot as plt
import random

def bipartite(numNodes):

    odds=[]
    evens=[]
    colours=[]

    for i in range(1,numNodes+1,2):
        odds.append(i)
        colours.append('red')
            
        
    for i in range(2,numNodes+1,2):
        evens.append(i)
        colours.append('blue')

    B = nx.Graph()
    B.add_nodes_from(odds, bipartite=0)
    B.add_nodes_from(evens, bipartite=1)
    for i in range(1,numNodes):
        B.add_edge(i,i+1)

    #just adds a few more edges on
    if numNodes>=3:
        for j in range(1,numNodes):
            x=random.uniform(0, 1)
            if x>0.6:
                y=random.randint(1, len(evens)-1)
                z=random.randint(1, len(odds)-1)
                if z!=y:
                    B.add_edge(odds[z],evens[y])

    lhs = nx.bipartite.sets(B)[0]
    positions = nx.bipartite_layout(B, lhs,scale=40)
    
    nx.draw_networkx_labels(B, pos=positions)
    nx.draw(B, pos=positions,node_color=colours)
    plt.savefig((str(numNodes)+"bipartite.png"), dpi=300)
    plt.show()




bipartite(10)
