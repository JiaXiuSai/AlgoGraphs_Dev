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


##fix hypercube, there is something up wilth the graph when building the
#hypercube because [0,1,2] it ignoes the zero

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
    plt.clf()
    G= nx.Graph()
    

    if numNodes == 1:
        G.add_node(0)

    elif numNodes > 1:
        G.add_node(0)
        for i in range(0,numNodes-1):
            G.add_node(i)
            G.add_edge(i,i+1)
    G.add_edge(0,numNodes-1)
    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    #nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"cycle.png"), dpi=300)
    #plt.show()
    adjlist=[]
    x = nx.convert.to_dict_of_lists(G)
    for i in x.values():
        adjlist.append(i)
    
    return adjlist,G,positions

def star(numNodes):
    plt.clf()
    G= nx.Graph()
    

    if numNodes == 1:
        G.add_node(0)

    elif numNodes > 1:
        G.add_node(0)
        for i in range(1,numNodes):
            G.add_node(i)
            G.add_edge(0,i)

    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='white')
    #nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    
    plt.savefig((str(numNodes)+"star.png"), dpi=300)
    #plt.show()

    adjlist=[]
    x = nx.convert.to_dict_of_lists(G)
    for i in x.values():
        adjlist.append(i)
    
    return adjlist,G,positions


def tree(numNodes):
    plt.clf()
    G= nx.Graph()
    
    if numNodes == 1:
        G4.add_node(0)

    elif numNodes > 1:
        G.add_node(0)
        for i in range(1,numNodes):
            G.add_node(i)

            prob = random.uniform(0,1)

            if prob>0.5:
                randy = random.randint(0,i-1)
                G.add_edge(randy,i)

            else:
                G.add_edge(i,i-1)
        
    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    #nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(numNodes)+"tree.png"), dpi=300)
    #plt.show()
    adjlist=[]
    x = nx.convert.to_dict_of_lists(G)
    for i in x.values():
        adjlist.append(i)
    
    return adjlist,G,positions

def path(numNodes):
    plt.clf()
    G= nx.Graph()
    if numNodes == 1:
        G.add_node(0)

    elif numNodes > 1:
        G.add_node(0)
        for i in range(0,numNodes-1):
            G.add_node(i)
            G.add_edge(i,i+1)

    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='grey')
    #nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"path.png"), dpi=300)
    #plt.show()
    #print(
    adjlist=[]
    x = nx.convert.to_dict_of_lists(G)
    for i in x.values():
        adjlist.append(i)
    return adjlist,G,positions


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


def bipartite(numNodes):
    plt.clf()
    odds=[]
    evens=[]
    colours=[]
    B = nx.Graph()
    for i in range(0,numNodes,2):
        print(i)
        evens.append(i)
        B.add_node(i)
        colours.append('red')
        odds.append(i+1)
        B.add_node(i+1)
        colours.append('blue')

    for i in range(0,numNodes-1):
        B.add_edge(i,i+1)

    #just adds a few more edges on
    if numNodes>3:
        for j in range(0,numNodes-1):
            x=random.uniform(0, 1)
            if x>0.6:
                y=random.randint(0, len(evens)-2)
                z=random.randint(0, len(odds)-2)
                if z!=y:
                    B.add_edge(odds[z],evens[y])

    lhs = nx.bipartite.sets(B)[0]
    positions = nx.bipartite_layout(B, lhs,scale=40)
    #positions = nx.spring_layout(B,scale=40)
    nx.draw_networkx_labels(B, pos=positions,labels={n: n+1 for n in B})
    #nx.draw_networkx_labels(B, pos=positions)
    nx.draw(B, pos=positions,node_color=colours)
    #nx.draw_networkx_labels(B, pos=positions)
    plt.savefig((str(numNodes)+"bipartite.png"), dpi=300)
    #plt.show()
    adjlist=[]
    x = nx.convert.to_dict_of_lists(B)
    for i in x.values():
        adjlist.append(i)
  
    return adjlist,B,positions


def hypercube(n):
    plt.clf()
    if n==0:
        x= nx.Graph()
        x.add_node(0)
    else:
        x=nx.generators.lattice.hypercube_graph(n)
    positions = nx.spring_layout(x, scale=0.8)
    nx.draw(x, pos=positions,node_color='grey', width=1, edge_color="skyblue", style="solid")
    nx.draw_networkx_labels(x, pos=positions, font_size=10)
    r=0
    #nx.draw_networkx_labels(x, pos=positions,labels={p: r+1 for p in x})
    #plt.figure(figsize=(10.0,10.0))

    #fits everything in
    plt.margins(0.15)
    plt.savefig((str(n)+"hypercube.png"), dpi=800)#,figsize=(10.0,10.0))
    #plt.show()

    adjlist=[]
    h = nx.convert.to_dict_of_lists(x)
    for i in h.values():
        adjlist.append(i)

    z=[]
    y=[]
    for i in adjlist:
        for j in i:
            z.append(list(j))
        y.append(z)
        z=[]
    fdf={}
    counter=1
##    y.sort()
##    y.reverse()
    for i in y:
        for j in i:
            if j not in fdf.values():
                fdf[counter]=j#(counter)%(2**n)
                counter+=1
    aaaa=[]
    aa=[]
    for i in y:
        for j in i:
            for num,val in fdf.items():
                #print(num,val)
                if j==val:
                    aa.append(num)
                    break

        aaaa.append(aa)
        aa=[]
    print('aa',adjlist)
    print(y)
    print(fdf)
    print(aaaa)
    return aaaa,x,positions

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

def custom(adj):
    plt.clf()
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
    #plt.show()

    x = nx.convert.to_dict_of_lists(Graph)
    for i in x.values():
        adjlist.append(i)
  
    return adjlist,G,positions



def cycleDetection(G,positions):
    plt.clf()
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
                
    #positions = nx.spring_layout(G)
    edge_colour_list = [G[e[0]][e[1]]['color'] for e in G.edges()]
    nx.draw(G, pos=positions,node_color=node_colour_list,edge_color=edge_colour_list)
    #nx.draw_networkx_labels(G, pos=positions)
    try:
        nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    except:
        nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(len(node_colour_list))+"cycledetection.png"), dpi=300)
        
    
    
def bfs(adjlist,G,positions):
    print(adjlist)

    #visited list- check if bfs already seen
    visited=[0]*len(adjlist)
    queue=[]
    tour=[0]
    r=0
    queue.extend(adjlist[0])#=adjlist[0]

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
    plt.savefig((str(order)+"bfs.png"), dpi=300)

    #adds orange to first node 0 (which is node 1 on networkx graph)
    vColour[0]=colourList[colourCount]
    colourCount+=1

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
    plt.savefig((str(order)+"bfs.png"), dpi=300)

    #adds orange to first node 0 (which is node 1 on networkx graph)
    vColour[0]=colourList[colourCount]
    colourCount+=1

    #draws first COLOURED stage and saves
    order=1
    nx.draw(G, pos=positions,node_color=vColour)
    #nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(order)+"bfs.png"), dpi=300)

    order=2
    print(queue)
    print(adjlist)
    while(len(queue)!=0):
        a=len(queue)
        secondq=[]
        for i in queue:
            secondq.append(i)
        visited[r]=1

        #r keeps track of the first node in queue
        r=queue[0]
        tour.append(r)
        
        #everything thats in the queue at this moment in time must have come from the same node (if not already coloured)
        #therefore can be coloured the next colour in the list initialised at the top
        #save new drawn graph at each coloured node stage
        for i in queue:
            if vColour[i]=='#ffffff':
                vColour[i]=colourList[colourCount]
                nx.draw(G, pos=positions,node_color=vColour)
                #nx.draw_networkx_labels(G, pos=positions)
                plt.savefig((str(order)+"bfs.png"), dpi=300)
                order+=1
                #plt.show()
        
        colourCount+=1
        queue.remove(r)

        #add all unvisited nodes that are adjacent to the queue to repeat
        for x in secondq:
            for i in range(0,len(adjlist[x])):#and (x not in tour)
                if(visited[adjlist[x][i]]==0 and (adjlist[x][i] not in queue)):
                        queue.append(adjlist[x][i])
        print(queue)
        print(adjlist)
    print(vColour)
    return tour
