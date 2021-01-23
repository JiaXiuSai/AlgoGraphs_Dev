import networkx as nx
import matplotlib.pyplot as plt

# prints all not yet visited vertices reachable from s 
def dfs(adjlist,G,positions):
    #keeps track of which index of colourList we are allowed to colour the node in
    colourCount=0
    colourList=['orange','blue','yellow','red','purple','grey','pink','green','grey']

    #initialise an all white list for the nodes that have not yet been coloured
    #will get coloured as we go on
    vColour=['#ffffff']*len(adjlist)

    #draws first stage and saves (non coloured graph)
    nx.draw(G, pos=positions,node_color=vColour)
    #nx.draw_networkx_labels(G, pos=positions)
    order=0
    plt.savefig((str(order)+"dfs.png"), dpi=300)

    #adds orange to first node 0 (which is node 1 on networkx graph)
    vColour[0]=colourList[colourCount]
    colourCount+=1

    #draws first COLOURED stage and saves
    order=1
    nx.draw(G, pos=positions,node_color=vColour)
    #nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(order)+"dfs.png"), dpi=300)

    order=2

    
    visited = [False] * len(adjlist)
    s=0
    # Create a stack for DFS 
    stack = []

    # Push the current source node. 
    stack.append(s) 

    while (len(stack)): 
        # Pop a vertex from stack and print it 
        s = stack[-1] 
        stack.pop()

        # Stack may contain same vertex twice. So 
        # we need to print the popped item only 
        # if it is not visited. 
        if (not visited[s]): 
            print(s,'\n')
            vColour[s]=colourList[colourCount]
            nx.draw(G, pos=positions,node_color=vColour)
            #nx.draw_networkx_labels(G, pos=positions)
            plt.savefig((str(order)+"dfs.png"), dpi=300)
            order+=1
            visited[s] = True
        print(vColour)
        # Get all adjacent vertices of the popped vertex s 
        # If a adjacent has not been visited, then push it 
        # to the stack. 
        for node in adjlist[s]: 
            if (not visited[node]): 
                stack.append(node)

def petersen():
    plt.clf()
    Graph = nx.petersen_graph()
    
    nx.draw_shell(Graph, nlist=[range(5, 10), range(5)],  font_weight='bold',node_color='grey')
    positions = nx.shell_layout(Graph, nlist=[range(5, 10), range(5)])
    nx.draw_networkx_labels(Graph, pos=positions,labels={n: n+1 for n in Graph})
    #print(pos)
    plt.savefig(("petersen.png"), dpi=800)
    #plt.show()
    adjlist=[]
    x = nx.convert.to_dict_of_lists(Graph)
    for i in x.values():
        adjlist.append(i)
  
    return adjlist,Graph,positions

def complete(numNodes):
    plt.clf()
    G= nx.Graph()
    
    if numNodes == 1:
        G.add_node(0)
    elif numNodes > 1:
        G.add_node(0)
        for i in range(1,numNodes):
            G.add_node(i)

            for j in range(0,i):
                G.add_edge(j,i)

    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    #nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"complete.png"), dpi=300)
    #plt.show()
    adjlist=[]
    x = nx.convert.to_dict_of_lists(G)
    for i in x.values():
        adjlist.append(i)
  
    return adjlist,G,positions
