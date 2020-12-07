import networkx as nx
import matplotlib.pyplot as plt
#import graph5

def bfs(adjlist):

    #visited list- check if bfs already seen
    visited=[0]*len(adjlist)
    queue=[]
    tour=[0]
    r=0
    queue=adjlist[0]


    #keeps track of which index of colourList we are allowed to colour the node in
    colourCount=0
    colourList=['orange','blue','yellow','red','purple']

    #initialise an all white list for the nodes that have not yet been coloured
    #will get coloured as we go on
    vColour=['#ffffff']*len(adjlist)

    #draws first stage and saves (non coloured graph)
    nx.draw(G4, pos=positions,node_color=vColour)
    nx.draw_networkx_labels(G4, pos=positions)
    order=0
    plt.savefig((str(order)+"bfs.png"), dpi=300)

    #adds orange to first node 0 (which is node 1 on networkx graph)
    vColour[0]=colourList[colourCount]
    colourCount+=1

    #draws first COLOURED stage and saves
    order=1
    nx.draw(G4, pos=positions,node_color=vColour)
    nx.draw_networkx_labels(G4, pos=positions)
    plt.savefig((str(order)+"bfs.png"), dpi=300)

    order=2
    while(len(queue)!=0):
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
                nx.draw(G4, pos=positions,node_color=vColour)
                nx.draw_networkx_labels(G4, pos=positions)
                plt.savefig((str(order)+"bfs.png"), dpi=300)
                order+=1
                plt.show()
                
        
        colourCount+=1
        queue.remove(r)

        #add all unvisited nodes that are adjacent to the queue to repeat
        for i in range(0,len(adjlist[r])):
            if(visited[adjlist[r][i]]==0 and (adjlist[r][i] not in queue)):
                    queue.append(adjlist[r][i])
        		
    print(vColour)
    return tour




#old eg
##G6=graph5.Graph()
##positions = nx.spring_layout(G6)



#initialise graph - adj list sets and add edges in a for loop rather than one by one like below
G4= nx.Graph()
for i in range(1,9):
    G4.add_node(i)
G4.add_edge(1,4)
G4.add_edge(1,5)
G4.add_edge(1,6)
G4.add_edge(1,7)
G4.add_edge(1,8)
G4.add_edge(1,9)
G4.add_edge(3,2)
G4.add_edge(4,3)
G4.add_edge(2,1)

G4.add_nodes_from(G4.nodes(), colour='never coloured')
positions = nx.spring_layout(G4)


#print(bfs([[1],[0,2],[1,3],[2,4],[3]]))
#print((bfs([[2,3,4],[0,3],[0,1],[0,1],[0]])))
##print(bfs([[2],[3,4],[0,4],[1],[1,2]]))


#bit confusing - nodes on this start at 0 because of indexing, but networkx starts from 1. will change if possible
print(bfs([[1,3,4,5,6,7,8],[0,2],[1,3],[0,1,2],[0],[0],[0],[0],[0]]))



