from queue import PriorityQueue

#Definition of a graph
#v: Represents the number of vertices in the graph.
#edges: Represents the list of edges in the form of a matrix. For nodes u and v, self.edges[u][v] = weight of the edge.
#visited: A set which will contain the visited vertices.
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        #-1 is base value if theres no edge between the vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight



#definition of dijkstra algorithm
def dijkstra(graph, start_vertex):
    #List with size of graph, all value to infinity
    D = {v:float('inf') for v in range(graph.v)}
    #start_vertex is definited with value 0
    D[start_vertex] = 0


    pq = PriorityQueue()
    pq.put((0, start_vertex))

    #As long as there is more vertices to look at
    while not pq.empty():
        #We set current vertex to vertex in the queue
        (dist, current_vertex) = pq.get()
        #Mark it as visited now
        graph.visited.append(current_vertex)

        #We then check for neighbors
        for neighbor in range(graph.v):
            #To which the connection must not be -1, as to which there wouldnt be an edge connecting them
            if graph.edges[current_vertex][neighbor] != -1:
                #We get the distance of the edge of current vertex and neighbor
                distance = graph.edges[current_vertex][neighbor]
                #We then check wether the neighbor has not been visited
                if neighbor not in graph.visited:
                    #If it hasn't we check if distance is shorter than existing distances
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    #We then return the dictionary of edge distances
    return D


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3) 

D = dijkstra(g, 0)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])