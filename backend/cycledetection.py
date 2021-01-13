import networkx as nx
import matplotlib.pyplot as plt


def cycleDetection(G):
    x=[]        
    try:
        x=list(nx.find_cycle(G, orientation="original"))
    except:
        pass

    if(x):
        print((nx.find_cycle(G, orientation="ignore")))
        
        print(True)
    else:
        print(True)
    G.add_nodes_from(G.nodes(), colour='never coloured')

    for e in G.edges():
            print(e)
            G[e[0]][e[1]]['color'] = 'black'
            for i in x:
                if(((e[0]==i[0])and(e[1]==i[1]))or((e[1]==i[0])and(e[0]==i[1]))):
                    print(i[0],e[0],i[1],e[1])
                    G[e[0]][e[1]]['color'] = 'red'

    node_colour_list=[]

    #colour nodes that are in the cycle
    for e in G.nodes():
            print(e)
            coloured=False
            for i in x:
                if((e==i[0])):
                    node_colour_list.append('pink')
                    coloured=True
                    break
            if(coloured==False):
                node_colour_list.append('white')
                
                    
    
    positions = nx.spring_layout(G)
    edge_colour_list = [G[e[0]][e[1]]['color'] for e in G.edges()]
    nx.draw(G, pos=positions,node_color=node_colour_list,edge_color=edge_colour_list)
    nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(len(node_colour_list))+"cycledetection.png"), dpi=300)
    #plt.show()#wont need this reaslitically, but just for show


##multi cycle
adj=[[0,1,1,0,1],
     [1,0,0,1,1],
     [1,0,0,1,1],
     [0,1,1,0,1],
     [1,1,1,1,0]]

#no cycle
##adj=[[0,0,1,0],
##     [0,0,0,1],
##     [1,0,0,1],
##     [0,0,1,0]]

#cycle
##adj=[[0,1,1,0],
##     [1,0,0,1],
##     [1,0,0,1],
##     [0,1,1,0]]


#graph will be premade from another function - eg custom
#i have left it as 0 for starting node right now because this
#is not where the graph will be actually made
G = nx.Graph()

for i in range(0,len(adj)):
    G.add_node(i)

for i in range(0,len(adj)):
    for j in range(0,len(adj[i])):
        if(adj[i][j]==1):
            G.add_edge(i,j)

cycleDetection(G)
