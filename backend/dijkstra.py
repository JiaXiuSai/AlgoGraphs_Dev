import networkx as nx
import matplotlib.pyplot as plt

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def dijkstra(graph, source, target):
    queue = []
    visited = {}
    distance = {}
    shortest_distance = {}
    parent = {}

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
            print(backtrace(parent, source, target))
            #break
        for neighbor in graph[current]:
            if visited[neighbor] == False:
                distance[neighbor] = distance[current] + 1
                if distance[neighbor] < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = distance[neighbor]
                    parent[neighbor] = current
                    queue.append(neighbor)
    
    print(distance)
    print(shortest_distance)
    print(parent)
    print(target)

inf = float('inf')

#make user input in matrix to show edge weights between edges. I am assuming the graph is undirected.
#To show that there isn't an edge between i and j, user needs to input 'inf' in the table.

adj=[[0,1,1,0],
     [inf,0,0,0],
     [0,6,inf,4],
     [5,0,0,4]]

G=nx.Graph()

for i in range(len(adj)):
    for j in range(len(adj)):
        if (adj[i][j] != 'inf'):
           G.add_edge(i,j,weight= adj[i][j])


dijkstra(G,0,len(adj))
positions = nx.spring_layout(G)
nx.draw(G,pos=positions,node_color='orange', width=1, style="solid" )
nx.draw_networkx_labels(G, pos=positions, font_size=10)
plt.savefig((str(len(G))+"dijkstra.png"), dpi=300)
plt.show()

