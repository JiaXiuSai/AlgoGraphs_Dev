import networkx as nx
import matplotlib.pyplot as plt
import random

#will need to check if the user has chosen to run an alg on chosen graph, since
#this may slightly alter how it works ie saving figures, may need to add
#an additional parameter that is passed from frontend if the user has selected
#to run a search algorithm, if they have selected, then draw
#or have own seperate drawing function? may not work for search algs

# was thiking about sep drawing func just for the graphs that could be run if the
#search algs dont execute but will be an issue for some creation algs like
#hypercube, bipartite
"""
all these added below

1. cycle
2. star
3. tree
4. path
5. complete
6. bipartite
7. hypercubes
8. petersen
9. custom


need adding/doing
1. bfs
2. dfs
3. dijkstra
4. kruskal
5. cycle

!!!!!!!!!!temporal!!!!!!!!!

"""


#ADD POSITIONS AS PARAMETERS AND RETURNS SO THE GRAPH LOOKS CONSISTENT

def cycle(numNodes):

    G= nx.Graph()
    

    if numNodes == 1:
        G.add_node(1)

    elif numNodes > 1:
        G.add_node(1)
        for i in range(1,numNodes):
            G.add_node(i)
            G.add_edge(i,i+1)
    G.add_edge(1,numNodes)
    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    nx.draw_networkx_labels(G, pos=positions)
    
    plt.savefig((str(numNodes)+"path.png"), dpi=300)
    plt.show()

    return G

def star(numNodes):

    G= nx.Graph()
    

    if numNodes == 1:
        G.add_node(1)

    elif numNodes > 1:
        G.add_node(1)
        for i in range(2,numNodes+1):
            G.add_node(i)
            G.add_edge(1,i)

    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions)
    
    plt.savefig((str(numNodes)+"star.png"), dpi=300)
    plt.show()

    return G

def tree(numNodes):

    G= nx.Graph()
    
    if numNodes == 1:
        G4.add_node(1)

    elif numNodes > 1:
        G.add_node(1)
        for i in range(2,numNodes+1):
            G.add_node(i)

            prob = random.uniform(0,1)

            if prob>0.5:
                randy = random.randint(1,i-1)
                G.add_edge(randy,i)

            else:
                G.add_edge(i,i-1)
        
    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(numNodes)+"tree.png"), dpi=300)
    plt.show()

    return G

def path(numNodes):

    G= nx.Graph()
    

    if numNodes == 1:
        G.add_node(1)

    elif numNodes > 1:
        G.add_node(1)
        for i in range(1,numNodes):
            G.add_node(i)
            G.add_edge(i,i+1)

    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    nx.draw_networkx_labels(G, pos=positions)
    
    plt.savefig((str(numNodes)+"path.png"), dpi=300)
    plt.show()

    return G


def complete(numNodes):

    G= nx.Graph()
    
    if numNodes == 1:
        G.add_node(1)

    elif numNodes > 1:
        G.add_node(1)
        for i in range(2,numNodes+1):
            G.add_node(i)

            for j in range(1,i):
                G.add_edge(j,i)

        
    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(numNodes)+"complete.png"), dpi=300)
    plt.show()

    return G


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

    return B


def hypercube(n):

    if n==0:
        x= nx.Graph()
        x.add_node(0)
        
    else:
        x=nx.generators.lattice.hypercube_graph(n)
    positions = nx.spring_layout(x, scale=0.8)
    nx.draw(x, pos=positions,node_color='grey', width=1, edge_color="skyblue", style="solid")
    nx.draw_networkx_labels(x, pos=positions, font_size=10)
    #plt.figure(figsize=(10.0,10.0))

    #fits everything in
    plt.margins(0.15)
    plt.savefig((str(n)+"hypercube.png"), dpi=800)#,figsize=(10.0,10.0))
    plt.show()
    return x

def petersen():
    Graph = nx.petersen_graph()
    nx.draw_shell(Graph, nlist=[range(5, 10), range(5)],  font_weight='bold',node_color='grey')

    plt.savefig("petersen.png"), dpi=800)
    plt.show()
    return Graph

def custom(adj):

    G= nx.Graph()
    

    for i in range(0,len(adj)):
        G.add_node(i)

    for i in range(0,len(adj)):
        for j in range(0,len(adj[i])):
            if(adj[i][j]==1):
                G.add_edge(i,j)

    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions)
    
    plt.savefig((str(len(adj))+"custom.png"), dpi=300)
    plt.show()

    return G
