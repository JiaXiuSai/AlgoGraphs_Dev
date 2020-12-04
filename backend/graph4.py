import networkx as nx

def Graph():
    G = nx.Graph()
    for i in range(1,10):
        G.add_node(i)

    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(1,4)
    G.add_edge(1,5)
    G.add_edge(2,6)
    G.add_edge(2,7)
    G.add_edge(3,8)
##    G.add_edge(7,9)
   
    G.add_edge(8,7)

    G.add_edge(7,9)

    
##    k = 5
##    
##    for i in range(1,2*k+1):
##        G.add_node(i)
##    
##    for i in range(1,k+1):
##        for j in range(1,k+1):
##            if i!=j:
##                G.add_edge(2*i-1,2*j)
##    
    G.add_nodes_from(G.nodes(), colour='never coloured')
    return G
