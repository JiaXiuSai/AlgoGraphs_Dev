import networkx as nx
import matplotlib.pyplot as plt
import random

#note for mitchell
#for capturing the order of the images (and the right number), may
#need to return the order (in search algs) to
#ensure the right amount of images are collected

#ask jacob
#hyperecube n currently dimension, ask jacob how he is doing in front end, may need to send down the sq rooted version
# or change the for loops from 2**n to n
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

1. bfs
2. dfs
3. dijkstra
4. kruskal --- nope
5. cycle det


need adding/doing: temporal

!!!!!!!!!!temporal!!!!!!!!!

"""

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
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"cycle.png"), dpi=300)
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
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"star.png"), dpi=300)
    adjlist=[]
    x = nx.convert.to_dict_of_lists(G)
    for i in x.values():
        adjlist.append(i)
    return adjlist,G,positions


def tree(numNodes):
    plt.clf()
    G= nx.Graph()
    if numNodes == 1:
        G.add_node(0)
    elif numNodes > 1:
        G.add_node(0)
        for i in range(1,numNodes):
            G.add_node(i)
            prob = random.uniform(0,1)
            if prob>0.7:
                randy = random.randint(0,i-1)
                G.add_edge(randy,i)
            else:
                G.add_edge(i,i-1)
        
    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G)
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"tree.png"), dpi=300)
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
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"path.png"), dpi=300)
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
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(numNodes)+"complete.png"), dpi=300)
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
        #print(i)
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
    nx.draw_networkx_labels(B, pos=positions,labels={n: n+1 for n in B})
    nx.draw(B, pos=positions,node_color=colours)
    plt.savefig((str(numNodes)+"bipartite.png"), dpi=300)
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
    elif n==4:
        x= nx.Graph()
        for i in range(0,2**n):
            x.add_node(i)
        x.add_edge(0,1)
        x.add_edge(0,2)
        x.add_edge(0,3)
        x.add_edge(1,4)
        x.add_edge(1,5)
        x.add_edge(2,4)
        x.add_edge(2,6)
        x.add_edge(3,5)
        x.add_edge(3,6)
        x.add_edge(4,7)
        x.add_edge(5,7)
        x.add_edge(6,7)

        x.add_edge(8,9)
        x.add_edge(8,10)
        x.add_edge(8,11)
        x.add_edge(9,12)
        x.add_edge(9,13)
        x.add_edge(10,12)
        x.add_edge(10,14)
        x.add_edge(11,13)
        x.add_edge(11,14)
        x.add_edge(12,15)
        x.add_edge(13,15)
        x.add_edge(14,15)

        x.add_edge(0,8)
        x.add_edge(1,9)
        x.add_edge(2,10)
        x.add_edge(3,11)
        x.add_edge(4,12)
        x.add_edge(5,13)
        x.add_edge(6,14)
        x.add_edge(7,15)
        
    elif n==3:
        x= nx.Graph()
        for i in range(0,2**n):
            x.add_node(i)
        x.add_edge(0,1)
        x.add_edge(0,2)
        x.add_edge(0,3)
        x.add_edge(1,4)
        x.add_edge(1,5)
        x.add_edge(2,4)
        x.add_edge(2,6)
        x.add_edge(3,5)
        x.add_edge(3,6)
        x.add_edge(4,7)
        x.add_edge(5,7)
        x.add_edge(6,7)
        
    elif n==2:
        x= nx.Graph()
        for i in range(0,2**n):
            x.add_node(i)
        x.add_edge(0,1)
        x.add_edge(1,2)
        x.add_edge(2,3)
        x.add_edge(0,3)
        
    elif n==1:
        x= nx.Graph()
        for i in range(0,2**n):
            x.add_node(i)
        x.add_edge(0,1)
        
    positions = nx.spring_layout(x, scale=0.8)
    nx.draw(x, pos=positions,node_color='white', width=1, edge_color="black", style="solid")
    nx.draw_networkx_labels(x, pos=positions,labels={u: u+1 for u in x})

    #fits everything in
    plt.margins(0.15)
    plt.savefig((str(n)+"hypercube.png"), dpi=800)#,figsize=(10.0,10.0))

    adjlist=[]
    h = nx.convert.to_dict_of_lists(x)
    for i in h.values():
        adjlist.append(i)
    return adjlist,x,positions

def petersen():
    plt.clf()
    Graph = nx.petersen_graph()
    nx.draw_shell(Graph, nlist=[range(5, 10), range(5)],  font_weight='bold',node_color='white')
    positions = nx.shell_layout(Graph, nlist=[range(5, 10), range(5)])
    nx.draw_networkx_labels(Graph, pos=positions,labels={n: n+1 for n in Graph})
    plt.savefig(("petersen.png"), dpi=800)
    adjlist=[]
    x = nx.convert.to_dict_of_lists(Graph)
    for i in x.values():
        adjlist.append(i)
    return adjlist,Graph,positions


#custom([[0,0,1],[0,0,1],[1,1,0]])
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
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(len(adj))+"custom.png"), dpi=300)
    adjlist=[]
    x = nx.convert.to_dict_of_lists(G)
    for i in x.values():
        adjlist.append(i)
    return adjlist,G,positions

def cycleDetection(adjlist,G,positions):
    plt.clf()
    x=[]        
    try:
        x=list(nx.find_cycle(G, orientation="original"))
    except:
        pass

    G.add_nodes_from(G.nodes(), colour='never coloured')

    for e in G.edges():
            #print(e)
            G[e[0]][e[1]]['color'] = 'black'
            for i in x:
                if(((e[0]==i[0])and(e[1]==i[1]))or((e[1]==i[0])and(e[0]==i[1]))):
                    #print(i[0],e[0],i[1],e[1])
                    G[e[0]][e[1]]['color'] = 'red'

    node_colour_list=['white']*len(adjlist)
    order=0
    edge_colour_list = [G[e[0]][e[1]]['color'] for e in G.edges()]
    nx.draw(G, pos=positions,node_color=node_colour_list,edge_color=edge_colour_list)
    #nx.draw_networkx_labels(G, pos=positions)
    try:
        nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    except:
        nx.draw_networkx_labels(G, pos=positions)
    plt.savefig((str(order)+"cycledetection.png"), dpi=300)
    #colour nodes that are in the cycle
    order+=1
    for e in G.nodes():
            #print(e)
            coloured=False
            for i in x:
                if((e==i[0])):
                    node_colour_list[e]='pink'
                    coloured=True
                    break
            if(coloured==False):
                node_colour_list[e]='white'
            else:
                #positions = nx.spring_layout(G)
                edge_colour_list = [G[e[0]][e[1]]['color'] for e in G.edges()]
                nx.draw(G, pos=positions,node_color=node_colour_list,edge_color=edge_colour_list)
                #nx.draw_networkx_labels(G, pos=positions)
                try:
                    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
                except:
                    nx.draw_networkx_labels(G, pos=positions)
                plt.savefig((str(order)+"cycledetection.png"), dpi=300)
                order+=1
        
def bfs(adjlist,G,positions):
    #print(adjlist)

    #visited list- check if bfs already seen
    visited=[0]*len(adjlist)
    queue=[]
    tour=[0]
    r=0
    queue.extend(adjlist[0])#=adjlist[0]

    #keeps track of which index of colourList we are allowed to colour the node in
    colourCount=0
    colourList = ['#FFB6C1','#836FFF','#7FFFD4','#7D9EC0','#CAE1FF','#458B00','#FFFF00','#FFA07A','#F5DEB3','#FF3030','#CDC9C9','#EE7AE9','#A0522D','#00EE00','#FF9912','#E3CF57','#B3EE3A','#FF3E96','#00F5FF','#BF3EFF','#4876FF']
    #colourList=['orange','blue','yellow','red','purple','cyan','pink','green','grey','indigo']

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
##    print(queue)
##    print(adjlist)
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
##        print(queue)
##        print(adjlist)
##    print(vColour)
    return tour

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

    order=1
    visited = [False] * len(adjlist)
    s=0
    stack = [] 
    stack.append(s) 

    while (len(stack)): 
        # Pop a vertex from stack and print it 
        s = stack[-1] 
        stack.pop()

        # Stack may contain same vertex twice. So 
        # we need to print the popped item only 
        # if it is not visited. 
        if (not visited[s]): 
            #print(s,'\n')
            vColour[s]=colourList[colourCount]
            nx.draw(G, pos=positions,node_color=vColour)
            #nx.draw_networkx_labels(G, pos=positions)
            plt.savefig((str(order)+"dfs.png"), dpi=300)
            order+=1
            visited[s] = True
        #print(vColour)
        # Get all adjacent vertices of the popped vertex s 
        # If a adjacent has not been visited, then push it 
        # to the stack. 
        for node in adjlist[s]: 
            if (not visited[node]): 
                stack.append(node)

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def dijkstra(adjlist,graph,positions,source,target):
    source=source-1
    target=target-1
    queue = []
    visited = {}
    distance = {}
    shortest_distance = {}
    parent = {}

    colours=['white']*len(adjlist)

    for node in range(len(graph)):
        distance[node] = None
        visited[node] = False
        parent[node] = None
        shortest_distance[node] = float("inf")

    queue.append(source)
    distance[source] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        visited[current] = True
        if current == target:
            shortpath = (backtrace(parent, source, target))
            #print('s',shortpath)
        for neighbor in graph[current]:
            if visited[neighbor] == False:
                distance[neighbor] = distance[current] + 1
                if distance[neighbor] < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = distance[neighbor]
                    parent[neighbor] = current
                    queue.append(neighbor)

    nx.draw(graph,pos=positions,node_color='white', width=1, style="solid" )
    try:
        nx.draw_networkx_labels(graph, pos=positions,labels={n: n+1 for n in graph})
    except:
        nx.draw_networkx_labels(graph, pos=positions)
    order=0
    plt.savefig((str(order)+"dijkstra.png"), dpi=300)
    plt.show()
    
    for i in shortpath:
        colours[i]='orange'
        order+=1
        nx.draw(graph, pos=positions,node_color=colours)
        try:
            nx.draw_networkx_labels(graph, pos=positions,labels={n: n+1 for n in graph})
        except:
            nx.draw_networkx_labels(graph, pos=positions)
        plt.savefig((str(order)+"dijkstra.png"), dpi=300)
        plt.show()



