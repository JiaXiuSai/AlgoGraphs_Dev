
import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations

def temporal(num,max_life):

##    if num <1 or num>10:
##        print("please ennter number of nodes between 1 and 10")
##        exit()
        
    vertices=[]
    for i in range(num):
        vertices.append(i)
    

##    if max_life < (2*num):
##        print("please enter max_life which is atleast twice the number of nodes")
##        exit()

##    if max_life > 20:
##        print("please enter max_life which is atleast twice the number of nodes and not more than 2")
##        exit()
        
    edges_not_used= list(combinations((vertices),2)) #getting all possible combinations of length 2
   # print("combinations possible",edges_not_used)
    plt.clf() #used to clear the current figure
    G= nx.Graph()
    order=0
    
    for i in range(0,num):
        G.add_node(i)
        
    G.add_nodes_from(G.nodes(), colour='never coloured')
    positions = nx.spring_layout(G,scale=0.2)
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
    plt.savefig((str(order)+"temporal.png"), dpi=300)
    order+=1
    
    main=[]
    for j in range(0,max_life):
        #print("j",j)
        lst1=[]
        G.remove_edges_from(list(G.edges()))
        for k in range(0,num):
            #print("k",k)
            for q in range(0,num):
                #print("q",q)
                probability = random.uniform(0, 1)
                if(k!=q):#edges created with random probability
                    if(probability<(1/(num))): #create random edges at diff times
                        
                        if((k,q) in edges_not_used) or ((q,k) in edges_not_used):
                            vertices_traversed= (k,q)
                            lst1.append(vertices_traversed)
                            G.add_edge(k,q)
                            if(k,q) in edges_not_used:
                                edges_not_used.remove((k,q))
                            if(q,k) in edges_not_used:
                                edges_not_used.remove((q,k))
                            
        plt.clf()
        main.append(lst1)
        nx.draw(G, pos=positions,node_color='white')
        nx.draw_networkx_labels(G, pos=positions,labels={n: n+1 for n in G})
        plt.savefig((str(order)+"temporal.png"), dpi=300)
        order+=1

                
    return G.edges 

#temporal(no_of_nodes, max_life,source_node)    
f =temporal(10,20)

#no_of_nodes(n): 1 to 10  
#max_life: >= 2n and max 20
#enter source_vertex
