import networkx as nx
import matplotlib.pyplot as plt

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

##hypercube(0)
##hypercube(1)
##hypercube(2)
hypercube(3)
hypercube(4)
hypercube(5)


