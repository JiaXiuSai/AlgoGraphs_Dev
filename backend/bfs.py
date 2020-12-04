import networkx as nx
import matplotlib.pyplot as plt
import graph4
import copy

#hello pal, need to figure out how to save each stage of the folours. issue you are having is that when u append to big
#big list, the colourassignemnt overwrites the lsit
global colourBox
colourBox=[]

global colourAssignment
colourAssignment=[]

global bigbig
bigbig=[]

global dic
dic={}

def bfs(G,a,b):
    i=0
    count=0
    smallNeighbours=[]
    bigNeighbours=[]
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.nodes[a]['label'] = 0
    global colourAssignment
    colourAssignment=['']*9
    global bigbig
    global dic
    global colourBox
    colourCount=0

    print('COCLOURAdd', colourAssignment)

    n = len(G.nodes())
    listOfColours = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4']
    x=listOfColours[colourCount]
    colourBox.append(x)
    colourAssignment[0]=x
    bigbig.append(colourAssignment)
    
    #print(bigbig[-1])
    colourCount+=1
    G4=graph4.Graph()
    c=0
    positions = nx.spring_layout(G4)
    while (G.nodes[b]['label']==-1):
        #print('COCLOURAdd', colourAssignment)

        #p=set(colourAssignment)
        #bigbig.append(list(p))
        x=copy.deepcopy(colourAssignment)
        bigbig.append(x)

        dic[c]=colourAssignment
        c+=1

##        for i in range(0,len(colourAssignment)):
##            if colourAssignment[i]=='':
##                colourAssignment[i]='#ffffff'

        
        
##        nx.draw(G4, pos=positions,node_color=colourAssignment)
##        nx.draw_networkx_labels(G4, pos=positions)
##        plt.show()
        #break

##        for i in range(0,len(colourAssignment)):
##            if colourAssignment[i]=='#ffffff':
##                colourAssignment[i]=''

        
       # print('\n')
    
      #  print('l',bigbig)
        for u in range(1,n):
            if (G.nodes[u]['label']==i):
                for v in G.neighbors(u):
                    if (G.nodes[v]['label']==-1):
                        G.nodes[v]['label']=i+1
                        smallNeighbours.append(v)
                        x=listOfColours[colourCount]
                        colourBox.append(x)
                        
                        G.nodes[v]['colour']=x
                       # print(u,count,v)

                        if(colourAssignment[v-1]==''):
                            colourAssignment[v-1]=x

                        
                      #  print('colour', colourBox)
                       # print('colodddur', colourAssignment)

        plt.show()        
        bigNeighbours.append(smallNeighbours)
        smallNeighbours=[]
        colourCount+=1
        count+=1
        i=i+1
       # print(bigNeighbours)
       # print(smallNeighbours)

            
    #return G.nodes[b]['label']                

 
print('Graph G4:')
G=graph4.Graph()
##print('From Node 1 to 9, answer is:',bfs(G,1,9))
bfs(G,1,9)

##positions = nx.spring_layout(G)
##
##
##nx.draw(G, pos=positions,node_color=colourAssignment)
##nx.draw_networkx_labels(G, pos=positions)
##plt.show()

print('////////////////////////')
for i in bigbig:
    print(i)
    

for i in range(0,len(bigbig)):
    for j in range(0,len(bigbig)):
        if(bigbig[i][j]==''):
            print('yrs')
            bigbig[i][j]="#ffffff"


print('d',dic)
a=[['#e6194b', '#3cb44b', '#3cb44b', '#3cb44b', '#3cb44b', '#ffe119', '#ffe119', '#ffe119', '#4363d8'],
   ['#e6194b', '#3cb44b', '#3cb44b', '#ffffff', '#3cb44b', '#ffe119', '#ffffff', '#ffe119', '#4363d8'],
   ['#e6194b', '#3cb44b', '#3cb44b', '#3cb44b', '#3cb44b', '#ffe119', '#ffe119', '#ffe119', '#4363d8'],
   ['#e6194b', '#3cb44b', '#3cb44b', '#3cb44b', '#3cb44b', '#ffe119', '#ffe119', '#ffe119', '#4363d8']]
print(len(bigbig))
G4=graph4.Graph()
positions = nx.spring_layout(G4)

aa=[]
setBig=[]

fire=copy.deepcopy(colourAssignment)

fire=sorted(set(fire), key=fire.index)

print('firee,',fire)

print(colourAssignment)


G4=graph4.Graph()
positions = nx.spring_layout(G4)
aa.append(colourAssignment[0])
##fire.remove(fire[0])
for j in range(1,len(colourAssignment)):
    for i in range(0,len(colourAssignment)-1):
        print('lalalala',colourAssignment[i],aa[-1])
        print('i,j',i,j)
        if(colourAssignment[i] == aa[-1] and colourAssignment[i+1] == aa[-1]):
            aa.append(colourAssignment[i])

    for k in range(len(aa),len(colourAssignment)):
        print('k',k)
        aa.append('#ffffff')
    print('aa',aa)
    nx.draw(G4, pos=positions,node_color=aa)
    nx.draw_networkx_labels(G4, pos=positions)
    plt.show()
    while '#ffffff' in aa:
        #print('\n','blah',i)
        aa.remove('#ffffff')
    print('aa',aa)
    fire.remove(fire[0])
    aa.append(fire[0])
    
    print('aafire',aa)
    
for i in range(0,len(bigbig)):

    nx.draw(G4, pos=positions,node_color=colourAssignment)
    nx.draw_networkx_labels(G4, pos=positions)
    plt.show()


X = nx.bidirectional_shortest_path(G,1,9)
print('ANSWER SHOULD BE',X)
