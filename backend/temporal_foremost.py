import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations


def temporal_foremost(num,max_life,src):
    src=src-1
##    if num <1 or num>10:
##        print("please ennter number of nodes between 1 and 10")
##        exit()
        
    vertices=[]
    for i in range(num):
        vertices.append(i)

    

    
##    if check not in vertices:
##        print("please ennter a source vertex between 1 and your max no. of nodes")
##        exit()
##
##    if max_life < (2*num):
##        print("please enter max_life which is atleast twice the number of nodes")
##        exit()
##
##    if max_life > 20:
##        print("please enter max_life which is atleast twice the number of nodes and not more than 2")
##        exit()
    

        
    edges_not_used= list(combinations((vertices),2)) #getting all possible combinations of length 2
    #print("combinations possible",edges_not_used)
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
        lst1=[]
        G.remove_edges_from(list(G.edges()))
        for k in range(0,num):
            for q in range(0,num):
                probability = random.uniform(0, 1)
                if(k!=q):#edges created with random probability
                    if(probability<(1/(num))): #create random edges at diff times
                        
                        if((k,q) in edges_not_used) or ((q,k) in edges_not_used):
                            if j==0:
                                k=src
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

                
    #If dest and source vertex found, we apply algorithm to find shortest path

    S=[] #creating a list called 'S' of (u,v) and (v,u) edges since our graph is undirectes 
    for i in range(len(main)):
        new=[]
        for each in main[i]:
            a=each[0]
            b=each[1]
            one= (a,b)
            swap=(b,a)
            new.append(one)
            new.append(swap)
        S.append(new)

        
    #print("S",S)
    null='-'
    
    vertices_traversed=[src]
    parents={}
    arrival_time={}
    parents[src]= null
    arrival_time[src]= 0

    #Part of the algorithm
    #finding time at which edges appear and adding it to the dict arrival_time
    #setting parents of all vertices to null
    
    for i in range(len(S)):
        for each in S[i]:
            if each[0] not in vertices_traversed:
                vertices_traversed.append(each[0])
                arrival_time[each[0]]= i+1
                parents[each[0]]= null
            if each[1] not in vertices_traversed:
                vertices_traversed.append(each[1])
                arrival_time[each[1]]= i+1
                parents[each[1]]= null
        
    #print("arrival_time",arrival_time)
    #print("parents",parents)

    #dst here is the vertex that appears latest
    dst=vertices_traversed[-1]
    
    R= [src]

    #print("R",R)
    #print("dst",dst)

    for l in range(len(S)):
        for each in S[l]:
            a=each[0]
            b=each[1]
            if (a in R and b not in R): #main algorithm of foremost jounrey
                if arrival_time[a] < l+1:
                    parents[b]= a
                    arrival_time[b]= l+1
                    R.append(b)
            elif (b in R and a not in R): #i have also taking reverse since our graph is undirected 
                if arrival_time[b] < l+1:
                    parents[a]= b
                    arrival_time[a]= l+1
                    R.append(a)


    #print("arrival_time",arrival_time)
    #print("parents",parents)
    #print("R222",R)

    traverse=[] #to add all edges in the order they will be traversed
    for i in range(max_life):
        for each in arrival_time:
            if (arrival_time[each]==i):            
                lst2=(parents[each],each)
                traverse.append(lst2)
    

    del traverse[0]
    #print("traverse",traverse)
    
   
    final=0 #to calculage total time taken
    if len(R)!= len(vertices):
        print("Path not found, you can try again by increasing max_life")
        exit()
        
    for i in vertices:
        final+= arrival_time[i]
    #print("final",final)


    G.remove_edges_from(list(G.edges())) #to label edges with time at which they appear
    for each in traverse:
         G.add_edge(each[0],each[1])
         G[each[0]][each[1]]['time'] = arrival_time[each[1]]

    labels={} #to label nodes, source node also labelled
    for n in G.nodes:

        #print(n)
        if n==src:
            labels[n]= str(n+1) + '$: SOURCE$'
            
        else:
            labels[n]= n+1
            
    plt.clf()#Plotting edges from the list traversed
    main.append(lst1)
    nx.draw(G, pos=positions,node_color='white')
    nx.draw_networkx_labels(G, pos=positions,labels=labels)
    
    b=dict(((u, v), d) for u, v, d in G.edges(data=True))
    nx.draw_networkx_edge_labels(G,pos=positions, edge_labels=b ,font_color='red')
    final=str(max_life+1)
    name_of_final= final+ "temporal.png" 

    plt.savefig((name_of_final), dpi=250)



    return G.edges 

#temporal_foremost(no_of_nodes, max_life,source_node)    
f =temporal_foremost(10,20,1)

#no_of_nodes(n): 1 to 10  
#max_life: >= 2n and max 20
#enter source_vertex

